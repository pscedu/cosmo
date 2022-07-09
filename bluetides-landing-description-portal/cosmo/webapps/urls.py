from django.urls import path
from . import views

app_name = 'webapps'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('people/', views.People.as_view(), name='people'),
    path('results/', views.Results.as_view(), name='results'),
    path('gallery/', views.Gallery.as_view(), name='gallery'),
    path('api-reference/', views.Reference.as_view(), name='api-reference'),
    path('tutorial/', views.Tutorial.as_view(), name='tutorial'),
    path('data-access/', views.DataAccess.as_view(), name='data-access'),
    path('data-structure/', views.Structure.as_view(), name='data-structure'),
    path('about/', views.About.as_view(), name='about'),
]
