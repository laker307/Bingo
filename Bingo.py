import random as rnd

def start(spisok):
    for i in range(0, len(spisok)):
        p = spisok.pop(rnd.randint(0,len(spisok)-1))
        print('Номер случайного бочонка: ', p,'\nДостать ещё один бочонок? y/n')
        ans = input()
        if ans != 'y':
            print('Завершение работы')
            break
        if len(spisok) == 0: print('Все бочонки закончились!')


print('Введите количество бочонков: ')
n = input()
while True:
    if n.isdigit():
        if int(n) == float(n) and (int(n) > 0):
            break
        else:
            print('Введите число больше нуля!!!')
            n = input()
    else:
        print('Введите число больше нуля!!!')
        n = input()
spisok = [i for i in range(1, int(n)+1)]
print('Достать бочонок?')
h = input()
start(spisok)