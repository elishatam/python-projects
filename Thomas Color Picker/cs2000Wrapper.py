import time
import re
import serial
from scipy.optimize import minimize

class CS2000:

    def __init__(self, file=None, mode='spectral', log=True):
        self.tag = "CS2000 WRAPPER:\t"
        self.log = log
        self.id = 'cs2000 camera'
        self.ser = serial.Serial()
        self.baud = 9600
        self.port = 'COM3'
        self.MAX_CONN_ATTEMPTS = 3
        self.fpath = file
        self.mode = mode
        self.f = self.open()


        self.setRemote(1)
        self.setSpeed(1)

        if self.log:
            print(self.tag + 'initiated CS2000')

    def open(self):
        self.ser = serial.Serial()
        self.ser.timeout = 5
        self.ser.baudrate = self.baud
        self.ser.port = self.port
        self.ser.open()

        if self.fpath is not None:
            f = open(self.fpath, 'w')
            if 'spect' in self.mode:
                headers = 'x-pos\ty-pos\t' + "\t".join([str(lam) for lam in range(380, 781)])+ '\n'
            else:
                headers = 'x-pos\ty-pos\tX\tY\tL\n'
            f.write(str(headers))
        else:
            f = None
        return f

    def getemptystring(self):
        return '                                                                                                                                                                                                                                                                        '

    def setRemote(self,n):
        if n > 0:
            s = 'RMT,1\r'
        else:
            s = 'RMT,0\r'

        try:
            self.ser.write(s.encode(encoding='UTF-8'))
            ret = self.wait_for_response()
            if self.log:
                print(self.tag + " returned {0}".format(ret.replace("\r\n", "\t")))
        except Exception:
            return 1

        return 0

    def setSpeed(self, prm):
        s = 'SPMS,'+str(prm)+'\r'

        try:
            self.ser.write(s.encode(encoding='UTF-8'))
            ret = self.wait_for_response()
            if self.log:
                print(self.tag + " returned {0}".format(ret.replace("\r\n", "\t")))
        except Exception:
            return 1

        s = 'SPMr,' + str(prm) + '\r'

        try:
            self.ser.write(s.encode(encoding='UTF-8'))
            ret = self.wait_for_response()
            if self.log:
                print(self.tag + " returned {0}".format(ret.replace("\r\n", "\t")))
        except Exception:
            return 1

        return 0

    def measure_subroutine(self):
        s = "MEAS,1" + "\r"
        try:
            self.ser.write(s.encode(encoding='UTF-8'))
            ret = self.wait_for_response()
            return self.check_error(ret)
        except Exception:
            return 1

    def measure(self,xpos=None,ypos=None):
        ret = self.measure_subroutine()
        if ret < 0:
            return ret

        # READING
        try:
            if "spect" in self.mode:
                ret = ''
                for i in range(1, 5):
                    s = "MEDR,1,0,"+str(i)+"\r"
                    self.ser.write(s.encode(encoding='UTF-8'))
                    ret = self.wait_for_response()
                    retVal = self.check_error(ret)
                    if retVal < 0:
                        return retVal
                    elif retVal == 1:
                        ret = self.wait_for_data()
                    tmp = ret.split(',')
                    tmp = [val.replace('\r', '') for val in tmp]
                    tmp = [val.replace('\n', '') for val in tmp]
                    ret += ",".join(tmp[1:])
            else:
                s = "MEDR,2,0,02\r\n"
                self.ser.write(s.encode(encoding='UTF-8'))
                ret = self.wait_for_response()
                self.debug_print(ret)
                retVal = self.check_error(ret)
                if retVal < 0:
                    return retVal
                elif retVal == 1:
                    ret = self.wait_for_data()

        except Exception:
            return 1

        # post processing return string ret for spectral and color info
        if "spect" in self.mode:
            # Formatting position and spectral info
            xpos = abs(xpos)
            ret = ret.replace("OK00,", "")
            ret = ret.replace("\n", "")
            ret = ret.replace("\r", "")

            # reading the x y and L from camera
            s = "MEDR,2,0,02\r\n"
            self.ser.write(s.encode(encoding='UTF-8'))
            xyL = self.wait_for_response()
            self.debug_print(xyL)
            retVal = self.check_error(xyL)
            if retVal < 0:
                return retVal
            elif retVal == 1:
                xyL = self.wait_for_data()
            x, y, L = self.parseXYL(xyL)

            if self.f is not None:
                # Creating output
                output1 = str.format('{0:.4f}', xpos) + ',' + \
                          str.format('{0:.4f}', ypos) + ',' + \
                          str.format('{0:.4f}', x) + ',' + \
                          str.format('{0:.4f}', y) + ',' + \
                          str.format('{0:.4f}', L) + ',' + \
                          ret
                self.debug_print('Writing "' + output1 + '"')

                # Writing to file
                self.f.write(output1+"\n")

            return x, y, L
        else:
            # reading the x y and L from camera
            s = "MEDR,2,0,02\r\n"
            self.ser.write(s.encode(encoding='UTF-8'))
            xyL = self.wait_for_response()
            self.debug_print(xyL)
            retVal = self.check_error(xyL)
            if retVal < 0:
                return retVal
            elif retVal == 1:
                xyL = self.wait_for_data()
            x, y, L = self.parseXYL(xyL)

            if self.f is not None:
                xpos = abs(xpos)
                output1 = str.format('{0:.4f}', xpos) + ',' + str.format('{0:.4f}', ypos) + ',' + str.format('{0:.4f}', x) + ',' + str.format('{0:.4f}', y) + ',' + str.format('{0:.4f}'+'\n', L)
                self.debug_print('Writing "' + output1 + '"')
                self.f.write(output1.replace("OK00,", "")+"\n")

            return x, y, L

    def cleanup(self):
        if self.log:
            print(self.tag + 'ending...')
        self.ser.close()
        self.f.close()
        return 0

    @staticmethod
    def parseXYL(string):
        splt = string.split(",")
        x = float(splt[1].replace('\r\n', ''))
        y = float(splt[2].replace('\r\n', ''))
        L = float(splt[3].replace('\r\n', ''))

        return x, y, L

    def parseSpectral(self, string):
        splt = string.split(",")
        non_decimal = re.compile(r'[^\d.]+')
        return non_decimal

    def wait_for_response(self):
        r = ''
        count = 0
        while len(r) == 0:
            if count > 1000:
                if self.log:
                    print(self.tag + "FATAL ERROR: Could not read from CS2000 after 100 seconds, quitting")
                self.cleanup()
                quit()
            r = str(self.ser.read_all().decode())
            time.sleep(0.1)
            count += 1
        self.debug_print(r)
        return r

    def wait_for_data(self):
        count = 0
        while True:
            if count > 1000:
                if self.log:
                    print(self.tag + "FATAL ERROR: Could not read data from CS2000 after 100 seconds, quitting")
                self.cleanup()
                quit()
            r = str(self.ser.read_all().decode())
            if len(r) > 0:
                self.debug_print(r)
                retVal = self.check_error(r)
                if retVal < 0:
                    if self.log:
                        print(self.tag + "FATAL ERROR, quitting")
                    self.cleanup()
                    quit()
                elif retVal == 0:
                    break
            time.sleep(0.1)
            count += 1

        return r

    def check_error(self, r):
        if "ER00" in r:
            if self.log:
                print(self.tag + 'Input Error, Invalid command for CS2000!')
            return -100
        elif "ER10" in r:
            if self.log:
                print(self.tag + 'Error, Over CS2000 measurement range')
            return -10
        elif "ER17" in r:
            if self.log:
                print(self.tag + 'Parameter Error, CS2000 busy')
            return 1
        elif "ER20" in r:
            if self.log:
                print(self.tag + 'No Measurement Data available, CS2000 may be measuring...')
            return 1
        elif "OK00" in r:
            if self.log:
                print(self.tag + 'CS2000 Action Completed')
            return 0
        else:
            if self.log:
                print(r)
                print(self.tag + 'Unknown Error, quitting...')
            return -1

    def debug_print(self, s):
        if self.log:
            print(self.tag + s.replace('\r', '\t').replace('\n', '\t'))

    def test(self):
        if self.log:
            print(self.tag + '##### test cs2000 commencing #####')
        ret = self.measure(0, 0)

        if self.log:
            print(ret)
            print(self.tag + '##### test cs2000 completed #####')
