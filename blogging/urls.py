from django.urls import path
from blogging import views
from blog import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('<int:id>', views.blog_detail, name='blog_detail'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)