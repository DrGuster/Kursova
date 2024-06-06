from django.urls import path
from. import views
from django.contrib.auth.views import LogoutView
from. import consumers

websocket_urlpatterns = [
    path("ws/chat_detail/<str:room_name>", consumers.ChatConsumer.as_asgi()),
]

urlpatterns = [
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='user_profile'),
    path('logout/', LogoutView.as_view(template_name='logout.html', next_page='chat'), name='logout'),
    path('new_chat/', views.new_chat, name='new_chat'),
    path('chat_list/', views.chat_list, name='chat_list'),
    path('chat_detail/<int:pk>/', views.chat_detail, name='chat_detail'),
    path("ws/chat_detail/<str:room_name>/", consumers.ChatConsumer.as_asgi()),
]