from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.cache import cache_page

from women.views import WomenHome, about, LoginUser, WomenCategories, ShowPost, AddPage, RegisterUser, \
    logout_user, ContactView

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('about/', about, name='about'),
    # path('add_page/', add_page, name='add_page'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('categories/<slug:cat_slug>', WomenCategories.as_view(), name='categories'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('register/', RegisterUser.as_view(), name='register'),


]
