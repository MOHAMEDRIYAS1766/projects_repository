from django.shortcuts import render,redirect
import mysql.connector as sql
# Create your views here.
def index(request):
    return render(request,"index.html")


def feedback(request):
    global name,mobile,trainer,feed_back
    if request.method=='POST':
        conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
        cursor = conn.cursor()
        csrf=request.POST
        print(csrf.items())
        for key,value in csrf.items():
            if key=='name':
                name=value
            if key=='mobile':
                mobile=value
            if key=='trainer':
                trainer=value
            if key=='feed_back':
                feed_back=value
        query="insert into feedback(name,mobile,trainer,feed_back) values ('{}','{}','{}','{}')".format(name,mobile,trainer,feed_back)
        cursor.execute(query)
        conn.commit()
        return redirect("/")
    
    return render(request,"feedback.html")


def team(request):
    
    return render(request,"team.html")
def about(request):
    
    return render(request,"about.html")
def clas(request):
    
    return render(request,"class.html")
def contact(request):
    
    return render(request,"contact.html")
def testimonial(request):
    
    return render(request,"testimonial.html")

def register(request):
    global name,mobile_number,email,password,conform_password
    if request.method=='POST':
        conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
        cursor = conn.cursor()
        csrf=request.POST
        print(csrf.items())
        for key,value in csrf.items():
            if key=='name':
                name=value
            if key=='mobile_number':
                mobile_number=value
            if key=='email':
                email=value
            if key=='password':
                password=value
            if key=='conform_password':
                conform_password=value
        query="insert into customer(name,mobile_number,email,password,conform_password) values ('{}','{}','{}','{}','{}')".format(name,mobile_number,email,password,conform_password)
        cursor.execute(query)
        conn.commit()
        return redirect("/")
    return render(request,"register.html")

def login(request):
    global email,conform_password
    csrf=request.POST
    try:
        if request.session["users"]:
            return redirect("/edit/"+str(request.session["users"]))
    except:
        pass
    try:
        if request.session["admin"]:
            return redirect("/edit/"+str(request.session["admin"]))
    except:
        pass
            
    if request.method=='POST':
        conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
        cursor = conn.cursor(dictionary=True)
        
        print(csrf.items())
        for key,value in csrf.items():
            if key =='email':
                email = value
            if key =='conform_password':
                conform_password = value
                
        query="select * from customer where email ='{}' And conform_password='{}' ".format(email,conform_password)
        cursor.execute(query)
        result=cursor.fetchone()
        conn.commit()
        if result == None:
            return render(request,"login.html",{"error":"login Failed!"})
            
        if email =="riyas88@gmail.com":
            if conform_password == "riyas23":
                
                try:
                    del request.session["users"]
                except:
                    pass
                request.session["admin"] = result['id']
                return redirect('/view')
        
        try:
            del request.session["admin"]
        except:
            pass
        request.session["users"]=result['id']
       
        
    return render(request,"login.html")
###########
def view(request):
    try:
        if request.session['admin']:
            conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
            cursor = conn.cursor(dictionary=True)
            query="select*from customer"
            cursor.execute(query)
            result=cursor.fetchall()
            print(result)
            conn.commit()
            return render(request,"view.html",{"customer":result})
    except:
       return redirect('/')
    
def edit(request,id):
    if request.session.get("admin") or request.session["users"]:
        pass
    else:
        return redirect("/view")
  
    global name,mobile_number,email,password,conform_password
    csrf=request.POST 
    conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
    cursor = conn.cursor(dictionary=True)
    query="select*from customer where id = {}".format(id)
    cursor.execute(query)
    result=cursor.fetchone()
    print(result,id)
    conn.commit()
    return render(request,"edit.html",{"std":result})

def update(request,id):
    if request.method=='POST':
        conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
        cursor = conn.cursor()
        csrf=request.POST
        print(csrf.items())
        for key,value in csrf.items():
            if key=='name':
                name=value
            if key=='mobile_number':
                mobile_number=value
            if key=='email':
                email=value
            if key=='password':
                password=value
            if key=='conform_password':
                conform_password=value
        query="update customer set name = '{}',mobile_number = '{}',email = '{}',password= '{}',conform_password = '{}' where id ='{}'".format(name,mobile_number,email,password,conform_password,id)
        cursor.execute(query)
        conn.commit()
        del request.session['admin']
        return redirect("/")
    return redirect("/")
   
def delet(request,id):
    conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
    cursor = conn.cursor()
    query="delete from customer where id = '{}'".format(id)
    cursor.execute(query)
    conn.commit()
    return redirect("/view")
######################
def logout(request):
    if request.session['users']:
        del request.session['users']
    return redirect("/")
    
def adminlogout(request):
    if request.session['admin']:
        del request.session['admin']
    return redirect("/")
    


def employees(request):
    
    try:
        if request.session['admin']:
            conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
            cursor = conn.cursor(dictionary=True)
            query="select*from employees"
            cursor.execute(query)
            result=cursor.fetchall()
            print(result)
            conn.commit()
            return render(request,"employees.html",{"employees":result})
    except:
        pass
    return redirect('/employees')

def addnewemployee(request):
    global emp_id,name,number,email,salary
    if request.session['admin']:
        if request.method=='POST':
            conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
            cursor = conn.cursor()
            csrf=request.POST
            print(csrf.items())
            for key,value in csrf.items():
                if key=='emp_id':
                    emp_id=value
                if key=='name':
                    name=value
                if key=='number':
                    number=value
                if key=='email':
                    email=value
                if key=='salary':
                    salary=value
                
            query="insert into employees(emp_id,name,number,email,salary) values ('{}','{}','{}','{}','{}')".format(emp_id,name,number,email,salary)
            cursor.execute(query)
            conn.commit()
            return redirect("/employees")
        return render(request,"addnewemployee.html")
    return redirect('/')
  
def empedit(request,id):
    if request.session.get("admin"):
        pass
    else:
        return redirect("/view")
  
    global emp_id,name,number,email,salary
    csrf=request.POST 
    conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
    cursor = conn.cursor(dictionary=True)
    query="select*from employees where id = {}".format(id)
    cursor.execute(query)
    result=cursor.fetchone()
  
    conn.commit()
    return render(request,"empedit.html",{"emp":result})

def empdelet(request,id):
    conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
    cursor = conn.cursor()
    query="delete from employees where id = '{}'".format(id)
    cursor.execute(query)
    conn.commit()
    return redirect("/employees")
def empupdate(request,id):
    if request.method=='POST':
        conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
        cursor = conn.cursor()
        csrf=request.POST
        for key,value in csrf.items():
            if key=='emp_id':
                emp_id=value
            if key=='name':
                name=value
            if key=='number':
                number=value
            if key=='email':
                email=value
            if key=='salary':
                salary=value
        query="update employees set emp_id ='{}',name = '{}',number = '{}',email = '{}',salary= '{}' where id ='{}'".format(emp_id,name,number,email,salary,id)
        cursor.execute(query)
        conn.commit()
        return redirect("/employees")
    return redirect("/")


def feedbackpage(request):
    
    try:
        if request.session['admin']:
            conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
            cursor = conn.cursor(dictionary=True)
            query="select*from feedback"
            cursor.execute(query)
            result=cursor.fetchall()
            print(result)
            conn.commit()
            return render(request,"feedbackpage.html",{"FeedBack":result})
    except:
        pass
    return redirect('/feedbackpage')


def feedbackdelet(request,id):
    conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
    cursor = conn.cursor()
    query="delete from feedback where id = '{}'".format(id)
    cursor.execute(query)
    conn.commit()
    return redirect("/feedbackpage")


###########
def empaccount(request):
    global emp_id,name,month,salary,credit
    if request.session['admin']:
        if request.method=='POST':
            conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
            cursor = conn.cursor()
            csrf=request.POST
            print(csrf.items())
            for key,value in csrf.items():
                if key=='emp_id':
                    emp_id=value
                if key=='name':
                    name=value
                if key=='month':
                    month=value
                if key=='salary':
                    salary=value
                if key=='credit':
                    credit=value
                
            query="insert into empaccounts(emp_id,name,month,salary,credit) values ('{}','{}','{}','{}','{}')".format(emp_id,name,month,salary,credit)
            cursor.execute(query)
            conn.commit()
            return redirect("/accounts")
        return render(request,"empaccount.html")
    return redirect('/')



def accounts(request):
    
    try:
        if request.session['admin']:
            conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
            cursor = conn.cursor(dictionary=True)
            query="select*from empaccounts"
            cursor.execute(query)
            result=cursor.fetchall()
            print(result)
            conn.commit()
            return render(request,"accounts.html",{"emp":result})
    except:
        pass
    return redirect('/accounts')


def customeraccount(request):
    global name,mobile_number,email,month,fees,paid
    if request.session['admin']:
        if request.method=='POST':
            conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
            cursor = conn.cursor()
            csrf=request.POST
            print(csrf.items())
            for key,value in csrf.items():
                if key=='name':
                    name=value
                if key=='mobile_number':
                    mobile_number=value
                if key=='email':
                    email=value
                if key=='month':
                    month=value
                if key=='fees':
                    fees=value
                if key=='paid':
                    paid=value
                
            query="insert into customeraccounts(name,mobile_number,email,month,fees,paid) values ('{}','{}','{}','{}','{}','{}')".format(name,mobile_number,email,month,fees,paid)
            cursor.execute(query)
            conn.commit()
            return redirect("/useraccount")
        return render(request,"customeraccount.html")
    return redirect('/')


def useraccount(request):
    
    try:
        if request.session['admin']:
            conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
            cursor = conn.cursor(dictionary=True)
            query="select*from customeraccounts"
            cursor.execute(query)
            result=cursor.fetchall()
            print(result)
            conn.commit()
            return render(request,"useraccount.html",{"user":result})
    except:
        pass
    return redirect('/accounts')

def editempaccount(request,id):
    if request.session.get("admin"):
        pass
    else:
        return redirect("/view")
  
    global emp_id,name,month,salary,credit
    csrf=request.POST 
    conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
    cursor = conn.cursor(dictionary=True)
    query="select*from empaccounts where id = {}".format(id)
    cursor.execute(query)
    result=cursor.fetchone()
  
    conn.commit()
    return render(request,"editempaccount.html",{"emp":result})

def empaccountupdate(request,id):
    global emp_id,name,month,salary,credit
    if request.session['admin']:
        if request.method=='POST':
            conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
            cursor = conn.cursor()
            csrf=request.POST
            print(csrf.items())
            for key,value in csrf.items():
                if key=='emp_id':
                    emp_id=value
                if key=='name':
                    name=value
                if key=='month':
                    month=value
                if key=='salary':
                    salary=value
                if key=='credit':
                    credit=value
        query="update empaccounts set emp_id ='{}',name = '{}',month = '{}',salary = '{}',credit= '{}' where id ='{}'".format(emp_id,name,month,salary,credit,id)
        cursor.execute(query)
        conn.commit()
        return redirect("/accounts")
    return redirect("/")


def deletempaccount(request,id):
    conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
    cursor = conn.cursor()
    query="delete from empaccounts where id = '{}'".format(id)
    cursor.execute(query)
    conn.commit()
    return redirect("/accounts")

def editcustomeraccount(request,id):
    if request.session.get("admin"):
        pass
    else:
        return redirect("/view")
  
    global name,mobile_number,email,month,fees,paid
    csrf=request.POST 
    conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
    cursor = conn.cursor(dictionary=True)
    query="select*from customeraccounts where id = {}".format(id)
    cursor.execute(query)
    result=cursor.fetchone()
  
    conn.commit()
    return render(request,"editcustomeraccount.html",{"client":result})


def customeraccountupdate(request,id):
    global name,mobile_number,email,month,fees,paid
    if request.session['admin']:
        if request.method=='POST':
            conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
            cursor = conn.cursor()
            csrf=request.POST
            print(csrf.items())
            for key,value in csrf.items():
                if key=='name':
                    name=value
                if key=='mobile_number':
                    mobile_number=value
                if key=='email':
                    email=value
                if key=='month':
                    month=value
                if key=='fees':
                    fees=value
                if key=='paid':
                    paid=value
        query="update customeraccounts set name ='{}',mobile_number = '{}',email = '{}',month = '{}',fees= '{}',paid='{}' where id ='{}'".format(name,mobile_number,email,month,fees,paid,id)
        cursor.execute(query)
        conn.commit()
        return redirect("/useraccount")
    return redirect("/")


def deletecustomeraccount(request,id):
    conn = sql.connect(host="localhost",user="root",password="",database="gym_pro")
    cursor = conn.cursor()
    query="delete from customeraccounts where id = '{}'".format(id)
    cursor.execute(query)
    conn.commit()
    return redirect("/useraccount")




    






    
