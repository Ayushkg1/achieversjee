from django.http import HttpResponse
from django.shortcuts import render
from .models import Chapter, Contact, Material, Mathematics, Physics, Chemistry


def index(request):
    all_chap = Chapter.objects.all()
    params = {'chapter':all_chap, 'no_of_chapters':len(all_chap)}
    return render(request, 'index.html',params)


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        contact = Contact(contact_name=name, email=email, phone=phone, contact_desc=desc)
        contact.save()
        alrt = True
        return render(request, 'contact.html', {'alrt':alrt})
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def material(request):
    materials = Material.objects.all()
    kaamkicheez = {'materials':materials}
    return render(request, 'material.html', kaamkicheez)

def study(request):
    math = Mathematics.objects.all()
    phy = Physics.objects.all()
    chm = Chemistry.objects.all()
    padhnekicheez = {'maths':math, 'phy':phy, 'chm':chm}
    return render(request, 'study.html', padhnekicheez)

def courses(request):
    chapters = Chapter.objects.all()
    parameters = {'chapters':chapters}
    return render(request, 'courses.html', parameters)
