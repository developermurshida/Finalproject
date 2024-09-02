from django.contrib import admin
from django.urls import path


from . import views


urlpatterns = [
    path('productlist/', views.show_products,name='products'),
    
]

#
# from django.contrib import admin
# from django.urls import path

# from . import views



# urlpatterns = [
#     path('login/', views.login, name='login'),
#     path('signup/', views.signup, name='signup'),

# ]