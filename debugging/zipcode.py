# class ZIPCode:
#     #US Only
#     def __init__(self, zip):
#         self._zip = zip
#         #self.checkRep()
#
#     def zip(self):
#         return self._zip()
#
#     def checkRep(self):
#         assert len(self.zip()) == 5
#         for i in range(0,5):
#             assert '0' <= self.zip()[i] <= '9'
#         #assert 0 <= self.zip() <= 99999
#
# t = ZIPCode(12)
# print(t)


class ZIPCode:
    def __init__(self, zip):
        self._zip = zip
        self.checkRep()

    def zip(self):
        return self._zip

    def __repr__(self):  #representation
        return "{:s}".format(
            self.zip())

    def checkRep(self):  #Invariant checker. Checks if internal representation is sane
                        # Use at beginning or end of function, as appropriate
        assert len(self.zip()) == 5
        #assert 0 <= self.zip()   <= 99999
        for i in range(0,5):
            assert '0' <= self.zip()[i] <= '9'


t = ZIPCode('95070')
print(t)