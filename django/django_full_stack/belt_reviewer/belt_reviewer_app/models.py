from django.db import models
import bcrypt


class UserManager(models.Manager):
    def regValidator(self, postData):
        errors = {}
        username_filter = User.objects.filter(username=postData['username'])

        if len(postData['name']) == 0:
            errors['name_req'] = "Name is required."
        elif len(postData['name']) < 3:
            errors['name_len'] = "Name must be at least 3 characters."

        if len(postData['username']) == 0:
            errors['username_req'] = "Username is required."
        elif len(postData['username']) < 3:
            errors['username_len'] = "Username must be at least 3 characters."
        else:
            if len(username_filter) > 0:
                errors['username_taken'] = "This username is already taken."

        if len(postData['pw']) < 4:
            errors['pw_len'] = "Password must be at least 4 characters."
        if postData['pw'] != postData['c_pw']:
            errors['c_pw_match'] = "Passwords must match."
        return errors

    def loginValidator(self, postData):
        errors = {}
        username_filter = User.objects.filter(username=postData['username'])
        if len(postData['username']) == 0:
            errors['username_req'] = "Username is required to login."
        elif len(username_filter) == 0:
            errors['username_not_found'] = "Username is not found. Please make sure you've registered."
        else:
            if bcrypt.checkpw(postData['pw'].encode(), username_filter[0].password.encode()):
                print("Password matches.")
            else:
                errors['pw_not_match'] = "Password is incorrect."
        return errors


class ItemManager(models.Manager):
    def itemValidator(self, postData):
        errors = {}
        if len(postData['item_name']) == 0:
            errors['item_req'] = "Item name required."
        elif len(postData['item_name']) < 3:
            errors['item_len'] = "Item name must be at least 3 characters."
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Item(models.Model):
    name = models.CharField(max_length=255)
    uploader = models.ForeignKey(
        User, related_name="items_uploaded", on_delete=models.CASCADE)
    favorites = models.ManyToManyField(User, related_name="items_favorited")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()
