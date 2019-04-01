import re

def test(s):
    # return "FAIL" if s causes Mozilla to crash
    # "PASS" if otherwise
    #if re.search("<SELECT[^>]*>", s) >= 0:
    if re.search("<SELECT[^>]*>", s) >= 0:
        return "FAIL"
    else:
        return "PASS"

print(test("<HTML>"))