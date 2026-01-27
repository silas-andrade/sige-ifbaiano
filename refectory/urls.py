from django.urls import path
from .views import (
    refectory_page,
    create_token
)

app_name = 'refectory'


urlpatterns = [
    path("", refectory_page, name="home"),
    path("create-token/", create_token, name="create-token"),
]
