name = input("Введите свое имя ")
first_name = input("Введите свою фамилию ")
age = int(input('Введите свой возраст '))

if (age >= 18):
    print("Уважаемый",first_name,name,"Вам ",age,"лет. И вы уже достаточно взрослый.")
else:
    print("Уважаемый",first_name,name,"Вам ",age,"лет. И вам расти еще и расти.")