from django.urls import path
from film import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'film'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('search/', views.search, name='search'),
    path('person/<int:person_id>/', views.person, name='person'),
    path('top/', views.top, name='top'),
    path('profile/', views.profile, name='profile'),
    path('search_suggestions/', views.search_suggestions, name='search_suggestions'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)