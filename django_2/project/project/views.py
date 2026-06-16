from django.http import HttpResponse

def homepage(request):
  return HttpResponse("This is my homepage ")

def about(request):
  return HttpResponse("This is about me page django")