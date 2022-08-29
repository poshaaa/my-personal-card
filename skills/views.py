from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F

from .models import Skills, Element, Aboutme, Examples, Contact


def index(request):
    abouts = Aboutme.objects.all()
    skills = Skills.objects.all()
    skill_1 = Skills.objects.filter(id=1)
    element_1 = Element.objects.filter(description_id=1)
    skill_2 = Skills.objects.filter(id=2)
    element_2 = Element.objects.filter(description_id=2)
    skill_3 = Skills.objects.filter(id=3)
    element_3 = Element.objects.filter(description_id=3)
    skill_4 = Skills.objects.filter(id=4)
    element_4 = Element.objects.filter(description_id=4)
    examp = Examples.objects.all()
    contacts = Contact.objects.all()
    return render(request, 'skills/index.html',
                  {'contacts': contacts,'examp': examp, 'abouts': abouts, 'element_4': element_4, 'element_3': element_3,
                   'element_2': element_2,
                   'element_1': element_1,
                   'title': 'Навыки', 'skills': skills, 'skill_4': skill_4, 'skill_3': skill_3, 'skill_2': skill_2,
                   'skill_1': skill_1})
