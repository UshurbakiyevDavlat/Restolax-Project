import datetime

from django.db import models
from django import forms


# Create your models here.

class Users(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.IntegerField()
    bank_acc_id = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()

    # def getUsersCreatedToday(self):
    #     "Selecting all users which created 27.11.2021 from users table.."
    #     import datetime
    #     if self.created_at == datetime.date(2021, 11, 27):
    #         return self.login


class black_list(models.Model):
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateField()
    updated_at = models.DateField()


class bank_acc_info(models.Model):
    account_number = models.IntegerField()
    black_list = models.ForeignKey(black_list, on_delete=models.CASCADE)
    created_at = models.DateField()
    updated_at = models.DateField()


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
            "password"
        ]
