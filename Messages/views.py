from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Message
from Login.models import User
from .forms import MessageForm

# Create your views here.
@login_required
def send_message(request, username):
  if request.method == 'POST':
      form = MessageForm(request.POST)
      if form.is_valid():
        receptor = get_object_or_404(User, username=username)
        body = form.cleaned_data['body']
        emisor = request.user

        message = Message(receptor=receptor, body=body, emisor=emisor)
        message.save()
        return redirect('messages', username=username)
      else:
        print('mal')

@login_required
def messages_view(request, username):
  # Métodos como GET
  form = MessageForm()

  user = request.user
  if username.lower() == 'none':
    emisor = None
  else:
    emisor = get_object_or_404(User, username=username)

  # Busco los mensajes enviados y recibidos
  messages = Message.objects.filter(Q(emisor=user) | Q(receptor=user))
  # Filtro por emisor y receptor para tener las conversaciones activas
  unique_emisor = [elem['emisor'] for elem in messages.values('emisor').distinct()]
  unique_receptor = [elem['receptor'] for elem in messages.values('receptor').distinct()]
  # Busco en el modelo User los usuarios hallados
  emisores = User.objects.filter((Q(id__in=unique_emisor) & ~Q(id=user.id)) |
                                  Q(id__in=unique_receptor) & ~Q(id=user.id))

  # Filtro para obtener los mensajes con el usuario seleccionado
  if emisor:
    selected_messages = messages.filter(Q(emisor=emisor) | Q(receptor=emisor)).order_by('date')
  else:
    selected_messages = None

  return render(request, 'Messages/messages.html', {'messages': selected_messages, 'emisores': emisores, 'form': form})
