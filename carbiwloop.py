import random

# สุ่มตัวเลข 1-100
answer = random.randint(1, 100)

count = 0  # นับจำนวนครั้งที่ทาย

while True:
    guess = int(input("ทายตัวเลข (1-100): "))
    count += 1

    if guess > answer:
        print("มากไป")
    elif guess < answer:
        print("น้อยไป")
    else:
        print(f"ถูกต้อง! คุณทายทั้งหมด {count} ครั้ง")
        break