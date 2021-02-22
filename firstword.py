def firstword(s): 
    space=s.find(" ")
    if(space!=-1):
        return s[:space]
    else :
        return s