from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime


from loans.models import Loan, Material, LoanApplication
from .forms import LoanApplicationForm
from accounts.models import User


@login_required(login_url="/accounts/login/")
def RequestLoan(request):
    form = LoanApplicationForm()

    if request.method == 'POST':
        user = User.objects.get(email=request.user)
        form = LoanApplicationForm(request.POST)
        if form.is_valid:
            if not user.is_blocked_loans:
                pedido = form.save(commit=False)
                pedido.user = user
                pedido.save()
                return redirect('loans:dashboard-user')
            else:
                return HttpResponse('<h1>Você está proibido de fazer empréstimos</h1>')
        
    context = {
        'form':form,   
    }
    return render(request, "loans/solicitar_emprestimos.html", context)


@login_required(login_url="/accounts/login/")
def MakeLoanReturn(request, pk):
    loan = Loan.objects.get(id=pk)
    if request.user == loan.user:
        loan.is_returned = True
        loan.date_returned = datetime.now()
        loan.save()
        return redirect('loans:dashboard-user')
    else:
        return HttpResponse('<h1>Você não pode fazer isso!</h1>')



@login_required(login_url='/accounts/login/')
def DashboardUser(request):

    context = {
            'pedidos_pendentes':LoanApplication.objects.filter(
                user=User.objects.get(email=request.user), 
                is_pending=True
                ),
            'pedidos_respondidos':LoanApplication.objects.filter(
                user=User.objects.get(email=request.user), 
                is_pending=False,
                ),
            'loans':Loan.objects.filter(
                user=User.objects.get(email=request.user), 
                ),
       }
    return render(request, "loans/dashboard_user.html", context)




@login_required(login_url='/accounts/login/')
def DashboardAdmin(request):
    """
    Mostra aos moderadores todos os pedidos pendentes 
    e materias disponíveis  
    """
    if not request.user.is_staff:
        return redirect('dashboard-user')
    
    else:
        context = {
            'pedidos':LoanApplication.objects.filter(is_pending=True),
            'materiais':Material.objects.filter(available_quantity__gte=1),
            'emprestimos_esperando_devolucao':Loan.objects.filter(is_returned=False),
            'emprestimos_esperando_confimacao_de_devolucao':Loan.objects.filter(is_returned=True, is_return_confirmed=False),
        }
        return render(request, "loans/dashboard_admin.html", context)



@login_required(login_url='/accounts/login/')
def ViewAllLoans(request):
    user = User.objects.get(email=request.user)
    emprestimos_devolvidos = list(
         Loan.objects.filter(user=user, is_return_confirmed=True)
    )
    emprestimos_nao_devolvidos = list(
         Loan.objects.filter(user=user, is_return_confirmed=False)
    )
    
    context = {
        'emprestimos_devolvidos':emprestimos_devolvidos,
        'emprestimos_nao_devolvidos':emprestimos_nao_devolvidos,
    }
    return render(request, "loans/all_loans.html", context)


@login_required(login_url='/accounts/login/')
def BlockUser(request, pk):
    if not request.user.is_staff:
        return redirect('dashboard-user')
    
    else:
        user = User.objects.get(id=pk)

        if user.is_blocked_loans:
            user.is_blocked_loans = False
        else:
            user.is_blocked_loans = True

        user.save()
    return redirect('loans:dashboard-admin')

@login_required(login_url='/accounts/login/')
def ViewMaterials(request):
    if request.user.is_staff:
        materias = Material.objects.all()
        context = {
            'materiais':materias,   
        }
        return render(request, "moderator/material.html", context)
    else:
         return redirect('dashboard-user')
    

@login_required(login_url='/accounts/login/')
def DeleteMaterial(request, pk):
    if request.user.is_staff:
        materiais = Material.objects.get(id=pk)
        materiais.delete()
        return redirect('loans:dashboard-admin')
    else:
        return redirect('loans:dashboard-user')


@login_required(login_url='/accounts/login/')
def AcceptMaterialReturn(request, pk):
    if not request.user.is_staff:
        return redirect('loans:dashboard-user')
    else:
        loan = Loan.objects.get(id=pk)
        if loan.is_returned:
            loan.return_confirmed = True
            loan.save()

            material = Material.objects.get(nome=loan.material)
            material.available_quantity += loan.quantity
            material.save()

            return redirect('loans:dashboard-admin')
        return redirect('loans:dashboard-admin')


@login_required(login_url='/accounts/login/')
def AcceptLoanApplication(request, pk):
    if not request.user.is_staff:
        return redirect('loans:dashboard-user')
    else:
        loan_application = LoanApplication.objects.get(id=pk)
        material = Material.objects.get(name=loan_application.material.name)

        if loan_application.is_pending and material.available_quantity >= loan_application.quantity and loan_application.quantity > 0:
            loan_application.is_pending = False
            loan_application.is_approved = True
            loan_application.save()

            material.available_quantity -= loan_application.quantity
            material.save()
            
            Loan.objects.create(
                user=loan_application.user,
                material=material,
                expected_return_date=loan_application.expected_return_date,
                quantity=loan_application.quantity,
                who_approved=User.objects.get(email=request.user)
            )
            return redirect('loans:dashboard-admin')
        return redirect('loans:dashboard-admin')
        


@login_required(login_url='/accounts/login/')
def RejectLoanApplication(request, pk):
    if not request.user.is_staff:
        return redirect('loans:dashboard-user')
    else:
        loan_application = LoanApplication.objects.get(id=pk)
        if loan_application.is_pending:
            loan_application.is_pending = False
            loan_application.is_approved = False
            loan_application.save()
            return redirect('loans:dashboard-admin')
        return redirect('loans:dashboard-admin', {"warning":"This request has already been fulfilled"})