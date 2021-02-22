def remainingwords(s): 
    space=s.find(" ")
    if(space!=-1):
        return s[space+1:]
    else :
        return ""