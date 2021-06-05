from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    formulario = [
    {
        'monto': '5000',
        'tasa': '10',
        'plazo': '12',
        'cuota': '600',
        'total': '200',
        },
        {   
        'monto': '600',
        'tasa': '2',
        'plazo': '8',
        'cuota': '100',
        'total': '200',
        },

    ]    

    if request.method == 'POST':
        monto  = request.POST.get('monto')
        tasa  = request.POST.get('tasa')
        plazo  = request.POST.get('plazo')
        cuota  = request.POST.get('cuota')
        total  = request.POST.get('total')

        formulario
    else:

    ctx = {
        'formulario': formulario
    }

    return render(request, 'app1/index.html', ctx)
