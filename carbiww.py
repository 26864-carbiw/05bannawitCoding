print("โปรเเกรมคำนวณ Total score\n")
Physics = int(input("คะเเนนวิชาฟิสิกส์ "))
chemical = int(input("คะเเนนวิชาเคมี "))
Biology = int(input("คะเเนนวิชาชีวะ "))
total = (Physics + chemical + Biology)
averag = (total/3)
print("\nคะเเนนรวมของคุณคือ" , averag)
if averag < 60:
    print("ควรพยายามให้มากกกว่านี้นะ")
elif averag < 80:
    print("คะเเนนรวมของคุณคือ" , averag)
    print("ผ่าน")
else:
    print("คะเเนนของคุณคือ" , averag)
    print("เก่งมาก")