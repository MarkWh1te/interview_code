# coding:utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^msg/$',
        views.MessageCreateListView.as_view(),
        name ="msg_create_list"
        ),
    url(r'user_msg/$',
        views.UserMessageListView.as_view(),
        name ="user_msg_list"
        )
]

