from django.db import models

# Create your models here.
class Cluster(models.Model):
        name = models.CharField(max_length=128,unique=True)
        description = models.CharField(max_length=512)
        number_of_cores = models.IntegerField()
        created_time = models.DateTimeField(auto_now_add=True)
        modified_time = models.DateTimeField(auto_now=True)

        def __str__(self):
                return str(self.name)

class Institution(models.Model):
        name = models.CharField(max_length=256,unique=True)
        created_time = models.DateTimeField(auto_now_add=True)
        modified_time = models.DateTimeField(auto_now=True)

        def __str__(self):
                return str(self.name)

class User(models.Model):
        #...
        username = models.CharField(max_length=64,unique=True, verbose_name="Username")
        common_name = models.CharField(max_length=128, verbose_name="Common Name")
        #userID = models.IntegerField(unique=True)
        email = models.CharField(max_length=128, verbose_name="Email")
        disabled = models.BooleanField(default=False)
        institution = models.ForeignKey(Institution)
        projects = models.ManyToManyField(Project, through='UserProjectMembership')
        created_time = models.DateTimeField(auto_now_add=True)
        modified_time = models.DateTimeField(auto_now=True)
        def __str__(self):
                return self.commonName

class UserProjectMembership(models.Model):
        user = models.ForeignKey(User)
        project = models.ForeignKey(Project)
        date_joined = models.DateField()
        date_left = models.DateField(default=datetime.date.max)
        project_lead = models.BooleanField(default=False)
        created_time = models.DateTimeField(auto_now_add=True)
        modified_time = models.DateTimeField(auto_now=True)
        def __str__(self):
                return (str(self.user)+":"+str(self.project)+":"+str(self.dateJoined)+":"+str(self.dateLeft))
