from django.urls import path
from . import views

# this is a mapping at app level, 
# NB it is internal and must be registered with the mapping at project level
# in the urls.py of the project
urlpatterns = [
    # path('mySubURL', myView)
    path('function', views.hello_world),
    path('class',    views.HelloEthiopia.as_view()),
    path('reservation', views.home),
]