print("Мини игра")
first = 0
while True:
    first = int(input("Введите ваше число а я скажу больше оно 10 или меньше:"))
    if first < 10:
        print("Ваше число меньше 10")
    elif first > 10:
        print("ваше число болше десяти")
    elif first == 10:
        print("Ваше число равно десяти")
    else:
        print("Вы ввели не число по пробуйте ещё раз")