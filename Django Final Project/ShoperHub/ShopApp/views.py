from django.db.models import Q
from django.db.models import Sum,Avg
from django.shortcuts import render,redirect
from django.http import HttpResponse

from ShopApp.models import Product,Emp_Details,User_Details




# Login and register details of users...

def login(request):

    if request.method=="POST":
        name=request.POST['Uname']
        password=request.POST['Upass']
        q1=Q(User_Name=name)
        q2=Q(U_Password=password)
        if(User_Details.objects.filter(q1&q2)):
            return redirect('/Dashboard')
        else:
            return render(request,"login.html")
        # return render(request,"dashboard.html")
    else:
        return render(request,"login.html")
        


def logout(request):
      # this function destroy login session from database  (import) 
    return redirect('/home')

def User_Register(request):

    if request.method=="POST":
        name=request.POST['Uname']
        mail=request.POST['Umail']
        password=request.POST['Upass']
        p1=User_Details(User_Name=name,U_Email=mail,U_Password=password,)
        print(p1)
        p1.save()
        return render(request,"home.html")
    else :
        return render(request,"register.html")

#-----------------------------------------------------------------------------
# product Details -----------------------------------------------------------

def home(request):
    return render(request,"home.html")

def dashboard(request):
        # display all data on Dashboard
        q1=Q(is_Cart="N")      
        q2=Q(is_deleted="N")
        rec=Product.objects.filter(q1 & q2 ) 
        content={}
        content['data']=rec
        return render(request,"dashboard.html",content)
        # return render(request,"home.html")

def addtocart(request,rid):
    x=Product.objects.filter(id=rid)
    x.update(is_Cart="Y")
    return redirect('/Dashboard')
    # return render(request,"home.html")

def RemoveFromCart(request,rid):
    z=Product.objects.filter(id=rid)
    z.update(is_Cart="N")
    return redirect('/Viewcart')
    # return render(request,"home.html")

def viewcart(request):
    q1=Q(is_Cart="Y")      
    q2=Q(is_deleted="N")
    rec=Product.objects.filter(q1 & q2 ) 
    content={}
    content['data']=rec
    return render(request,"Viewcart.html",content)
    # return render(request,"home.html")

def sort(request,sv):
    if(sv=='AS'):
        # q1=Q(order_by="Name")
        q2=Q(is_deleted="N")
        q3=Q(is_Cart="N")
        pqr=Product.objects.filter(q3&q2).order_by("Name")
    elif(sv=='DE'):
        # q1=Q(order_by="-Name")
        q2=Q(is_deleted="N")
        q3=Q(is_Cart="N")
        pqr=Product.objects.filter(q3&q2).order_by("-Name")
    
    content={}
    content['data']=pqr
    return render(request,"dashboard.html",content)


def PriceRange(request):
    if request.method=="POST":
        min=request.POST["from"]
        max=request.POST["to"]
        q1=Q(Discount_Price__gte=min)
        q2=Q(Discount_Price__lte=max)
        q3=Q(is_deleted="N")
        q4=Q(is_Cart="N")
        xyz=Product.objects.filter(q1&q2&q3&q4)
        content={}
        content['data']=xyz
        return render(request,'dashboard.html',content)


def SearchByName(request):
    if request.method=="POST":
        prod=request.POST["SearchByName"]
        A1=Q(Name=prod)
        A2=Q(is_deleted="N")
        A3=Q(is_Cart="N")
        AA=Product.objects.filter(A1&A2&A3)
        content={}
        content['data']=AA
        return render(request,'dashboard.html',content)


def PriceSort(request,p):
    if(p=='HI'):
        q2=Q(is_deleted="N")
        q3=Q(is_Cart="N")
        ps=Product.objects.filter(q3&q2).order_by("-Discount_Price")
    elif(p=='LW'):
        q2=Q(is_deleted="N")
        q3=Q(is_Cart="N")
        ps=Product.objects.filter(q3&q2).order_by("Discount_Price")

    content={}
    content['data']=ps
    return render(request,"dashboard.html",content)

def confirm_order(request):
        c=Product.objects.all()
        c.update(is_Cart="N")
        return render(request,"confirm_order.html")
        # return render(request,"home.html")

def filter(request,Type):
    if Type=='Mob':
        f='M'
    elif Type=='Fas':
        f='F'
    elif Type=='kit':
        f='k'
    q1=Q(Type=f)
    q2=Q(is_deleted="N")
    q3=Q(is_Cart="N")
    t=Product.objects.filter(q1&q2&q3)
    content={}
    content['data']=t
    return render(request,'dashboard.html',content)
    # return render(request,"home.html")

def all(request):
    q1=Q(is_Cart="N")      
    q2=Q(is_deleted="N")
    all=Product.objects.filter(q1 & q2 ) 
    content={}
    content['data']=all
    return render(request,"dashboard.html",content)
    # return render(request,"home.html")

def Total(request):
    q1=Q(is_Cart="N")      
    q2=Q(is_deleted="N")
    # Total1=Product.objects.filter(q1 & q2).count()
    # Total1=Product.objects.filter(q1 & q2).annotate(sum('Discount_Price'))
    Total1=Product.objects.filter(q1 & q2).aggregate(sum('Discount_Price'))
    print(Total1)
    # content={}}
    # content['data']=Total1
    return render(request,"dashboard.html",{'Total':Total1})




    # Create your views here.  employee Product------------------

def empdashboard(request):
    if request.method=="POST":
        name=request.POST['pname']
        desc=request.POST['pdesc']
        D_price=request.POST['dprice']
        A_price=request.POST['aprice']
        Type=request.POST['ptype']
        Offer=request.POST['poffer']
        Image=request.POST['pimage']

        # Link with data base database name= variable name and save data
        p1=Product(Name=name,P_desc=desc,Discount_Price=D_price,Actual_Price=A_price,Type=Type,Offer=Offer,Image=Image,is_deleted="N",is_Cart="N")
        p1.save()

        # return render(request,"emp_dashboard.html")
        return redirect('/empdashboard')
    else :
        rec=Product.objects.all() 
        content={}
        content['data']=rec
        return render (request,'emp_dashboard.html',content)
    # return render(request,"home.html")


def emplogin(request):

    if request.method=="POST":
        print("at post section")
        Ename=request.POST['Ename']
        Epassword=request.POST['Epass']
        q1=Q(E_Name=Ename)
        q2=Q(E_Password=Epassword)
        if(Emp_Details.objects.filter(q1&q2)):
            return redirect('/empdashboard')
            # return render(request,"emp_dashboard.html")
        else:
            print("not match")
            return render(request,"home.html")
        # return render(request,"dashboard.html")
    else:
        print("else part -----------------ss")
        return render(request,"emplogin.html")

def ERegister(request):

    if request.method=="POST":
        name=request.POST['Ename']
        Role=request.POST['ERole']
        password=request.POST['Epass']
        p1=Emp_Details(E_Name=name,E_Role=Role,E_Password=password,)
        print(p1)
        p1.save()
        return redirect("/emplogin")
    else :
        return render(request,"Eregister.html")


def edit(request,rid):

    if request.method=="POST":
        name=request.POST['pname']
        desc=request.POST['pdesc']
        D_price=request.POST['dprice']
        A_price=request.POST['aprice']
        Type=request.POST['ptype']
        Offer=request.POST['poffer']
        Image=request.POST['pimage']

        x=Product.objects.filter(id=rid)
        x.update(Name=name,P_desc=desc,Discount_Price=D_price,Actual_Price=A_price,Type=Type,Offer=Offer,Image=Image)
        return redirect('/empdashboard')
    else:
        rec=Product.objects.get(id=rid)
        content={}
        content['data']=rec
        return render (request,'edit_emp.html',content)

def delete(request,rid):
    x=Product.objects.filter(id=rid)
    x.update(is_deleted="Y")
    return redirect('/empdashboard')