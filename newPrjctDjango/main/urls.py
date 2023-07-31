from django.urls import path, include
from . import views
from .views import RegisterUser

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('delete/<int:id>', views.delete),
    path('<int:pk>/update', views.TasksUpdateView.as_view(), name='tasks-update'),
    path('registration', RegisterUser.as_view(), name='registration')
]
