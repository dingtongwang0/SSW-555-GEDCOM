from datetime import datetime

def us04(marrdate, divdate, hubname, wifename):
    res = True
    if marrdate > divdate:
        error_us04 = "Error US04: Divorce of " + hubname + " and " + wifename + " happens before their marriage date.\n"
        print(error_us04)
        res = False

    return res