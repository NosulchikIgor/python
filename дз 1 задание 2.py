time = int(input("Введите время в секундах "))

hour = time // 3600
minute = (time % 3600) // 60
second = (time % 60)

# форматирование строки первым способом
print(f"Ваш результат составит {hour:02d}:{minute:02d}:{second:02d}")

# форматирование другим вариантом
time_look = "Ваш результат составит %i:%i:%i"
print(time_look %(hour,minute,second))

# форматирование третьим вариантом
template = "Ваш результат составит {}:{}:{}"
print(template.format(hour,minute,second))
