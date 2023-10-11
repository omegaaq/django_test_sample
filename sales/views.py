from django.shortcuts import render, redirect
from .models import Client, Product, Sales, Salesman

# Create your views here.
def index(request):
    return render(request, "index.html")

def show_clients(request):
    data = Client.objects.all()
    return render(request, "clients.html", {"data": data})

def show_client(request, id):
    data = Client.objects.get(id=id)
    return render(request, "client.html", {"data": data})

def show_salesman(request):
    data = Salesman.objects.all()
    return render(request, "salesman.html", {"data": data})

def show_seller(request, id):
    data = Salesman.objects.get(id=id)
    return render(request, "seller.html", {"data": data})

def show_products(request):
    data = Product.objects.all()
    return render(request, "products.html", {"data": data})

def delete_sale(request, id):

    # if request.method == 'GET':
    #     contact = PhoneBook.objects.get(id=id)
    #     contact.delete()
    #     return redirect('phone_book/show_contacts')
    
    data = Product.objects.all()


    return render(request, "products.html", {"data": data})




def show_sales(request):
    data = Sales.objects.all()
    return render(request, "sales.html", {"data": data})

def add_client(request):
    if request.method == "POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        client = Client(name=name, surname=surname, phone=phone, email=email)
        client.save()
        return redirect("show_clients")
    return render(request, "add_client.html")

def add_sale(request):
    if request.method == "POST":
        client = Client.objects.get(id=request.POST["client"])
        seller = Salesman.objects.get(id=request.POST["seller"])
        # products = Product.objects.get(id=request.POST["products"])
        # print(f"\n\n{type(request.POST['products'])}\n\n")
        products_ids = request.POST.getlist('products')
        sale = Sales(cash_amount = request.POST["cash"],
                     sales_date = request.POST["date"],
                     client = client,
                     salesman = seller)
        sale.save()
        for id in products_ids:
            product = Product.objects.get(id=id)
            sale.product.add(product)
        return redirect("show_sales")
    context = {
        "products": Product.objects.all(),
        "clients": Client.objects.all(),
        "salesman": Salesman.objects.all(),
    }
    return render(request, "add_sale.html", context)