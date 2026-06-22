print("โปรเเกรมคำนวณ Total score\n")
Physics = int(input("คะเเเนนวิชาฟิสิกส์ "))
chemical = int(input("คะเเเนนวิชาเคมี "))
Biology = int(input("คะเเเนนวิชาชีวะ "))
total = Physics + chemical + Biology
averag = total/3

if averag < 60:
    print("คะเเนนรวมของคุณคือ" , averag)
    print("ควรพยายามให้มากกกว่านี้นะ")
elif averag < 80:
    print("คะเเนนรวมของคุณคือ" , averag)
    print("ผ่าน")
else:
    print("คะเเนนของคุณคือ" , averag)
    print("เก่งมาก")