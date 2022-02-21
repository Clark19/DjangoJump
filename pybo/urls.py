from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),
]

# 제네릭 뷰
# app_name = 'pybo'
# urlpatterns = [
#     path('', views.IndexView.as_view()),
#     path('<int:pk>/', views.DetailView.as_view()),
# ]