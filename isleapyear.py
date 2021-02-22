def isleapyear(s):
    if(s%4!=0):
        return False
    elif(s%100==0 and s%400!=0):
        return False
    else:
        return True