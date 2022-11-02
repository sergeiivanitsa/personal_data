from django.urls import path

from . import views

app_name = 'generate'

urlpatterns = [
    # path('', views.index),
    # path('generate/', views.generate),
    path('generate/', views.statement_generate, name='new_generate'),
    path('success/', views.success)
]
