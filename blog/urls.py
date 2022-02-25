from django.urls import path, include
from . import views
from .views import *

app_name = 'blog'


urlpatterns = [
    # path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
	# path('contact/', views.ContactView.as_view(), name="contact"),
    path('', views.blog, name='blog'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/',views.blog, name='post_tag'),
    # path('search/', views.post_search, name='post_search'),
]