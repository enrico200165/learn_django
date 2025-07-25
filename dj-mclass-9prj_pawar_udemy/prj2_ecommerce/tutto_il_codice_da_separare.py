urls py:
from django.contrib import admin
from django.urls import path
from shop import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),
    path('checkout/',views.checkout,name='checkout'),
   
]
checkout html
<!DOCTYPE html>
<html lang="en">
<head>
    <script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
 
    <title>Document</title>
</head>
<body>
   <div class="container">
    <div class="row m-5">
      <div class="col-md-12">
        <h1>Review your order</h1>
        <hr>
      </div>
    </div>
    <div class="row m-5">
      <div class="col-md-12">
        <h4>Items in your cart</h4>
        <hr>
      </div>
    </div>
      <div class="row m-5">
        <div class="col-md-12">
           
                    <ul class="list-group" id="item_list">
                            
                    </ul>    
            </div>
        </div>   
 
        <div class="row m-5">
      <div class="col-md-12">
        <h1>Enter shipping details</h1>
        <hr>
      </div>
    </div>
        <div class="row m-5">
          <div class="col-md-12">
              <form method="POST" >
                {% csrf_token %}
                    <input type="hidden" id="items" name="items">
                  <div class="form-row">
                    <div class="form-group col-md-6">
                      <label for="inputEmail4">Name</label>
                      <input id="name" name="name" type="text" class="form-control" id="inputEmail4" placeholder="John">
                    </div>
                    <div class="form-group col-md-6">
                      <label for="inputPassword4">Email</label>
                      <input id="email" name="email" type="text" class="form-control" id="inputPassword4" placeholder="john@john.com">
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="inputAddress">Address</label>
                    <input id="address" name="address" type="text" class="form-control" id="inputAddress" placeholder="1234 Main St">
                  </div>
                  
                  <div class="form-row">
                    <div class="form-group col-md-6">
                      <label for="inputCity">City</label>
                      <input id="city" name="city" type="text" class="form-control" id="inputCity">
                    </div>
                    <div class="form-group col-md-4">
                      <label for="inputState">State</label>
                      <input id="state" name="state" type="text" class="form-control" id="inputCity">
                 
                    </div>
                    <div class="form-group col-md-2">
                      <label for="inputZip">Zip</label>
                      <input id="zipcode" name="zipcode" type="text" class="form-control" id="inputZip">
                    </div>
                    <div class="form-group col-md-2">
                      <label for="inputZip">Amount to be paid</label>
                      <input readonly="" type="text" class="form-control" id="total" name="total">
                    </div>
                  </div>
                  
                  
                  <button type="submit" class="btn btn-warning">Place Order</button>
                </form>
          
          </div>
 
        </div>
    </div>
</body>
<script type="text/javascript">
if(localStorage.getItem('cart')==null){
  var cart ={};
}
else{
  cart = JSON.parse(localStorage.getItem('cart'));
}
let total = 0;
for(item in cart){
  let name = cart[item][1];
  let quantity = cart[item][0];
  let price = cart[item][2];
  total = total + cart[item][2];
 
 
 
 
 
 
  itemString = `  <li class="list-group-item d-flex justify-content-between align-items-center">${quantity} of  ${name}     <span class="badge badge-warning badge-pill">${price}</span></li>`;
 
  $('#item_list').append(itemString);
 
 
}
totalPrice = ` <li class ="list-group-item d-flex justify-content-between align-items-center"><b>Your total</b>
  ${total}</li> `
$('#total').val(total);
$('#item_list').append(totalPrice);
$('#items').val(JSON.stringify(cart));
</script>
</html>
 
detail html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    
    <title>Document</title>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <div class="row">
                    <div class="col-md-12">
                        <img src="{‌{ product_object.image }}">
                    </div>
                </div>
            </div>
 
            <div class="col-md-6">
                <div class="row">
                    <div class="col-md-12">
                        {‌{ product_object.title }}
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12">
                        {‌{ product_object.price }}
                    </div>
                </div>
 
                <div class="row">
                    <div class="col-md-12">
                        {‌{ product_object.discount_price }}
                    </div>
                </div>
 
                <div class="row">
                    <div class="col-md-12">
                        {‌{ product_object.description }}
                    </div>
                </div>
            </div>
 
        </div>
    </div>
</body>
</html>
 
index html
{% load staticfiles %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  
<script
  src="https://code.jquery.com/jquery-3.4.1.js"
  integrity="sha256-WpOohJOqMqqyKL9FccASB9O0KwACQJpFTUBLTYOVvVU="
  crossorigin="anonymous"></script>
 
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>   
 
 
    <link rel="stylesheet" href="{% static 'shop/style.css' %}">
    <title>Document</title>
</head>
<body>
    <div class="container">
 
        <div class="row ">
            <div class="col-md-12">
                <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                    <a class="navbar-brand" href="#">ABC Shopping</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                      <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                      <ul class="navbar-nav">
                        <li class="nav-item active">
                          <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                        </li>
                        <li class="nav-item">
                          <a class="nav-link" href="#">Features</a>
                        </li>
                        <li class="nav-item">
                            <button id="cart" data-html="true" type="button" class="btn btn-secondary" data-container="body" data-toggle="popover" data-placement="bottom" data-content="Vivamus
                            sagittis lacus vel augue laoreet rutrum faucibus.">
                              Cart(0)
                            </button>
                        </li>
                        <li class="nav-item">
                          <a class="nav-link disabled" href="#">Disabled</a>
                        </li>
                      </ul>
                    </div>
                  </nav>
            </div>
        </div>
 
        <div class="row m-5">
            <div class="col-md-12">
                <form class="card card-sm">
                    <div class="card-body row no-gutters align-items-center">
                        <div class="col">
                            <input type="search" name='item_name' placeholder="Search for products" class="form-control form-control-borderless">
                        </div>
                        <div class="col-auto">
                            <button class="btn btn-success" type="submit" >Search</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
 
 
        <div class="row m-5">
            {% for product in product_objects %}
            <div class="col-md-3">
                <div class="card">
                    <img src="{‌{ product.image }}" class="card-img-top">
                    <div class="card-body">
                        <div id="nm{‌{product.id}}" class="card-title">{‌{ product.title }}</div>
                        <div id="price{‌{product.id}}" class="card-text">{‌{ product.price }}</div>
 
                        <a href="/{‌{product.id}}" class="btn btn-warning">View</a>
                        <button id="{‌{product.id}}" class="btn atc btn-warning">Add to cart</button>
                        
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
 
        <div class="row">
            <div class="col-md-3 offset-md-4">
                <ul class="pagination">
                    {% if product_objects.has_previous %}
                        <li class="page-item">
                            <a class="page-link" href="?page={‌{ product_objects.previous_page_number  }}">Previous</a>
                        </li>
                    {% endif %}
 
 
                    <li class="page-item active">
                        <a class="page-link" href="?page={‌{ product_objects.number  }}">Current</a>
                    </li>
 
                    {% if product_objects.has_next %}
                    <li class="page-item">
                        <a class="page-link" href="?page={‌{ product_objects.next_page_number  }}">Next</a>
                    </li>
                    {% endif %}
                </ul>
            </div>
        </div>
 
    </div>
</body>
<script type="text/javascript">
    console.log('This is working');
 
    if(localStorage.getItem('cart')==null){
        var cart = {};
    }
    else{
        cart = JSON.parse(localStorage.getItem('cart'));
    }
 
    $(document).on('click','.atc',function(){
        console.log("The add to cart button is clicked");
        var item_id = this.id.toString();
        console.log(item_id);
 
        if(cart[item_id]!=undefined){
            quantity = cart[item_id][0] + 1;
            cart[item_id][0] = quantity;
            cart[item_id][2] = cart[item_id][2] + parseFloat(document.getElementById("price"+item_id).innerHTML);
 
 
        }
        else{
            quantity = 1;
            price = parseFloat(document.getElementById("price"+item_id).innerHTML);
            name = document.getElementById("nm"+item_id).innerHTML;
            cart[item_id]=[quantity,name,price];
 
            
        }
        console.log(cart);
        localStorage.setItem('cart',JSON.stringify(cart));
        document.getElementById("cart").innerHTML = "Cart("+ Object.keys(cart).length +")";
       
    });
 
    DisplayCart(cart);
    function DisplayCart(cart){
        var cartString ="";
        cartString += "<h5>This is your cart</h5>";
        var cartIndex = 1;
        for(var x in cart){
            cartString += cartIndex;
            cartString += document.getElementById("nm"+x).innerHTML + "Qty:" + cart[x][0] + "</br>";
            cartIndex+=1;
        }
 
        cartString += "<a href='/checkout'><button class='btn btn-warning' id='checkout'>Checkout</button></a>";
        document.getElementById("cart").setAttribute('data-content',cartString);
        $('[data-toggle="popover"]').popover();
    }
 
 
</script>
</html>
 
 
 
 
models py:
from django.db import models
 
# Create your models here.
class Products(models.Model):
 
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)
 
 
class Order(models.Model):
 
    
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email =models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
 
 
    views py:
from django.shortcuts import render
from .models import Products,Order
from django.core.paginator import Paginator
# Create your views here.
 
def index(request):
    product_objects = Products.objects.all()
 
    #search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)
 
    #paginator code
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    
    return render(request,'shop/index.html',{'product_objects':product_objects})
 
 
def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})
    
def checkout(request):
 
    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state =request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()
 
    return render(request,'shop/checkout.html')