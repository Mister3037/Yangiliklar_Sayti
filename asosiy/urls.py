from django.urls import path
from .views import *
from .processor import *





urlpatterns = [
    path('news/', HomeView.as_view()),
    path('contact/', ContactView.as_view()),
    path('local/', MahalliyYangiliklarView.as_view()),
    path('foreign/', XorijYangiliklarView.as_view()),
    path('technology/', TexnologiyaYangiliklarView.as_view()),
    path('sport/', SportYangiliklarView.as_view()),
    path('news/<slug:slug>/edit/', UpdateYangilikNews.as_view(), name="update_news"),
    path('news/<slug:slug>/', yangilik_detail, name="yangilik_detail"),
]