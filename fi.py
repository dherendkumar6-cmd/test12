#atm machine clone 
balence=1000000
username=input("enter your name")
pin=int(input("enter your pin"))
if(username=="dherend" and pin==9797):
    print("press 1 for check balance")
    print("press 2 for withdrawl balance")
    print("press 3 for deposit")
    choice=int(input("select from above option"))
    if(choice==1):
        print("your balence is",balence)         
    elif(choice==2):
        amount=int(input("enter your amount to withdrawl"))
        if(amount>balence):
            print("please enter valid amount")
        else:
            balence=balence-amount
            print(f"{amount}rs witdrawl successfully")
            print(f"remainig balence {balence}")
    elif(choice==3):
        money=int(input("enter the amount to deposit"))
        if (money<0):
             print("enter valid amount")
        else:
            balence=balence+money
            print(f"{money}rs deposit successfully")
            print(f"current balence {balence}")
