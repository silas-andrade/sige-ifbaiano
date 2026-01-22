from django.urls import path
from .views import (
    refectory_page,
    aluno_page,
    guarda_page,
    registrar_ficha,
    validar_ficha,
)

app_name = "refectory"

urlpatterns = [
    path("", refectory_page, name="refectory"),
    path("aluno/", aluno_page, name="aluno_page"),
    path("guarda/", guarda_page, name="guarda_page"),

    # APIs
    path("api/registrar/", registrar_ficha, name="registrar_ficha"),
    path("api/validar/", validar_ficha, name="validar_ficha"),
]
