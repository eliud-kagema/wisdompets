from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pet

def  index(request):
    pets = Pet.objects.all()
    template_name = 'adoptions/index.html'
    context = {
        'pets': pets
    }
    return render(request, template_name, context)

def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')

    template_name = 'adoptions/pet_detail.html'
    context = {
        'pet': pet
    }
    return render(request, template_name, context)