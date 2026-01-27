from django.urls import path
from .views import (
    refectory_page,
    create_token,
    validate_token
)

app_name = 'refectory'


urlpatterns = [
    path("", refectory_page, name="home"),
    path("create-token/", create_token, name="create-token"),
    path("validate-token/<uuid:pk>", validate_token, name="validate-token"),
]
