from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Users
from django.http import HttpResponse

# Create your views here.
def users(request):
    user = Users.objects.all()
    content ={
        "user":user
    }
    return render(request, "profilerapp/home.html",content)


def add(request):
    return render(request, "profilerapp/add.html")


def addprocess(request):
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    email = request.POST.get("email")
    position = request.POST.get("position")

    if request.FILES.get("images"):
        user_pic = request.FILES.get("images")
    else:
        user_pic = "background21.png"

    try:
        return HttpResponse("Unique Email Only")

    except ObjectDoesNotExist:
        users = Users.objects.create(f_name=fname, l_name=lname, email=email, position=position, images=user_pic)
        users.save()
        return redirect('users')


def details(request, pk):
    user = Users.objects.get(id=pk)

    content = {
        'user':user
    }

    return render(request, 'profilerapp/details.html', content)

def delete(request,pk):
    user = Users.objects.get(id=pk).delete()
    return redirect("users")


def update(request, pk):
    user = Users.objects.get(id=pk)
    content = {
        "user":user
    }

    return render(request, 'profilerapp/update.html', content)


def updateprocess(request,pk):
    images = request.FILES.get("images")

    try:
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        position = request.POST.get("position")

    except (KeyError, Users.DoesNotExist):
        return HttpResponse("Failed To Update")

    else:
        user = Users.objects.get(id=pk)
        user.f_name = fname
        user.l_name = lname
        user.email = email
        user.position = position
        if images:
            user.images = images
        user.save()

        return redirect("details", pk=user.id)
        
