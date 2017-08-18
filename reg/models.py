from django.db import models

# Create your models here.
class System(models.Model):
	name = models.CharField(max_length=128,unique=True)
	description = models.CharField(max_length=512)
	number_of_cores = models.IntegerField()
	created_time = models.DateTimeField(auto_now_add=True)
	modified_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Institution(models.Model):
	name = models.CharField(max_length=256,unique=True)
	created_time = models.DateTimeField(auto_now_add=True)
	modified_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class User(models.Model):
	username = models.CharField(max_length=64,unique=True, verbose_name="SCW Username")
	common_name = models.CharField(max_length=128, verbose_name="Common Name")
	#userID = models.IntegerField(unique=True)
	email = models.EmailField()
	disabled = models.BooleanField(default=False)
	institution = models.ForeignKey(Institution)
	created_time = models.DateTimeField(auto_now_add=True)
	modified_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.common_name

class FundingSource(models.Model):
	name = models.CharField(max_length=128, unique=True, verbose_name="Source Name")
	description = models.CharField(max_length=512)
	created_time = models.DateTimeField(auto_now_add=True)
	modified_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class ProjectCategory(models.Model):
	number = models.IntegerField(unique=True)
	name = models.CharField(max_length=128, unique=True, verbose_name="Category Name")
	description = models.CharField(max_length=512)
	created_time = models.DateTimeField(auto_now_add=True)
	modified_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
	
class ProjectStatus(models.Model):
	name = models.CharField(max_length=128, unique=True, verbose_name="Status")
	description = models.CharField(max_length=512)
	created_time = models.DateTimeField(auto_now_add=True)
	modified_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Project(models.Model):
	institution = models.ForeignKey(Institution)
	title = models.CharField(max_length=256, verbose_name="Project Title")
	description = models.CharField(max_length=1024, verbose_name="Project Description")
	pi_name = models.CharField(max_length=128, verbose_name="PI Name")
	pi_email = models.EmailField(verbose_name="PI Email")
	tech_lead = models.ForeignKey(User)
	funding_source = models.ForeignKey(FundingSource)
	category = models.ForeignKey(ProjectCategory)
	institution_reference = models.CharField(max_length=128, verbose_name="Owning institution project reference")
	start_date = models.DateField()
	end_date = models.DateField()
	requirements_software = models.CharField(max_length=512)
	requirements_gateways = models.CharField(max_length=512)
	requirements_training = models.CharField(max_length=512)
	requirements_onboarding = models.CharField(max_length=512)
	allocation_rse = models.BooleanField(default=False, verbose_name="RSE available to?")
	allocation_cputime = models.PositiveIntegerField(verbose_name="CPU time allocation")
	allocation_storage = models.PositiveIntegerField(verbose_name="Project group storage allocation")
	allocation_systems = models.ManyToManyField(System, through='ProjectSystemAllocation')
	users = models.ManyToManyField(User, through='ProjectUserMembership')
	created_time = models.DateTimeField(auto_now_add=True)
	modified_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class ProjectSystemAllocation(models.Model):
	project = models.ForeignKey(Project)
	system = models.ForeignKey(System)
	date_allocated = models.DateField()
	date_unallocated = models.DateField()
	created_time = models.DateTimeField(auto_now_add=True)
	modified_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return (str(self.project)+" on "+str(self.system)+" from "+str(self.date_allocated)+" to "+str(self.date_unallocated))

class ProjectUserMembership(models.Model):
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project)
	date_joined = models.DateField()
	date_left = models.DateField(default=datetime.date.max)
	created_time = models.DateTimeField(auto_now_add=True)
	modified_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return (str(self.user)+" on "+str(self.project)+" from "+str(self.date_joined)+" to "+str(self.date_left))

