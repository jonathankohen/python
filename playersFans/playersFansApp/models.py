from django.db import models

# Create your models here.
class Player(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	team = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __repr__(self):
		return f"Player Object {self.firstname} - {self.id}"

class Fan(models.Model):
	firstname = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255, null = True)
	# books = models.ManyToManyField(Book, related_name="publishers")
	favPlayers = models.ManyToManyField(Player, related_name = "fans")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __repr__(self):
		return f"Fan Object {self.firstname} - {self.id}"






