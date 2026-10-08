num = int(input("Enter a number: "))
numd = int(input("Enter a divisor: "))

if num % numd == 0:
    print(num, "is divisible by", numd)
else:
    print(num, "is not divisible by", numd)