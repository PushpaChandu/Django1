from django.http import HttpResponse
from django.template import loader
from .models import student1
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
  records1= student1.objects.all().values()
  output = ""
  template=loader.get_template("myfirst.html")
  context = {
    'mymembers': records1,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add1.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  obj = student1(firstname=x, lastname=y)
  obj.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = student1.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = student1.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = student1.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))


