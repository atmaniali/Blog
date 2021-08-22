from django.urls import path
from .views import *
app_name = "main"
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('create/', createpost, name='create'),
    path('update/<post_id>/',updatepost, name='update'),
    path('<int:question_id>/', detail, name='detail'),
    path('send_request_friend/<int:user_id>/', send_freind_request, name = "send_freind_request"),
    path('accept_freind_request/<int:request_id>/', accept_freind_request, name= "accept_freind_request"),
]