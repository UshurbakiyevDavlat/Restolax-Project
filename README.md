I.	Complete following tasks Part-1: Main tasks (90 points)

 

- Adding data via the admin panel is not convenient. Create a separate page on which you should create a form. Through the form, you should be able to add data to the database.
 - Functionality to update and delete data from db. To implement the update, use the UpdateView class, and to delete it, use DeleteView.

Prepare report using in .docx document. Your report should include full description of the templates, answer to the questions provided above, archive program codes and upload them to the dl.iitu.kz.

 

So, here I have: Sign Up, Resign and delete buttons,
 
I am creating user with help of this form
This is user creating view
  
After creating I have this message and new data in db.

 
Here I have update password and login view

 
  
Well I have shown all three functional features.
There are code for them below:


class userForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Users

        # specify fields to be used
        fields = [
            "login",
            "password",
            "type",
            "bank_acc_id"
        ]


class deleteUserForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Users

        # specify fields to be used
        fields = [
            "login",
        ]


class updateUserForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Users

        # specify fields to be used
        fields = [
            "login",
            "password"
        ]







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



