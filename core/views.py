from django.shortcuts import render #redirect
from core.models import Evento

# Create your views here.
def lista_eventos(request):
    usuario = request.user #pega so os do usuarios que estao logados
    evento = Evento.objects.filter( usuario = usuario) #pega so os do usuarios que estao logados #evento = Evento.objects.all() pega todos eventos de todos usuarios #Evento.objects.get(id=1) #só o do primeito evento #for evento in eventos
    dados = {'eventos': evento} #dicionario
    return render(request,'agenda.html',dados)

    #tem que registrar no diretorio de templates em agenda/
    # 'DIRS': [os.path.join(BASE_DIR, 'templates')],

# def index(request):
#     return redirect('/agenda/') 