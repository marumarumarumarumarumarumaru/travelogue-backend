from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Location(models.Model):
    name = models.CharField(max_length=250, default=None, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    pic_url = models.CharField(max_length=250, blank=True)
    users_visited = models.ManyToManyField(User, related_name='locations_visited')

    def __str__(self):
        return f"Name = {self.name}, Latitude = {self.latitude}, Longitude = {self.longitude}, Picture = {self.pic_url}"

class Review(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Title = {self.title}, Text = {self.text}, Posted at = {self.posted_at}, User = {self.user}, Location = {self.location}"

class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Text = {self.text}, Posted at = {self.posted_at}, User = {self.user}, Review = {self.review}"
