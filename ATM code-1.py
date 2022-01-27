list1 = {'2000': 40, '500': 20, '100': 100}
atm_total_amt,user_amt=100000,50000
password = "1234"
while(atm_total_amt>0):  
    print("***************")
    print("******ATM******")
    print("***************")
    print("1.admin")
    print("2.user")
    print("3.exit")
    a = int(input())
    def adminfun():
        global atm_total_amt
        print("1.load")
        print("2.check")
        print("3.exit")
        x = int(input())
        if x == 1:
            l = list1.get("2000") + int(input("enter number of 2000:"))
            m = list1.get("500") + int(input("enter number of 500:"))
            n = list1.get("100") + int(input("enter number of 100:"))
            list1.update({'2000': l, '500': m, '100': n})
            print("CURRENT ATM INFO")
            for key, value in list1.items():
                print(key, ":", value)
            atm_total_amt=(2000*list1.get("2000"))+(500*list1.get("500"))+100*list1.get("100")
            print("toatl amt in ATM :",atm_total_amt)
        elif (x == 2):
            for key, value in list1.items():
                print(key, ":", value)
            print("ATM bal:",atm_total_amt)
        print("1.do you want to continue \n      or \n2.exit")
        z = int(input())
        if (z == 1):
            adminfun()
        else:
            print("Thank you")  
    def userfun():
        global atm_total_amt
        global user_amt
        global password
        print("1.deposit\n2.withdrawal\n3.check\n4.change password\n5.exit")
        user_choice=int(input())
        if(user_choice==1):
            l =int(input("enter number of 2000:"))
            m =int(input("enter number of 500:"))
            n =int(input("enter number of 100:"))
            updated_amt_2000=list1.get("2000")+l
            list1.update({"2000":updated_amt_2000})
            updated_amt_500=list1.get("500")+m
            list1.update({"500":updated_amt_500})
            updated_amt_100=list1.get("100")+n
            list1.update({"100":updated_amt_100})
            add=2000*l+500*m+100*n
            user_amt+=add
            atm_total_amt+=add
            print("succesfully deposited and the current bal:",user_amt)
        elif(user_choice==2):
            amt=int(input("enter the withdrawal amount:"))
            if(amt%100==0 and amt<user_amt):
               re=0
               res1=0
               res2=0
               if(amt>=2000): 
                    re=amt//2000
                    res=amt%2000
                    print("2000 :",re)
                    updated_amt_2000=list1.get("2000")-re
                    list1.update({"2000":updated_amt_2000})
                    res1=res//500
                    res3=res%500
                    print("500 :",res1)
                    updated_amt_500=list1.get("500")-res1
                    list1.update({"500":updated_amt_500})
                    res2=res3//100
                    print("100:",res2)
                    updated_amt_100=list1.get("100")-res2
                    list1.update({"100":updated_amt_100})
                    user_amt-=amt 
                    atm_total_amt-=amt
               elif(500<=amt<2000): 
                    res1=amt//500
                    res=amt%500
                    print("500 :",res1)
                    updated_amt_500=list1.get("500")-res1
                    list1.update({"500":updated_amt_500})
                    res2=res//100
                    print("100:",res2)
                    updated_amt_100=list1.get("100")-res2
                    list1.update({"100":updated_amt_100})
                    user_amt-=amt 
                    atm_total_amt-=amt
               elif(100<=amt<500): 
                    res2=amt//100
                    print("100:",res2)
                    updated_amt_100=list1.get("100")-res2
                    list1.update({"100":updated_amt_100})
                    user_amt-=amt 
                    atm_total_amt-=amt
               else:
                    print("enter amount in 100's and 1000's")
        elif(user_choice==3):
                    print("your current bal:",user_amt)
        else:
               st=str(input("enter new pin:"))
               st1=str(input('enter new pin:'))
               if (st==st1):
                   password=st1 
                   print("Ur pin is successfully changed") 
        print("1.do you want to continue \n      or \n2.exit")
        z = int(input())
        if (z == 1):
                userfun()
        else:
                print("Thank you")    
    def admin(a):
        count = 1
        admin = "sasi"
        password = "123"
        while (count < 4):
            x = input("Enter your name:")
            y = input("Enter your password:")
            count += 1
            if x == admin and y == password:
                print("welcome", x)
                adminfun()
                break
            else:
                print("Invalid username or password")
        else:
            print("try after 24 hrs")

    def user(a):
        count = 1
        admin = "sasi"
        global password 
        while (count < 4):
            x = input("Enter your name:")
            y = input("Enter your password:")
            count += 1
            if x == admin and y == password:
                print("welcome", x)
                userfun()
                break
            else:
                print("Invalid username or password")
        else:
            print("try after 24 hrs")   
    if a == 1:
        admin(a)
    elif(a==2):
        user(a)
    else:
        print("")