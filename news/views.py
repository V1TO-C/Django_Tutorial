from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from cat.models import Cat
from subcat.models import SubCat
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime

# Create your views here.

def news_detail(request, word):

    site = Main.objects.get(pk=2)
    news = News.objects.filter(name=word)

    return render(request, 'front/news_detail.html', {'site':site, 'news': news})


def news_list(request):

    news = News.objects.all()

    return render(request, 'back/news_list.html', {'news':news})


def news_add(request):

    cats = Cat.objects.all()
    subcats = SubCat.objects.all()

    if request.method == "POST":

        newstitle = request.POST.get('newstitle')
        newssubcat = request.POST.get('newssubcat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        subcat = SubCat.objects.get(pk=newssubcat)

        if newstitle == "" or newstxt == "" or newstxtshort == "" or newssubcat == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
        except:
            error = "Please Input Your Image"
            return render(request, 'back/error.html', {'error':error})   

        if str(myfile.content_type).startswith("image"):
            if myfile.size < 5000000 :
                b = News(name=newstitle, catname=subcat.catname, subcatname=subcat.name, catid=0, short_txt=newstxtshort, body_txt=newstxt, date=dateNow(), time=timeNow(), picname=filename, picurl=url, writer="-", show=0)
                b.save()
                return redirect('news_list')
            else:
                fs = FileSystemStorage()
                fs.delete(myfile)
                error = "Your Pic Is Bigger Then 5 MB"
                return render(request, 'back/error.html', {'error':error})
        else:
            fs = FileSystemStorage()
            fs.delete(myfile)
            error = "Your Pic Format is not supported"
            return render(request, 'back/error.html', {'error':error})

    return render(request, 'back/news_add.html', {'cats':cats, 'subcats':subcats})


def news_delete(request, pk):
    try:
        article = News.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(article.picname)
        article.delete()

        return redirect('news_list')
    
    except:
        error = "Something Wrong"
        return render(request, 'back/error.html', {'error':error})   


def news_edit(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except:
        error = "News not found."
        return render(request, 'back/error.html', {'error':error})

    article = News.objects.get(pk=pk)
    subcats = SubCat.objects.all()

    if request.method == "POST":

        newstitle = request.POST.get('newstitle')
        newssubcat = request.POST.get('newssubcat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        subcat = SubCat.objects.get(pk=newssubcat)

        if newstitle == "" or newstxt == "" or newstxtshort == "" or newssubcat == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
        except:
            b = News.objects.get(pk=pk)

            b.name = newstitle
            b.short_txt = newstxtshort
            b.body_txt = newstxt
            """b.date = dateNow()
            b.time = timeNow() """
            b.catname = subcat.catname
            b.subcatname = subcat.name
            b.catid = newssubcat

            b.save()
            return redirect('news_list')   

        if str(myfile.content_type).startswith("image"):
            if myfile.size < 5000000 :

                b = News.objects.get(pk=pk)
                fss = FileSystemStorage()
                fss.delete(b.picname)

                b.name = newstitle
                b.short_txt = newstxtshort
                b.body_txt = newstxt
                """b.date = dateNow()
                b.time = timeNow() """
                b.picname = filename
                b.picurl = url
                b.catname = subcat.catname
                b.subcatname = subcat.name
                b.catid = newssubcat

                b.save()
                return redirect('news_list')
            else:
                fs = FileSystemStorage()
                fs.delete(myfile)
                error = "Your Pic Is Bigger Then 5 MB"
                return render(request, 'back/error.html', {'error':error})
        else:
            fs = FileSystemStorage()
            fs.delete(myfile)
            error = "Your Pic Format is not supported"
            return render(request, 'back/error.html', {'error':error}) 

    return render(request, 'back/news_edit.html', {'pk':pk, 'article':article, 'subcats':subcats})


# help functions.

def dateNow():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    if len(str(month)) == 1:
        month = "0" + str(month)

    if len(str(day)) == 1:
        day = "0" + str(day)

    date = str(year) + "/" + str(month) + "/" + str(day)
    return date


def timeNow():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute

    if len(str(hour)) == 1:
        hour = "0" + str(hour)

    if len(str(minute)) == 1:
        minute = "0" + str(minute)

    time = str(hour) + ":" + str(minute)

    return time