from django.urls import path
from .views import home, createpost, updatechek
app_name = "main"
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('create/', createpost, name='create'),
    path('updatechek/<str:pk>', updatechek, name='updatechek')
    # path('update/<str:pk>',updatepost, name='update'),
]