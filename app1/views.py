from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

formulario = [
{
    'monto': '5000',
    'tasa': '10',
    'plazo': '12',
    }
] 

def index(request):
   

    if request.method == 'POST':
        monto  = request.POST.get('monto')
        tasa  = request.POST.get('tasa')
        plazo  = request.POST.get('plazo')

        formulario.append(
            {
                'monto': monto,
                'tasa': tasa,
                'plazo': plazo,

            }
        )

        ctx = {
            'formulario': formulario
        }
        
        return render(request, 'app1/index.html', ctx)
        #return HttpResponse('Se agrego correctamente al formulario')
    else:
        ctx = {
            'formulario': formulario
        }

        return render(request, 'app1/index.html', ctx)
        
