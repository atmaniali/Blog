from django.urls import path , include
from .views import *
app_name = "main"
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('create/', createpost, name='create'),
    path('update/<post_id>/',updatepost, name='update'),
    path('<int:question_id>/', detail, name='detail'),
    path("send_request", friendship_request, name = "fr")
]