from django.shortcuts import render

# Create your views here.
def crud(response):
    return render(response, 'estructura_crud.html')