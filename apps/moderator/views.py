from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect


@csrf_protect
def processar_scan_view(request):
    if request.method == 'POST':
        qr_data = request.POST.get('token_id')
        
        print("QR recebido:", qr_data)
        return redirect(qr_data)
        # aqui você processa, salva, valida, etc.

    return render(request, "moderator/scanner.html")