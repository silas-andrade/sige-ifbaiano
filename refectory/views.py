import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import FichaAlmoco

TOKEN_ALMOCO = "ALMOCO2026"
LIMITE = 1100

def refectory_page(request):
    return render(request, 'refectory/refectory.html')

# =========================
# PÁGINAS
# =========================

def aluno_page(request):
    return render(request, "refectory/aluno_scanner.html")


def guarda_page(request):
    return render(request, "refectory/guarda_scanner.html")


# =========================
# ALUNO → GERA FICHA
# =========================

@csrf_exempt
def registrar_ficha(request):
    if request.method != "POST":
        return JsonResponse({"erro": "Método inválido"})

    data = json.loads(request.body)

    if data.get("token") != TOKEN_ALMOCO:
        return JsonResponse({"erro": "QR Code inválido"})

    if not request.user.is_authenticated:
        return JsonResponse({"erro": "Usuário não autenticado"})

    try:
        aluno = request.user.aluno
    except:
        return JsonResponse({"erro": "Usuário não é aluno"})
        hoje = timezone.now().date()

        ficha_existente = FichaAlmoco.objects.filter(
        aluno=aluno,
        data=hoje
    ).first()

    if ficha_existente:
        return JsonResponse({"ficha": ficha_existente.ficha_numero})

    total = FichaAlmoco.objects.filter(data=hoje).count()
    if total >= LIMITE:
        return JsonResponse({"erro": "Limite de fichas atingido"})

    ficha = FichaAlmoco.objects.create(
        ficha_numero=total + 1,
        aluno=aluno,
        data=hoje
    )

    return JsonResponse({"ficha": ficha.ficha_numero})


# =========================
# GUARDA → VALIDA FICHA
# =========================

@csrf_exempt
def validar_ficha(request):
    data = json.loads(request.body)
    token = data.get("token")

    try:
        ficha = FichaAlmoco.objects.get(token=token)
    except FichaAlmoco.DoesNotExist:
        return JsonResponse({"erro": "Ficha inválida"})

    if ficha.usada:
        return JsonResponse({"erro": "Ficha já utilizada"})

    ficha.usada = True
    ficha.hora_uso = timezone.now().time()
    ficha.save()

    return JsonResponse({
        "aluno": ficha.aluno.nome,
        "ficha": ficha.ficha_numero
    })