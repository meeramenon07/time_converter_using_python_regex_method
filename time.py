import re
def convert_time(time):
    hour,minute,second,am_pm = re.findall('\d+|\w+', time)
    hour = int(hour)
    if am_pm == "PM"  and hour != 12:
        hour += 12
    elif am_pm == "AM" and hour == 12 :
        hour = 0
    else:
        hour = hour
           
    return f' {hour:02d}: {minute}: {second}'
        
print(convert_time('12:20:00 AM'))          
        
    



