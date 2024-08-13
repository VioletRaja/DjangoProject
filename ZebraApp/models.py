from django.db import models
import datetime
import os

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('images/',new_filename)

class ContactUs(models.Model):
    username=models.CharField(max_length=200)
    phone=models.CharField(max_length=300)
    company=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    message=models.TextField(max_length=200)

    def __str__(self):
        return self.username

class services_pics(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")

    def __str__(self):
        return self.name


class Home_source(models.Model):
    Title=models.CharField(max_length=50,verbose_name='Title for this data',null=True,blank=False)
    video = models.FileField(upload_to=getFileName,null=True,blank=True,verbose_name='Upload a video to show in Slider')
    status=models.BooleanField(default=False,help_text="0-show,1=Hidden")
    logo_name=models.CharField(max_length=20,default=False,null=True,blank=True,verbose_name='logo name')
    logo=models.ImageField(upload_to=getFileName,null=True,blank=True,verbose_name='add a logo for counter')
    subject=models.CharField(max_length=50,null=True,blank=True,verbose_name='Subject will show under the logo')
    description=models.TextField(max_length=200,null=True,blank=True,verbose_name='Describtion will show under subject')
    DisplayFields=['title','logo_name']
    Project_Block_img_1=models.ImageField(upload_to=getFileName,null=True,blank=True)
    Project_Block_Vdo_2=models.FileField(upload_to=getFileName,null=True,blank=True)

    class Meta:
        db_table='HOME_SOURCE'

    def __str__(self):
        return self.Title
    
class home_url(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    home_url=models.URLField( max_length=200,verbose_name='Web site utube link URL',help_text='Enter the URL of the website',unique=False, blank=True,)
    print(home_url)
    def __str__(self):
        return self.Name
    

class Service_page(models.Model):
    Header=models.FileField(upload_to=getFileName,null=True,blank=False)
    

class projects_model(models.Model):
    Project_Header=models.FileField(upload_to=getFileName,null=True,blank=False)


class Project_catagory(models.Model):
    Project_album_name=models.CharField(max_length=150,null=1,blank=1,default=1)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    Customer=models.CharField(max_length=50,null=True,blank=True,default=1)
    description=models.TextField(max_length=500,null=True,blank=True)
    budget=models.IntegerField(null=True,blank=True)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Project_album_name
    

class Project_site_pics(models.Model):
    catagory=models.ForeignKey(Project_catagory,on_delete=models.CASCADE,null=True, blank=True)
    # catagory=models.ForeignKey(Project_catagory,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=True,blank=True)
    project_image1=models.ImageField(upload_to=getFileName,null=True,blank=True)
    project_image2=models.ImageField(upload_to=getFileName,null=True,blank=True)
    project_image3=models.ImageField(upload_to=getFileName,null=True,blank=True)
    
    def __str__(self):
        return self.name

class about_us(models.Model):
    Subject=models.CharField(max_length=10,null=True,blank=True)
    about_us_home=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.Subject

class client_logo(models.Model):
    Client_logo_name=models.CharField(max_length=50,null=True,blank=True)
    client_logos=models.ImageField(upload_to=getFileName,null=True,blank=True)

    def __str__(self) :
        return self.Client_logo_name

class rating(models.Model):
    stars=models.IntegerField(null=True,blank=True)

class Review(models.Model):
    username = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return f"{self.username} - {self.rating}"