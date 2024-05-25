from django.shortcuts import render,HttpResponse

# Create your views here.
def base(request):
    return render( request,"base.html")
def BUY(request):
    return render(request,"product1.html")
def product2(request):
    return render(request,"product2.html")
def product3(request):
    return render(request,"product3.html")


# def cart(request):
#     return render( request,"cart.html")
# def index(request):
#     return render( request,"index.html")
 
