import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader

from restolax.models import Users, userForm, deleteUserForm, updateUserForm

from django.urls import path


def index(request):
    aboutInfodict = {
        'welcome': "Добро пожаловать в",
        'name': 'Restolax',
        'sub': "Радуем клиентов каждый день!"
    }
    context = {"aboutdata": aboutInfodict}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def about(request):
    aboutInfodict = {
        'head': "Наш ресторан очень быстро развивающийся",
        'subhead': "Наш девиз качество должно быть превыше, количества!",
        'col1': "Цены доступные для среднего класса и выше",
        'col2': "Только свежие и вкуснейшие продукты",
        'col3': "Шеф повара лучшие из лучших",
        'text': "Мы рассчитываем на поддержку каждого, и стремимся повысить уровень готовки каждый день!"

    }
    context = {"aboutdata": aboutInfodict}
    template = loader.get_template('about.html')
    return HttpResponse(template.render(context, request))


def chefs(request):
    from restolax import models
    all_users = models.Users.objects.all()
    usersInfo = all_users.values('login', 'password', 'black_list')
    text = {
        'text': 'Наши лучшие повара!'
    }
    chefInfo1 = {
        'text': 'Middle chef!',
        'firstname': 'Karim',
        'surname': 'Ilyasov',
        'age': 19,
        'email': 'Ilyasov@ok.com',
        'img': 'images/assets/img/chefs/chef_karim.jpg'
    }
    chefInfo2 = {
        'text': 'Junior chef!',
        'firstname': 'Ulan',
        'surname': 'Erikov',
        'age': 20,
        'email': 'Erikov@ok.com',
        'img': 'images/assets/img/chefs/chef_ulan.jpg'
    }
    chefInfo3 = {
        'text': 'Middle chef!',
        'firstname': 'Aldiyar',
        'surname': 'Tagaibekov',
        'age': 19,
        'email': 'Tagaibekov@ok.com',
        'img': 'images/assets/img/chefs/chef_alldick.jpg'
    }
    cheflist = (text, chefInfo1, chefInfo2, chefInfo3)
    context = {"aboutdata": cheflist, "novemberUsers": usersInfo}
    template = loader.get_template('chefs.html')
    return HttpResponse(template.render(context, request))


def contact(request):
    contactInfodict = {
        "title": "Почему мы?",
        'sub': "Почему люди выбирают наш ресторан?"
    }
    context = {"aboutdata": contactInfodict}
    template = loader.get_template('contact.html')
    return HttpResponse(template.render(context, request))


def events(request):
    contactInfodict = {
        "title": "Организуем праздник в нашем ресторане"
    }
    context = {"aboutdata": contactInfodict}
    template = loader.get_template('events.html')
    return HttpResponse(template.render(context, request))


def gallery(request):
    contactInfodict = {
        "title": "Фото нашего ресторана!"
    }
    context = {"aboutdata": contactInfodict}
    template = loader.get_template('gallery.html')
    return HttpResponse(template.render(context, request))


def menu(request):
    contactInfodict = {
        "title": "Наше изысканейшее меню!"
    }
    context = {"aboutdata": contactInfodict}
    template = loader.get_template('menu.html')
    return HttpResponse(template.render(context, request))


def specials(request):
    contactInfodict = {
        "title": "Попробуйте наши блюда!"
    }
    context = {"aboutdata": contactInfodict}
    template = loader.get_template('specials.html')
    return HttpResponse(template.render(context, request))


def signUp(request):
    testData = {
        "title": "hello world!"
    }
    context = {"hello": testData}
    template = loader.get_template('signUp.html')
    return HttpResponse(template.render(context, request))


def addUser(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = userForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "addUser.html", context)


def deleteAcc(request, id = 3):
    testData = {
        "title": "hello world!"
    }
    context = {"data": Users.objects.get(id=id), "id": id}
    template = loader.get_template('deleteAcc.html')
    return HttpResponse(template.render(context, request))


def deleteUser(request, id = 3):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Users, id=id)

    # add the dictionary during initialization
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page

    return render(request, "deleteUser.html", context)


def updateAcc(request, id = 3):
    testData = {
        "title": "hello world!"
    }
    context = {"data": Users.objects.get(id=id), "id": id}
    template = loader.get_template('updateAcc.html')
    return HttpResponse(template.render(context, request))


def updateUser(request, id = 3):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(Users, id=id)

    # add the dictionary during initialization
    form = updateUserForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "updateUser.html", context)
