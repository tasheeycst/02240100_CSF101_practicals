print("enter the lowest temperature in celsius ")
lowTemp = int(input())
if lowTemp < -50:
    print("invalid input ")
    print("enter the lowest temperature in celsius ")
    lowTemp = int(input())
print("enter highest temperature celsius ")
highTemp = int(input())
if highTemp > 50:
    print("invalid")
    print("enter highest temperature celsius ")
    highTemp = int(input())
avg = float(lowTemp + highTemp) / 2
print("the average temperature in celsius is : " + str(avg))
if avg > 20:
    print("volatile")
else:
    if avg < 10:
        print("moderate")
    else:
        print("stable")
fahren = avg * 33.8
print("celsius to fahren :" + str(fahren))
