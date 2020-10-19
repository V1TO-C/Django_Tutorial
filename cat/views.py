from django.db.models.base import Model
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat

# Create your views here.

def cat_list(request):
    cat = Cat.objects.all()

    return render(request, 'back/cat_list.html', {'cat':cat})


def cat_add(request):
    if request.method == 'POST':

        cat_name = request.POST.get('catname')

        if cat_name == "":
            error = "Name of Cathegory Required!"
            return render(request, 'back/error.html', {'error':error})

        if len(Cat.objects.filter(name=cat_name)) != 0:
            error = "The Cathegory is already created!"
            return render(request, 'back/error.html', {'error':error})

        b = Cat(name=cat_name)
        b.save()
        return redirect('cat_list')

    return render(request, 'back/cat_add.html')


def cat_delete(request, pk):
    try:
        cat = Cat.objects.get(pk=pk)
        cat.delete()

        return redirect('cat_list')
    
    except:
        error = "Something Wrong"
        return render(request, 'back/error.html', {'error':error})