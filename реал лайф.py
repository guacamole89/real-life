day = 1
satiety = 0
money = 30
health = 30
success = 40
while True:
    print('Чтобы выйти из введите 5')
    while True:
        if success < 0 or satiety < 0 or money < 0 or health < 0:
            break
        if success >= 100 and money >= 100:
            print('Вы победили')
            break
        if success >= 100:
            success = 100
        if satiety >= 100:
            satiety = 100
        if health >= 100:
            health = 100
        if money >= 100:
            money = 100
        if day == 1 or day == 2 or day == 3:
            print(f'Здоровье: {health} Деньги: {money} Успеваемость: {success} Сытость: {satiety}')
            print(f'Сейчас день, выберите действие: '
                  f'\n1)Сходить на пары(Успеваемость: +5 Сытость:  -15 Деньги:  -5 Здоровье:  -10)'
                  f'\n2)Работа(Деньги: +15 Успеваемость: -5 Сытость: -15 Здоровье -5)'
                  f'\n3)Закрыть долги(Успеваемость: +10 - +30 Сытость: -10 - -30 Здоровье 0 - -10)'
                  f'\n4)Поесть(Сытость: +20)'
                  f'\n5)Пойти на пробежку(Здоровье +15)')
            choice1 = int(input())
            if choice1 == 1:
                satiety -= 10
                health -= 5
                success += 5
                print(f'Здоровье: {health}\nДеньги: {money} \nУспеваемость: {success} \nСытость: {satiety}')
                print('Идти на пары:\n1)Пешком\n2)Транспорт')
                choice2 = int(input())
                if choice2 == 1:
                    health -= 5
                    satiety -= 15
                elif choice2 == 2:
                    money -= 5
                else:
                    print('Вы нажали не ту кнопку')
                    break
            elif choice1 == 2:
                money += 15
                success -= 5
                satiety -= 15
                health -= 5
            elif choice1 == 3:
                print(f'Здоровье: {health}\nДеньги: {money} \nУспеваемость: {success} \nСытость: {satiety}')
                print('Какие предметы закрывать:\n'
                      '1)Лёгкие(Успеваемость: +10 Сытость: -10)'
                      '\n2)Сложные(Успеваемость: +20 Сытость: -20)'
                      '\n3)Супер сложные(Успеваемость: +30 Сытость: -30)')
                choice3 = int(input())
                if choice3 == 1:
                    success += 10
                    satiety -= 10
                elif choice3 == 2:
                    success += 20
                    satiety -= 20
                    health -= 5
                elif choice3 == 3:
                    success += 30
                    satiety -= 30
                    health -= 10
                else:
                    print('Вы нажали не ту кнопку')
                    break
            elif choice1 == 4:
                satiety += 20
            elif choice1 == 5:
                health += 15
            else:
                print('Вы нажали не ту кнопку')
                break
            day += 1
            if day == 4:
                day = 0
        elif day == 0:
            print(f'Здоровье: {health}\nДеньги: {money} \nУспеваемость: {success} \nСытость: {satiety}')
            print(f'Сейчас ночь, выберите действие: \n1)Спать(Здоровье: +10 Сытость: -5)'
                  f'\n2)Учить уроки(Успеваемость: +10 Здоровье: -5)')
            choice1 = int(input())
            if choice1 == 1:
                health += 10
                satiety -= 5
            elif choice1 == 2:
                success += 10
                health -= 5
            else:
                print('Вы нажали не ту кнопку')
                continue
            day += 1
        else:
            print('Вы нажали не ту кнопку')
            break

    if success < 0 or satiety < 0 or money < 0 or health < 0:
        print('Вы проиграли')
        break
    if success >= 100 and money >= 100:
        break

    print('Вы хотите выйти из игры?\nДа/Нет')
    x = input()
    if x == 'Да':
        break
    else:
        continue
print('Игра окончена')