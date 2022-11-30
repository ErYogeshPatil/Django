from django.urls import path
from ShopApp import views

urlpatterns = [
    path("home",views.home),
    # path('logout',views.logout),
    # path("Register",views.register),
    path("Dashboard",views.dashboard),
    path("Viewcart",views.viewcart),
    path("addtocart/<rid>",views.addtocart),
    path("removefromcart/<rid>",views.RemoveFromCart),
    path("confirm_order",views.confirm_order),
    path('filter/<Type>',views.filter),
    path('all',views.all),
    path('sort/<sv>',views.sort),
    path('PriceSort/<p>',views.PriceSort),
    path('PriceRange',views.PriceRange),
    path('SearchByName',views.SearchByName),
    path('Total',views.Total),

    #----User Login ----------
    path("Login",views.login),
    path('User_Register',views.User_Register),
    path('logout',views.logout),
    
    # --- Employee ----
    path("emplogin",views.emplogin),
    path("ERegister",views.ERegister),
    path("empdashboard",views.empdashboard),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    # path('setcookie',views.setcookie),
    # path('getcookie',views.getcookie),
    # path('setsession',views.setsession),
    # path('getsession',views.getsession),
    # path('prange',views.prange),
    # path('formapi',views.empform),
    # path('modelform',views.productform),


]