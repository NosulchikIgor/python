n = int(input("Введите желаемое целое положительное число "))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
       max = n % 10
print("Самая большая цифра в вашем числе равна", max)
