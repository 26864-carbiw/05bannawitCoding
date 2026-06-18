point1 = int(input("คะเเเนนวิชา 1 "))
point2 = int(input("คะเเเนนวิชา 2 "))
point3 = int(input("คะเเเนนวิชา 3 "))

total_point = point1 + point2 + point3
average = total_point/3

if average <60:
    print("คะเเนนเฉลี่ยรวมของคุณคือ" , average)
    print("ควรปรับปรุง")
elif average <80:
    print("คะเเนนเฉลี่ยรวมของคุณคือ" , average)
    print("ผ่าน")
else:
    print("คะเเนนเฉลี่ยรวมของคุณคือ" , average)
    print("ดีเยี่ยม")