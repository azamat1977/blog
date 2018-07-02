"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog.views import (article_listview, 
                        index, category_listview, ArticleCreateView, 
                        ArticleUpdateView, ArticleDeleteView, 
                        ArticleDetailView, CategoryCreateView,
                        CategoryDeleteView, CategoryUpdateView,
                        CategoryDetailView, login, logout, register)
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    # urls_for_article
    path('article/', article_listview),
    path('article/create/', ArticleCreateView.as_view()),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view()),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view()),
    path('article/<int:pk>/', ArticleDetailView.as_view()),

    # path('article/post_form/', post_form),


    # urls_for_category
    path('category/', category_listview),
    path('category/create/', CategoryCreateView.as_view()),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view()),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),

    # urls_for_login_logout
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
]


