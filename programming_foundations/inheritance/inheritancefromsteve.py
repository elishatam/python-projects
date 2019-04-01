class AcquisitionServerThread(threading.Thread):
    """Thread to start the XISL acquisition server and restart if it crashes"""

    @staticmethod
    def __get_tcp_port():
        """Get an open port to use for acquisition server by temporarily binding a socket"""
        s = socket.socket()
        s.bind(("", 0))
        return s.getsockname()[1]

    def __init__(self):
        """Find an available TCP port and assign to this thread"""
        self.server_port = self.__get_tcp_port()
        self.stop_sema = threading.Semaphore(value=0)
        self.start_sema = threading.Semaphore(value=0)
        self.stopped_sema = threading.Semaphore()
        threading.Thread.__init__(self)

    def run(self):
        """Launch the acquisition server and restart when it crashes"""
        # Make sure the thread is not already running
        if not self.stopped_sema.acquire(timeout=0):
            raise RuntimeError("Acquisition server already started")

        # All output is printed to the console. CREATE_NEW_PROCESS_GROUP is used
        # to prevent CTRL+C from propagating to this child process
        logger.info("Starting acquisition server listening on port " + str(self.server_port))
        acq_server = Popen([config["acquire_server"], "-n", "-p", str(self.server_port)],
            stdin=PIPE, universal_newlines=True, creationflags=CREATE_NEW_PROCESS_GROUP)

        # Notify that the server has been started
        self.start_sema.release()

        # Check the server periodically and restart if necessary
        while not self.stop_sema.acquire(timeout=1):
            if acq_server.poll() is not None:
                acq_server = Popen([config["acquire_server"], "-n", "-p", str(self.server_port)],
                    stdin=PIPE, universal_newlines=True, creationflags=CREATE_NEW_PROCESS_GROUP)

        # Attempt to gracefully kill the server. Note that Acquisition_CloseAll()
        # is called on exit, but this only iterates through the descriptors local
        # to the process (i.e. other acquisition server processes are unaffected)
        try:
            logger.info("Killing acquisition server gracefully")
            acq_server.communicate(input="q\n", timeout=10)
        except Exception as e:
            logger.error("Could not gracefully kill acquisition server: " + str(e))
            try:
                logger.info("Killing acquisition server forcefully")
                acq_server.kill()
            except Exception as e:
                logger.error("Could not forcefully kill acquisition server: " + str(e))

        # Notify that the server has stopped
        self.stopped_sema.release()

    def stop(self):
        """Kill the acquisition server and stop the thread"""
        self.stop_sema.release()
        # Wait for the thread to stop
        self.stopped_sema.acquire()
        # Release the semaphore so run() can acquire it again
        self.stopped_sema.release()

    def wait_for_start(self):
        """Block until the acquisition server has started"""
        if not self.start_sema.acquire(timeout=5):
            raise RuntimeError("Could not start acquisition server")
