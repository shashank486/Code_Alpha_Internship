from django.urls import path
from ecomapp import views
app_name = "ecomapp"
urlpatterns = [
    path("",views.base,name="home"),
    path("buy",views.BUY,name="buy"),
    path("product2",views.product2,name="p2"),
    path("product3",views.product3,name="p3"),
 
]
