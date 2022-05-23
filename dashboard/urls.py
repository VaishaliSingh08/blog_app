from django.urls import path, include
from django.conf.urls.static import static
from blog import settings
from dashboard import views

urlpatterns = [

    path('dashboard', views.dash, name='dash'),
    path('add_blog_post', views.add_blog_post, name='add_blog_post'),
    path('all_blogs', views.all_blogs, name='all_blogs'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit_blog/<int:id>', views.edit_blog, name='edit_blog'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


##attached media folder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

