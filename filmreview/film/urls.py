from django.urls import path
from film import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'film'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('search/', views.search, name='search'),
    path('person/<int:person_id>/', views.person, name='person'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)