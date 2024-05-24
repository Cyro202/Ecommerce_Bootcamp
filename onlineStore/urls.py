from django.urls import path
from .import views
from .views import register_user
# Create your tests here.

urlpatterns = [
    path('',views.index, name='index'),
    
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
   path('register/', register_user, name='register'),
   path('product/<int:pk>',views.product, name='product'),
   path('category/<str:foo>',views.category, name='category'),
   
]