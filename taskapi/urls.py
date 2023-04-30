from django.urls import path, include
from .views import ReadCreate, UpdateDelete

urlpatterns=[
    path("",ReadCreate.as_view()),
    path("<int:pk>/",UpdateDelete.as_view())
]
