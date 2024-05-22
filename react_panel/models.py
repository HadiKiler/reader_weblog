from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey


class User(AbstractUser):
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    def __str__(self):
        return self.username


class Category(models.Model):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def children(self):
        children = []
        ids = []
        print(self.post_set.all())
        children.extend(self.post_set.all())
        for subCategory in self.category_set.all():
            children.extend(subCategory.post_set.all())
            for extraCategory in subCategory.category_set.all():
                children.extend(extraCategory.post_set.all())
        for child in children:
            ids.append(child.id)
        return ids
        

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/')
    content = RichTextUploadingField()
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)


    def __str__(self):
        return self.title


class Comment(models.Model):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=75 ,null=True)
    email = models.EmailField(max_length=75, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} on {self.post}'

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')  # Ensure each user can like a post only once

    def __str__(self):
        return f'{self.user.username} likes {self.post}'
    