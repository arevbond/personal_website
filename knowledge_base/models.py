from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __repr__(self):
        return f"Category: {self.name}."


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __repr__(self):
        return f"Category: {self.name}."


class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    time = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(to=Tag, related_name="posts")

    def __repr__(self):
        return f"Post: {self.title}."


class Folder(models.Model):
    name = models.CharField(max_length=30)
    posts = models.ManyToManyField(Post)
    folders = models.ManyToManyField("self")

    def __repr__(self):
        return f"Folder: {self.name}."
