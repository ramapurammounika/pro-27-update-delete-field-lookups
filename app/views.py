from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q




def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='kabaddi')
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpage(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='kabaddi')
    QSW=Webpage.objects.exclude(topic_name='kabaddi')
    QSW=Webpage.objects.all()[::2]
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.all().order_by('-name')
    QSW=Webpage.objects.filter(topic_name='hockey').order_by('-name')
    QSW=Webpage.objects.order_by(Length('name'))
    QSW=Webpage.objects.order_by(Length('name').desc())
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__startswith='r')
    QSW=Webpage.objects.filter(name__endswith='a')
    QSW=Webpage.objects.filter(name__contains='a')
    QSW=Webpage.objects.filter(Q(topic_name='kabaddi')|Q(name='bha'))
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__in=['bha','appu','teja'])
    QSW=Webpage.objects.filter(Q(topic_name='kabaddi') | Q(name='appu'))
    QSW=Webpage.objects.filter(Q(topic_name='hockey') & Q(url__startswith='https'))
    QSW=Webpage.objects.filter(name__regex='\W{3}')
    d={'webpage':QSW}
    return render(request,'display_webpage.html',d)

def display_Access(request):
    QSA=Accessrecord.objects.all()
    QSA=Accessrecord.objects.filter(date__gt='2000-10-04')
    QSA=Accessrecord.objects.filter(date__gte='2000-10-04')
    QSA=Accessrecord.objects.filter(date__lt='2000-10-04')
    QSA=Accessrecord.objects.filter(date__lte='2000-10-04')
    QSA=Accessrecord.objects.filter(date__year='2000')
    QSA=Accessrecord.objects.filter(date__month='10')
    QSA=Accessrecord.objects.filter(date__day='04')
    


    d={'Access':QSA}
    return render(request,'display_Access.html',d)

def update_webpage(request):
    Webpage.objects.all()
    Webpage.objects.filter(name='teja').update(topic_name='kabaddi')
    Webpage.objects.filter(name='chinna').update(url='https://chinna.in')
    Webpage.objects.filter(name='bha').update(url='https://bha.in')
    
    Webpage.objects.filter(name='appu').update(url='https://bha.in')
    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    return render(request,'display_webpage.html',d)


def delete_webpage(request):
    Webpage.objects.filter(topic_name='kabaddi').delete()
    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    return render(request,'display_webpage.html',d)
