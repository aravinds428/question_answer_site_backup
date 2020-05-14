from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home-page'),
	path('displaycontent',views.display_content,name='display-content'),
	path('about',views.display_about,name='about'),
]
