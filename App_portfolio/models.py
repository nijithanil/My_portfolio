from django.db import models


# Create your models here.

class sidebar_edit(models.Model):
    img = models.ImageField(upload_to='sidebar_image')
    name = models.CharField(max_length=150, unique=True)


class Home_Image(models.Model):
    img = models.ImageField(upload_to='First_page_edit')


class About(models.Model):
    Heading = models.CharField(max_length=150, unique=True)
    Sub_Heading = models.CharField(max_length=150, unique=True)
    Image = models.ImageField(upload_to='About_Update')
    Website = models.CharField(max_length=150, unique=True)
    Link = models.CharField(max_length=150, unique=True)
    Phone = models.CharField(max_length=150, unique=True)
    City = models.CharField(max_length=150, unique=True)
    Degree = models.CharField(max_length=150, unique=True)
    Email = models.EmailField(max_length=100, unique=True)
    Freelance = models.CharField(max_length=150, unique=True)


class Interests(models.Model):
    Icon = models.CharField(max_length=150, unique=True)
    Name = models.CharField(max_length=150, unique=True)


class Skills1(models.Model):
    Name1 = models.CharField(max_length=150, unique=True)
    Percentage1 = models.IntegerField()
class Skills2(models.Model):
    Name2 = models.CharField(max_length=150, unique=True)
    Percentage2 = models.IntegerField()


class Resume(models.Model):
    Project_Name = models.CharField(max_length=150, unique=True)
    Project_link = models.CharField(max_length=150, unique=True)
    Project_Specifications = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return '{}'.format(self.Project_Name)

class MyProject_categories(models.Model):
    Name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ['Name']
        verbose_name = 'category'
        verbose_name_plural = 'MyProjects_Categories'

    def __str__(self):
        return '{}'.format(self.Name)


class MyProjects_Update(models.Model):
    Project_Image = models.ImageField(upload_to='MyProjects_Update')
    Project_Link = models.CharField(max_length=150, )
    Category = models.ForeignKey(MyProject_categories, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Category)


class Services(models.Model):
    Services_Icon = models.CharField(max_length=150, )
    Services_Name = models.CharField(max_length=150, unique=True)
    Services_Quotes = models.CharField(max_length=200)


class MyTeam(models.Model):
    Quotes = models.TextField()
    Image = models.ImageField(upload_to='MyTeam')
    Name = models.CharField(max_length=150, unique=True)
    Position = models.CharField(max_length=150)

class Contact(models.Model):
    Location = models.CharField(max_length=150, unique=True)
    Email = models.EmailField(max_length=100, unique=True)
    Call = models.CharField(max_length=150, unique=True)
    Website = models.CharField(max_length=150, unique=True)
