from django.db import models
from django.contrib.auth.models import User



# Create your models here

class Category(models.Model):
    Category_name = models.CharField(max_length=50 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.Category_name



STATUS_CHOICES=(
    ("Undone","Undone"),
    ("Done","Done")
)




class Complain(models.Model):
    title= models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE ,related_name="complaints_authored" )
    featured_image=models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=2000)
    complain_body= models.TextField(max_length=2000)
    complain_status= models.CharField(max_length=20,choices=STATUS_CHOICES, default="Undone")
    is_featured= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField( User , default=None , blank=True ,related_name="liked_complaints")

    def __str__(self):
        return self.title
    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = {
    ("Like","Like"),
    ("Dislike","Dislike"),
}

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Complain,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES , default='Like',max_length=10)

    def __str__(self):
        return str(self.post)