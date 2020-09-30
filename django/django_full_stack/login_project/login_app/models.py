from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        # check if email exists in db:
        user = User.objects.filter(email=postData['email'])

        if len(postData['email']) == 0:
            errors['email_required'] = "Email required to log in."
        elif len(user) == 0:
            errors['email_none'] = "Email not found."
        else:
            # if email is found, check pw w/bcrypt!
            if bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                print("Password match.")
            else:
                errors['pw_check'] = "Password is incorrect."
        return errors

    def reg_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        user = User.objects.filter(email=postData["email"])

        if len(postData['first_name']) < 2:
            errors["invalid_first_name"] = "First name should be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors["invalid_last_name"] = "Last name should be at least 2 characters."

        if len(postData['email']) == 0:
            errors['no_email'] = "Email is required"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['invalid_email'] = "Invalid email address!"
        else:
            if len(user) > 0:
                errors['email_in_use'] = "This email is already in use."

        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters."
        if postData['password'] != postData['c_password']:
            errors["pw_match"] = "Passwords must match!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Post(models.Model):
    content = models.TextField()
    # one to many
    uploader = models.ForeignKey(
        User, related_name="posts_uploaded", on_delete=models.CASCADE)
    # many to many
    likes = models.ManyToManyField(User, related_name="posts_liked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
