from django.urls import path
from .views import (
    refectory_page,
    create_token,
    validate_token,
    scan_token,
    queue_status
)

app_name = 'refectory'

urlpatterns = [
    path("", refectory_page, name="home"),
    path("create-token/", create_token, name="create-token"),
    path("validate-token/<uuid:pk>", validate_token, name="validate-token"),
    path("scan-token/<uuid:pk>/", scan_token, name="scan-token"),
    #path('queue-status/', queue_status, name='queue-status'),
]
