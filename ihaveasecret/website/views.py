from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from website.models import Message

def home(request):
  return HttpResponse("This is the homepage")

def view_messages(request):
  latest_message_list = Message.objects.order_by('-date')[:5]
  context = {'latest_message_list': latest_message_list}
  return render(request, 'website/view.html', context)

def view_message(request, message_id):
  try:
    m = Message.objects.get(pk=message_id)
  except Message.DoesNotExist:
    raise Http404
  return render(request, 'website/message.html', {'message': m})

def write_message(request):
  return HttpResponse("Write Message")
