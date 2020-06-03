class Atm:
    def _init(self):
        pass
    def check_balance(self):
        global avl_bal
        print(f'your available balance is: {avl_bal} Naira')
    def deposite(self):
        global avl_bal
        dep_money = int(input('Enter amount of money tO deposite: '))
        print(f'your deposited money is: {dep_money}')
        i =  str(input(f'are you sure you want to deposite {dep_money} in this account ?: \n1: yes \n2: no \n'))

        if i == 1:
            if dep_money <= 500000:
                avl_bal += dep_money
                print('deposited successfully')
                print(f'available Balance: {avl_bal}')
           
            else:
                print(f'ypu cant transfer more than 500000N')
        
        elif i == 2:
            print(f'process for deposite money cancelled')
        else:
            print('wrong input')

    def withdraw(self):
        global avl_bal
        withdraw_money = int(input('Enter Amount To Withdraw : '))
        
        try:
            if withdraw_money <= avl_bal:
                # hello = int()
                if int():
                    avl_bal -= withdraw_money
                    print('retrieve your cash, withdrawal successful')
                    print(f'your Available Balance is {avl_bal}')
                else:
                    print('wrong input')
            else: 
                print('insufficient amount in Your Account')
                print(f'your main balance is {avl_bal}')
        except ValueError:
            print('wrong input')
        except TypeError:
            print('wrong input')
        except SyntaxError:
            print('wrong input')
        

avl_bal = 1
bank = Atm()
while True:
    print('Welcome To United Bank Of Africa')
    
    i  = int(input(' 1: CHECK BALANCE \n 2: DEPOSITE MONEY \n 3: WITHDRAW \n 4: EXIT \n\n'))
    
    if i == 1:
        bank.check_balance()
    elif i == 2:
        bank.deposite()
    elif i == 3:
        bank.withdraw()
    elif i == 4:
        break
    else:
        print('wrong input you must 1, 2, 3 or 4 ')