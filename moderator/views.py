from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect

# Create your views here.
def ni(request):
    if request.method == 'POST':
        qrcode_data = request.POST.get('qrcode_data', '')
        # Aqui você processa os dados:
        # Por exemplo, verifique no banco de dados, registre um evento, etc.
        print(f"Dados do QR Code recebidos: {qrcode_data}")

        # Exemplo de lógica de processamento:
        if qrcode_data == "URL_VALIDA":
            # Faça algo e redirecione
            return redirect('home')
        else:
            # Lide com dados inválidos
            return render(request, 'moderator/scanner.html', {'error': 'QR Code inválido'})
            
    # Caso alguém acesse via GET (não deve acontecer nesta implementação), redirecione ou mostre o template
    return render(request, 'moderator/scanner.html')    

@csrf_protect
def processar_scan_view(request):
    if request.method == 'POST':
        qr_data = request.POST.get('qrcode_data', '')
        
        print("QR recebido:", qr_data)
        return redirect(qr_data)
        # aqui você processa, salva, valida, etc.

    return render(request, "moderator/scanner.html")