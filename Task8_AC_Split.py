# AC/Split for automatically adjust the AC setting once the room temperature is so col

temp = int(input("Enter Temperature "))
while True:
    if temp > 20:
        print("compressor is Switch ON Now")
        temp = temp - 1
    elif temp < 15:
        print("compressor is Switch OFF Now")
        temp = temp - 1
        break
    else:
        print("AC Compressor is Working on ", temp)
        temp = temp-1


