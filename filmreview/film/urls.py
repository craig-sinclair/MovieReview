from django.urls import path
from film import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'film'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)