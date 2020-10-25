from django.db import models
from django.db.models.base import Model
from django.shortcuts import render, get_object_or_404, redirect
from .models import SubCat
from cat.models import Cat

# Create your views here.

def subcat_list(request):
    subcats = SubCat.objects.all()

    return render(request, 'back/subcat_list.html', {'subcats':subcats})


def subcat_add(request):
    
    cat = Cat.objects.all()
    if request.method == 'POST':

        subcat_name = request.POST.get('subcatname') 
        cat_pk = request.POST.get('catname')

        if subcat_name == "" or cat_pk == "":
            error = "Name of SubCathegory and Cathegory Required!"
            return render(request, 'back/error.html', {'error':error})

        if len(SubCat.objects.filter(name=subcat_name)) != 0:
            error = "The SubCathegory is already created!"
            return render(request, 'back/error.html', {'error':error})

        cat_name = Cat.objects.get(pk=cat_pk).name
        b = SubCat(name=subcat_name, catname=cat_name, catid=cat_pk)
        b.save()
        return redirect('subcat_list')

    return render(request, 'back/subcat_add.html', {'cat_name':cat})


def subcat_delete(request, pk):
    try:
        subcat = SubCat.objects.get(pk=pk)
        subcat.delete()

        return redirect('subcat_list')
    
    except:
        error = "Something Wrong"
        return render(request, 'back/error.html', {'error':error})