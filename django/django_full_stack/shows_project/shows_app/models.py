from django.db import models


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters."
        if len(postData['network']) < 3:
            errors["network"] = "Network title should be at least 3 characters."
        if len(postData['release_date']) == 0:
            errors["release_date"] = "Please enter a release date."
        if len(postData['desc']) < 10:
            errors["desc"] = "Description should be at least 10 characters."
        return errors


class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=15)
    release_date = models.CharField(max_length=10)
    desc = models.TextField("Show description")
    objects = ShowManager()
