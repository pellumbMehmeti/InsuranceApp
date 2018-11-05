from django.conf.urls import url
from .views import UserListApiView, UserRetrieveApiView
app_name = 'Backend'
urlpatterns = [
    url(r'^users/$', UserListApiView.as_view()),
    url(r'^users/(?P<user_id>\w+)/?$', UserRetrieveApiView.as_view()),
]
