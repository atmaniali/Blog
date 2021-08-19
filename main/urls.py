from django.urls import path
from .views import (home, createpost, updatepost, detail)
app_name = "main"
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('create/', createpost, name='create'),
    path('update/<post_id>/',updatepost, name='update'),
    path('<int:question_id>/', detail, name='detail'),
]