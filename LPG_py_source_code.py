

def login():
    Name=input("Enter valide user name:")
    Password=input("Enter valide password:")
    if Name in data.keys()and Password==data[Name]['my_profile']['Password']:
        print(":)Welcome",Name.upper())
        print("<============LOGIN SUCCESSFULL============>")
        option(Name)
       
    else:
        print("incorrect user name or password")
        print("<******RELOGIN******>")

        
        a=int(input('''Press >>>1 for-Relogin
Press >>>2 for -register again
Press >>>3 for -forgot password: '''))
        if a==1:
            login()
        elif a==2:
            register()
        elif a==3:
              forgot(Name)    
        else:
            print("please clik availbale option  ")
           


data={}
def register():
     Name=input("Enter user name:")
     if Name in data.keys():
          print("alredy user name is registered")
          a=input(''' if you wanto login press 1 or press any key for exit:''')
          if a==1:
              login()
          else:
             exit()
             
     else:
          Email=input("Enter user Email Id:")
          Password=input("Enter Password:")
          Phone_number=int(input("Enter user Mobile_Numer:"))
          data[Name]={}
          data[Name]['my_profile']={}
          data[Name]['my_profile']['Name'],data[Name]['my_profile']['Email'],data[Name]['my_profile']['Password'],data[Name]['my_profile']['Phone_number']=Name,Email,Password,Phone_number
          data[Name]['Orders']={}
          print("your register is done")
          for i in range(1,4):
              a=int(input('''Press >>>1 for-login
Press >>>2 for -register again: '''))
              if a==1:
                  login()
                  break
              elif a==2:
                  register()
                  break
          
              else:
                  print("please click 1 or 2")
                  
          
          



def forgot(Name):
     if Name in data.keys():
         Password=input("Enter Password:")
         if Password!=data[Name]['my_profile']['Password']:
             print("Password does't match")
             Password=input("Enter new-Password:")
             data[Name]['my_profile']['Password']=Password
             print("password has changed")
             option(Name)
         else:
             print("yor password is match")
             login()
     else:
         login()
             
             
             
def main(Name):
    global brand
    
    brand=int(input("""1-for HP Gas 
2-for Indane Gas
3-for Bharat Gas : """))
    if brand==1:
       
        brand='HP Gas'
        
    elif  brand==2:
        
        brand='Indane Gas'
        
    elif  brand==3:
        
        brand='Bharat Gas'
        
        
    else:
        print("pless enter given option")


def refill(Name):
    global year
    main(Name)
    year=int(input("year:"))
    month=int(input("""1-jan
2-feb    5-may   8-aug  11-nov
3- mar   6-june 9-sep   12-dec
4-apr    7-jul  10-oct  :     """))
    months= {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',
          10:'Oct',11:'Nov',12:'Dec'}
    if brand in data[Name]['Orders'].keys():
       
        if year in data[Name]['Orders'][brand].keys():
            if months[month] in data[Name]['Orders'][brand][year].keys():
               print('already you have ordered this month')
            else:
                
                data[Name]['Orders'][brand][year][months[month]]={}
                if month<=5:
                    amount=940
                    print(f'hello {Name.capitalize()} your booking amount is {amount}')
                    data[Name]['Orders'][brand][year][months[month]]['amount']=amount
                    
                else:
                    amount=990
                    print(f'hello {Name.capitalize()} your booking amount is {amount}')
                    data[Name]['Orders'][brand][year][months[month]]['amount']=amount
                    
               
        else:
            
            data[Name]['Orders'][brand][year]={}
            data[Name]['Orders'][brand][year][months[month]]={}
            if month<=5:
                amount=940
                print(f'hello {Name.capitalize()} your booking amount is {amount}')
                data[Name]['Orders'][brand][year][months[month]]['amount']=amount
                option(Name)
            else:
                amount=990
                print(f'hello {Name.capitalize()} your booking amount is {amount}')
                data[Name]['Orders'][brand][year][months[month]]['amount']=amount
                option(Name)
    else:
        data[Name]['Orders'][brand]={}
        if year in data[Name]['Orders'][brand].keys():
            if months[month] in data[Name]['Orders'][brand][year].keys():
                print('already you have ordered this month')
                if month<=5:
                    amount=940
                    print(f'hello {Name.capitalize()} your booking amount is {amount}')
                    data[Name]['Orders'][brand][year][months[month]]['amount']=amount
                    
                        
                else:
                    amount=990
                    print(f'hello {Name.capitalize()} your booking amount is {amount}')
                    data[Name]['Orders'][brand][year][months[month]]['amount']=amount
                   
            else:
                data[Name]['Orders'][brand][year][months[month]]={}
                if month<=5:
                    amount=940
                    print(f'hello {Name.capitalize()} your booking amount is {amount}')
                    data[Name]['Orders'][brand][year][months[month]]['amount']=amount
                    
                else:
                    amount=990
                    print(f'hello {Name.capitalize()} your booking amount is {amount}')
                    data[Name]['Orders'][brand][year][months[month]]['amount']=amount
                   
        else:
            data[Name]['Orders'][brand][year]={}
            data[Name]['Orders'][brand][year][months[month]]={}
            if month<=5:
                amount=940
                print(f'hello {Name.capitalize()} your booking amount is {amount}')
                data[Name]['Orders'][brand][year][months[month]]['amount']=amount
                
                   
            else:
                amount=990
                print(f'hello {Name.capitalize()} your booking amount is {amount}')
                data[Name]['Orders'][brand][year][months[month]]['amount']=amount
                

        
def option(Name):
    for i in range(1,4):
        print("______________________________")
        a=int(input('''Press >>>1 for-refill
Press >>>2 for -show order history
Press >>>3 for -view profile
Press >>>4 for -logout: '''))
        if a==1:
            refill(Name)
        elif a==2:
            hist(Name)
        elif a==3:
            d1=data[Name]['my_profile']
            for i,j in d1.items():
                print(f'{i}:{j} ')
            a = int(input('''
select option:
Press >>>1 for -change Name
Press >>>2 for -change Email
Press >>>3 for -change Number
'''))
            if a==1:
                newname = input('enter new name:')
                data[newname]=data[Name]
                data[Name]['my_profile']['Name']=newname
                del data[Name]
                print('name changed successfully')
                    
            elif a==2:
                newemail = input('enter new email:')
                data[Name]['my_profile']['Eamil']=newemail
                print('email changed successfully')
            
                    
            elif a==3:
                newmobile = str(int(input('enter new mobile number:')))
                data[Name]['my_profile']['mobile']=newmobile
                print('mobile changed successfully')
            else:
                print("incorrect user name or password")
                
        elif a==4: 
             Name=input("Enter valide user name:")
             Password=input("Enter valide password:")
             if Name in data.keys()and Password==data[Name]['my_profile']['Password']:
                 print("Thank you for coming")
                 break
             else:
                 print("incorrect user name or password")
                 print("<******RELOG0UT******>")

            

        else:
            print('select given option')

       
def hist(Name):
    print("-------------------------------------------------")
    a=int(input('''Press >>>1 for overall history
Press >>>2 for orders
Press >>>3 for Brands
Press >>>4 for year
Press >>>5 for months: '''))
    if a==1:
        d1=data[Name]
        print(d1)
                  
    elif a==2:
        d2=data[Name]['Orders']
        print(d2)
                  
    elif a==3:
        b = list(data[Name]['Orders'].keys())
        
        c = {i:j for i,j in zip(range(1,len(b)+1),b)}
        print('select any available option:')
        for i,j in c.items():
            print(i,'-',j)
        d = int(input())
        print(data[Name]['Orders'][c[d]])
                  
    elif a==4:
        b = list(data[Name]['Orders'].keys())
        
        c = {i:j for i,j in zip(range(1,len(b)+1),b)}
        print('select any available option:')
        for i,j in c.items():
            print(i,'-',j)
        d = int(input())
        b = list(data[Name]['Orders'][brand].keys())
       
        c = {i:j for i,j in zip(range(1,len(b)+1),b)}
        print('select any available option:')
        for i,j in c.items():
            print(i,'-',j)
        d = int(input())
        print(data[Name]['Orders'][brand][c[d]])
        
        
           
    elif a==5:
        b = list(data[Name]['Orders'].keys())
        c = {i:j for i,j in zip(range(1,len(b)+1),b)}
        print('select any available option:')
        for i,j in c.items():
            print(i,'-',j)
        d = int(input())
        b = list(data[Name]['Orders'][brand].keys())
        c = {i:j for i,j in zip(range(1,len(b)+1),b)}
        print('select any available option:')
        for i,j in c.items():
            print(i,'-',j)
        d = int(input())
        m=list(data[Name]['Orders'][brand][year].keys())
        a = {i:j for i,j in zip(range(1,len(m)+1),m)}
        print('select any available option:')
        for i,j in a.items():
            print(i,'-',j)
        d = int(input())
        print(data[Name]['Orders'][brand][year][a[d]])
        pass
            
         
        

    else:
        print("please select any available option:")
        hist(Name)

    


   

        

    
            
        
        
        
    
         
    


