c = int(input("เริ่มต้น : "))
s = int(input("สิ้นสุด : "))
for n in range(c,s+1):
 print("\nแม่",n)
 for i in range(1,13):
    print(n, "x",i,"=",n*i)
print("\nจัดทำโดย นายบรรณวิชญ์ วิเศษสุข")
