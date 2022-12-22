def romanToInt(s):
    otptint= 0
    rmints=list(s)
    i=0
    while i<len(rmints):
        dig=rmints[i]
        match dig:
            case "M":
                otptint += 1000
                i += 1
            case "D":
                otptint += 500
                i += 1
            case "C":
                try:
                    if rmints[i+1] == "D":
                        otptint +=400
                        i += 2
                    elif rmints[i+1] == "M":
                        otptint += 900
                        i += 2
                    else:
                        otptint += 100
                        i += 1
                except:
                    otptint += 100
                    i += 1
            case "L":
                otptint += 50
                i += 1
            case "X":
                try:
                    if rmints[i+1] == "L":
                        otptint +=40
                        i += 2
                    elif rmints[i+1] == "C":
                        otptint += 90
                        i += 2
                    else:
                        otptint += 10
                        i += 1
                except:
                        otptint += 10
                        i += 1
            case "V":
                otptint += 5
                i += 1
            case "I":
                try:
                    if rmints[i+1] == "V":
                        otptint +=4
                        i += 2
                    elif rmints[i+1] == "X":
                        otptint += 9
                        i += 2
                    else:
                        otptint += 1
                        i += 1
                except:
                        otptint += 1
                        i += 1                    
    print(otptint)
romanToInt("MCMXCIV")
