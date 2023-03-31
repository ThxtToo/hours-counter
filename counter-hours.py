hours = 1
minutes = 00
counterPlus = 15
meridiem = "AM"
pointer = 1

while pointer <= 92:
    print(hours, ":", minutes, meridiem)
    minutes += counterPlus
    if minutes >= 46:
        minutes = 0
        hours += 1
    if hours >= 13:
        meridiem = "PM"
        hours = 1
    pointer += 1
    
#i cant show 12 pm... but it works for me