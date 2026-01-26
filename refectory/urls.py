from django.urls import path
from .views import (
    refectory_page,
    create_token
)


urlpatterns = [
    path("", refectory_page, name="refectory"),
    path("create-token/", create_token, name="create-token"),
]
