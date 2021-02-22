day_of_call= input("Enter the day the call started at: ")
time_of_call= int(input("Enter the time the call started at (hhmm): "))
call_duration= int(input("Enter the duration of the call (in minutes): "))
if(day_of_call=="Sat" or day_of_call=="Sun"):
    callrate=.15
else :
    if(800<=time_of_call<=1800):
        callrate=.4
    else :
        callrate=.25

cost_of_call=call_duration*callrate

print ("This call will cost ${:2.2f}".format(cost_of_call))