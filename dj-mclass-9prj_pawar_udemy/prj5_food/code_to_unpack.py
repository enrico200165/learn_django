myapp/views

from django.shortcuts import render, redirect
from .models import Food,Consume
# Create your views here.
def index(request):
 
    if request.method =="POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()
        foods = Food.objects.all()
 
 
    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
 
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})
 
def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method =='POST':
        consumed_food.delete()
        return redirect('/')
    return render(request,'myapp/delete.html')
 
 


myapp/models

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
class Food(models.Model):
 
    def __str__(self):
        return self.name
 
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()
 
class Consume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food,on_delete=models.CASCADE)
 


myapp/admin

from django.contrib import admin
from .models import Food,Consume
# Register your models here.
admin.site.register(Food)
admin.site.register(Consume)


myapp/templates/myapp

index html

<html>
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.3/dist/Chart.min.js"></script>
    </head>
    <body>
 
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <nav class="navbar navbar-dark bg-primary">
                        <span class="navbar-brand">Calorie Tracker</span>
                    </nav>
                </div>
            </div>
 
            <br><br><br>
 
            <h4>Calorie Goal</h4>
            <br>
            <div class="row">
                <div class="col-md-9 offset-1">
                    <div class="progress">
                            <div class="progress-bar bg-success" role="progressbar" style="width: 0%" aria-valuenow="0" aria-valuemin="0" aria-valuemax="0"></div>
 
                    </div>
                </div>
            </div>
            <br><br>
            <div class="row">
                <div class="col-md-12">
                        <form method="POST">
                            <div class="form-group row">
                                {% csrf_token %}
                                <label class="col-md-2">
                                    <b>Select Food To Add </b>
                                    
                                </label>
                                <select class="col-md-6 form-control" name="food_consumed" id="food_consumed">
                                        {% for food in foods %}
                                         <option value="{‌{food.name}}">{‌{food.name}}</option>
                                        {% endfor %}
                                </select>
                                <button class="btn btn-success" type="submit">Add</button>
                            </div>
                        </form>
                </div>
            </div>
 
 
            <div class="row">
                <div class="col-md-7">
                    <div >
                        <h4> Today's Consumption</h4>
                    </div>
 
                    <table id="table" class="table table-striped table-primary">
                        <tr class="bg-primary text-white">
                            <th>Food item</th>
                            <th>Carbs(gm)</th>
                            <th>Protein(gm)</th>
                            <th>Fats(gm)</th>
                            <th>Calories(Kcal)</th>
                            <th>Remove Item</th>
                        </tr>
                                {% for c in consumed_food %}
                                <tr>
                                    <td>{‌{c.food_consumed.name}}</td>
                                    <td>{‌{c.food_consumed.carbs}}</td>
                                    <td>{‌{c.food_consumed.protein}}</td>
                                    <td>{‌{c.food_consumed.fats}}</td>
                                    <td>{‌{c.food_consumed.calories}}</td>
                                    <td><a class="btn btn-danger" href="{% url 'delete' c.id %}">X</a></td>
                                </tr>
 
                                {% endfor %}
 
                                <tr>
                                    <td id="name"><b>Total</b></td>
                                    <td id="totalCarbs"><b></b></td>
                                    <td id="totalProtien"><b></b></td>
                                    <td id="totalFats"><b></b></td>
                                    <td id="totalCalories"><b></b></td>
                                    
                                    
                                </tr>
                       
                    </table>
                </div>
 
                <div class="col-md-5 ">
                    <div class="">
                        <h4>Today's breakdown</h4>
                    </div>
                    <div class="card-header text-white bg-primary">
                        <h4>Macronutrients breakdown</h4>
                    </div>
                    <div class="col-md-12">
                        
                        <canvas id="myChart" width="400" height="400"></canvas>
 
                    </div>
                </div>
            </div>
            
        </div>
 
 
</body>
<script>
    var table = document.getElementById("table");
    var carbs=0,protein=0,fats=0,calories=0;
 
    for(var i=1;i<table.rows.length-1;i++){
        console.log(table.rows[i].cells[1].innerHTML);
        carbs +=parseFloat(table.rows[i].cells[1].innerHTML);
        carbs = Math.round(carbs);
        protein+= parseFloat(table.rows[i].cells[2].innerHTML);
        protein = Math.round(protein)
        fats+= parseFloat(table.rows[i].cells[3].innerHTML);
        fats = Math.round(fats);
        calories+= parseFloat(table.rows[i].cells[4].innerHTML);
        calories = Math.round(calories);
    }
    console.log(fats);
 
    document.getElementById("totalCarbs").innerHTML = '<b>' + carbs+'(gm)</b>';
 
    document.getElementById("totalProtien").innerHTML ='<b>' + protein+'(gm)</b>';
 
    document.getElementById("totalFats").innerHTML = '<b>' +fats+'(gm)</b>';
 
    document.getElementById("totalCalories").innerHTML = '<b>' +calories+'(Kcal)</b>';
 
    var calPer = (calories/2000) *100;
    document.getElementsByClassName("progress-bar")[0].setAttribute("style","width:"+calPer+"%");
 
 
    var total  = carbs+protein+fats;
    var carbsP = Math.round((carbs/total)*100);
    var protienP = Math.round((protein/total)*100);
    var fatsP = Math.round((fats/total)*100);
 
 
 
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Carbs '+carbsP+'%', 'Protein '+protienP+'%', 'Fats '+fatsP+'%'],
        datasets: [{
            label: '# of Votes',
            data: [carbsP, protienP, fatsP],
            backgroundColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                
            ],
            borderWidth: 1
        }]
    },
    
});
 
 
</script>
</html>


myapp/templates/myapp

delete html

<!DOCTYPE html>
<html lang="en">
<head>
 
    <title>Document</title>
</head>
<body>
    <form method="POST">
 
        {% csrf_token %}
        Are you sure you want to delete the item?
        <input type="submit">
    </form>
</body>
</html>


mysite/urls

from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('delete/<int:id>/',views.delete_consume,name="delete"),
]
 




