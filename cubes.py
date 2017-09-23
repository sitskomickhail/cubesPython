from func_randA import *
from func_randB import *
from os import *
from time import *

print('\t\t\tЭто игра в кости!\n\t\t\tНачнем Игру!')
mround = 0
name = str(input('Введите ваше имя: '))
money = int(input('Введите количество ваших денег, '+name+' (в $): '))
print('Имя твоего противника: Opponent!\nУ вашего противника тоже',money,'$')
money_op = money
money_end = money
accept = str

RandNumA = 0    
RandNumB = 0


#Готовность к работе
while accept !='yes' or accept != 'y' or accept != 'Yes' or accept != 'Y' or accept != 'n' or accept != 'no':       #Повтор запроса для начала
        accept = input('\nВы готовы? Введите yes / no: ')
        if accept == 'yes' or accept == 'y' or accept == 'Yes' or accept == 'Y':
            break
        elif accept == 'no' or accept == 'n':
            end = int(input('Press Enter for exit'))
            exit(1)


while True:        
#main game
    while accept == 'y' or accept == 'Yes' or accept == 'yes' or accept == 'Y' and  money == 0 or money_op == 0:
        if mround == 0:
            sumi = 0
            sumi_op = 0
            mround = 0
            bet = 0
            quan_round = 1
            while mround < 1 or mround >= 50:           #Инициализация раундов
                while 1:
                    mround = input('\nВведите количество раундов: ')
                    try:
                        mround = int(mround)
                        break
                    except ValueError:
                        print('Это не число!')
                        
                if mround >= 50:
                    print("Too much!")   
                elif mround < 1:
                    print("Too low!")


            while bet < 1 or bet > money:           #Инициализация ставки
                
                print(name,'у вас есть', money,'$')
                print('У Opponent есть', money_op,'$')
                while 1:
                    bet = input('\nВведите вашу ставку: ')
                    try:
                        bet = int(bet)
                        break
                    except ValueError:
                        print('Это не число!')
                        
                if bet == money:
                    money -= bet
                    bet_op = bet
                    if money_op < bet:
                        print('У противника осталось', money_op,'$. All in')
                        bet_op = money
                        money_op -= bet_op
                        break
                    money_op -= bet_op
                    break
                
                elif bet > money:
                    print("У вас нет столько денег!")
                    continue
                elif bet < 1:
                    print("Too low!")
                    continue
                
                if money_op < bet:
                    print('У противника осталось', money_op,'$. All in')
                    money -= bet
                    bet_op = money
                    money_op -= bet_op
                    break
                
                money -= bet
                bet_op = bet
                money_op -= bet_op
                
            print('Противник поставил:', bet_op)

            
        while mround > 0:        
            print('\t\t\tRound № ', quan_round,'!')
            sleep(2)
            ready = input('Hажмите Enter, чтобы бросить кубик')
            print('Ваш черед:')
            sleep(1)
            for _ in range(0, 10):

                system('cls')           
                RandNumA = func_nameA(RandNumA)     #Вывод кубиков
                RandNumB = func_nameB(RandNumB)
                sleep(0.2)
                
            sumi += RandNumA + RandNumB
            print("Сумма ваших очков сотавляет: ", sumi)
            sleep(2)

            print('Теперь очередь Opponent!')
            sleep(1)
            
            for _ in range(0, 10):

                system('cls')
                RandNumA = func_nameA(RandNumA)
                RandNumB = func_nameB(RandNumB)
                sleep(0.2) 
                
            sumi_op += RandNumA + RandNumB  
            print("Сумма очков противника сотавляет: ", sumi_op)
            sleep(2)

            mround -= 1
            quan_round += 1


            if mround == 0:                 #Вывод результата
                if sumi > sumi_op:                      
                    print('Вы выиграли!')
                    money += bet + bet_op
                elif sumi_op > sumi:
                    print('Машина одолела человека, в принципе ничего нового...')
                    money_op += bet + bet_op
                elif sumi_op == sumi:
                    print('Никакого шоу... Эх, ничья')
                    money_op += bet_op
                    money += bet
                mround == 0


                if money_op == 0:
                    print('\nВы победили, у противника не осталось денег!')
                    input('Press Enter for exit')
                    exit(1)
                if money == 0:
                    print('\nВы проиграли, у вас не осталось денег!')
                    input('Press Enter for exit')
                    exit(1)

                
                accept = 'end'              #Продолжение или нет
                while accept !='yes' or accept != 'y' or accept != 'Yes' or accept != 'Y':
                    accept = input('Продолжаем? (yes/no): ')
                    if accept == 'yes' or accept == 'y' or accept == 'Yes' or accept == 'Y':
                        break
                    if accept == 'no' or accept == 'n':
                        if money_op > money:
                            print('Ваш противник победил, заработав',money_op - money_end,'$\n У вас осталось', money,'$ из', money_end,'$')
                        elif money_op < money:
                            print('Вы выиграли, заработав', money - money_end,'$\nУ противника осталось', money_op,'$ из', money_end,'$')
                        input('Press Enter for exit')
                        exit(1)
