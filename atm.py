class Atm:
    try:
        def check_balance(self):
            global available_balance
            print(f'your available balance is: {available_balance} Naira')
        def deposite(self):
            global available_balance
            deposited_money = int(input('Enter amount of money to deposite: '))
            print(f'your deposited money is: {deposited_money}')
            i =  int(input(f'are you sure you want to deposite {deposited_money} in this account ?: \n1: yes \n2: no \n'))

            if i == 1:
                if deposited_money <= 500000:
                    available_balance += deposited_money
                    print('deposited successfully')
                    print(f'available Balance: {available_balance}')
            
                else:
                    print(f'you cant transfer more than 500000N')
            
            elif i == 2:
                print(f'process for deposite money cancelled')
            else:
                print('wrong input')

        def withdraw(self):
            global available_balance
            withdraw_money = int(input('Enter Amount To Withdraw : '))
        
            if withdraw_money <= available_balance:
                available_balance -= withdraw_money
                print('retrieve your cash, withdrawal successful')
            else: 
                print('insufficient amount in Your Account')
    except ValueError:
        print('wrong input')
    except TypeError:
        print('wrong input')
    except SyntaxError:
        print('wrong input')
    except InterruptedError:
        print('wrong input')
            

available_balance = 1
Bank = Atm()
while True:
    print('Welcome To United Bank Of Africa')
    
    i  = int(input(' 1: CHECK BALANCE \n 2: DEPOSITE MONEY \n 3: WITHDRAWAL \n 4: EXIT \n\n'))
    try:
        if i == 1:
            Bank.check_balance()
        elif i == 2:
            Bank.deposite()
        elif i == 3:
            Bank.withdraw()
        elif i == 4:
            break
        elif str():
            print('wrong input you must 1, 2, 3 or 4')
    except ValueError:
        print('wrong input ')
    except TypeError:
        print('wrong input ')
    except SyntaxError:
        print('wrong input ')
    except InterruptedError:
        print('wrong input')
    except SystemError:
        print('system error')
    except BaseException:
        print('wrong base')



