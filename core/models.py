from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#criar a tabela Eventos com os fields titulo, data do evento, etc
class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True) #podeser nulo
    data_evento = models.DateTimeField(verbose_name='Data do Evento') #nao pode ser nulo
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data da Criação') #automaticamente insere a hora 
    usuario = models.ForeignKey(User, on_delete = models.CASCADE) #vamos usar os usuarios do django admin que criamos
    #on_delete = models.CASCADE se o usuario for excluido exclui tb todos os eventos dele
    #python3 manage.py sqlmigrate core 0002
    #python3 manage.py migrate core 0002
#para fazer com que a classe vire uma tabela no banco de dados
#python3 manage.py makemigrations
#python3 manage.py makemigrations core -> olha so pro app core
#python3 manage.py sqlmigrate core 0001

    class Meta:
        db_table = 'evento' #exigindo que a tabela se chame evento
    
#python3 manage.py migrate core 0001-> vai fazer as creates tables

#agora vamo registrar a tabela no admin.py

    def __str__(self):
        return self.titulo #agora vai aparecer o titulo do evento correto

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%Mhrs')