class Time:
    def __init__(self, h=0, m=0, s=0):
        assert 0 <= int(h) <= 23
        assert 0 <= int(m) <= 59
        assert 0 <= int(s) <= 60
        self.checkRep()

        self._hours = int(h)   #convert input into integers
        self._minutes = int(m)
        self._seconds = int(s)

    def checkRep(self):  #Invariant checker. Checks if internal representation is sane
                        # Use at beginning or end of function, as appropriate
        assert 0 <= self.hours()   <= 23
        assert 0 <= self.minutes() <= 59
        assert 0 <= self.seconds() <= 60

    def hours(self):
        return self._hours
    def minutes(self):
        return self._minutes
    def seconds(self):
        return self._seconds

    def __repr__(self):  #representation
        return "{:02d}:{:02d}:{:02d}".format(
            self.hours(), self.minutes(), self.seconds())

    def seconds_since_midnight(self):
        return self.hours() * 3600 + self.minutes() * 60 + self.seconds()

    def advance(self, s):
        self.checkRep()
        old_seconds = self.seconds_since_midnight()

        #Some complex computation

        self.checkRep()
        assert (self.seconds_since_midnight() ==
                (old_seconds + seconds_offset) % (24 * 60 * 60))

t = Time(1.2, 0, 0)
print(t)