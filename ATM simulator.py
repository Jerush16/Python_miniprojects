a=50000
b=1234
print('_________WELCOME TO XYZ BANK_________')
i=0
while i<3:
    c=int(input('Enter the pin:'))
    if c==b:
       print('Your card is accepted.Welcome to XYZ Bank!')
       break
    else:
       i=i+1
       print('Invalid pin.Attempts left :',3-i)
if i==3:
    print('Too many attempts.Your card is blocked')
else:
 while True:
    print('1.Check balance\n2.Deposit\n3.Withdraw\n4.Change password\n5.Exit')
    x=int(input('Enter option: '))
    if x==1:
        print('The amount available is ',a)
    elif x==2:
        z=int(input('Enter the amount to deposit : '))
        a=a+z
        print('Amount deposited successfully!')
        m=input('Need to check balance?')
        if m.strip().lower()== 'yes':
            print('The account balance is ',a)
        else:
            print('Returning to Menu')
    elif x==3:
        q=int(input('Enter the amount to withdraw :'))
        if q<=a:
           a=a-q
           print('Amount withdrawn successfully!')
        else:
           print('Insufficient cash')
        m=input('Need to check balance?')
        if m.strip().lower()== 'yes':
            print('The account balance is ',a)
        else:
            print('Returning to Menu')
    elif x==4:
        e=input('Do you want to change password: ')
        if e.strip().lower()== 'yes':
            t=input('Enter new password: ')
            r=input('Reenter your new password: ')
            if t==r:
                b=int(t)
                print('Password changed successfully!')
            else:
                print('INVALID')
        else:
            print('Returning to Menu')
    else:
        print('Action done successfully!')
        print('Thank you, visit again')
        break
 
    
        
    
