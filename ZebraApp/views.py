from django.shortcuts import render,redirect,HttpResponse
from . models import * 
from django.contrib import messages
from django.http import QueryDict
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from .utils import *
from django.core.mail import send_mail
from django.conf import settings
import googlemaps
from django.db.models import Avg
from .models import rating
from  django.core import serializers

# from .forms import FeedbackForm

# Create your views here.
# "averageRating":average_rating,"range": rating_range,"RV":reviews_var,"NV":name_var

def index(request):
    Home_top_video=Home_source.objects.all()
    load_service_pic=services_pics.objects.filter(status=0)
    home_url_Z=home_url.objects.all()
    about_us_var=about_us.objects.all()
    client_logo_var=client_logo.objects.all()
    reviews = Review.objects.all()
 
    place_id="ChIJlVDAZWNZqDsRyWXjxw9bLwM"
    fetch_reviews(request)
    get_place_reviews(place_id)
    def reviews_view(request):
     place_id = 'ChIJlVDAZWNZqDsRyWXjxw9bLwM'  # Replace with the actual Place ID
     
     return render(request, 'index.html', {'reviews': reviews})
    reviews = get_place_reviews(place_id)
    
   
    return render(request,'index.html',{"LSP":load_service_pic,"HTV":Home_top_video,"URL":home_url_Z,"AU":about_us_var,"CL":client_logo_var,'reviews': reviews})

def service(request):
    service_header=Service_page.objects.all()
    return render(request,'service-detail.html',{"SP":service_header})



def projects(request):
    
    project_header_var=projects_model.objects.all()

    pac_items = Project_catagory.objects.all()
    

    psc_items = Project_site_pics.objects.all()

    


    context={

        'PAC': pac_items,
        'PSP': psc_items,
        'PH1':project_header_var,
  
        } 
    
    return render(request, 'projects.html',context)


def contact(request):
    return render(request,'contact.html')

def addrec(request):
    a=request.POST['username']
    b=request.POST['phone']
    c=request.POST['company']
    d=request.POST['email']
    e=request.POST['message']
    mem=ContactUs(username=a,phone=b,company=c,email=d,message=e)
    mem.save()
    if request.method=='POST':
        name=request.POST.get('username')
        email = request.POST.get('email') 
        message = request.POST.get('message')
        phone = request.POST.get('phone') 

        send_feedback_email(email, message,request)
        
        subject = 'Zebra New Feedback'
        message = f'Name: {name}\nEmail: {email}\nMessage: {message}\nPhone: {phone}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]

        send_mail(subject, message, from_email, recipient_list)
        
        return redirect("/contact")
        
    return render(request,'contact.html')
    
def addrec_home(request):
    a=request.POST['username']
    b=request.POST['phone']
    c=request.POST['company']
    d=request.POST['email']
    e=request.POST['message']
    mem=ContactUs(username=a,phone=b,company=c,email=d,message=e)
    mem.save()
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        message=request.POST.get('message')
        phone=request.POST.get('phone')
        # messages.success(request,"Thanks For you'r Feedback !") 

        send_feedback_email(email,message,request)
        subject = 'Zebra New Feedback'
        message = f'Name: {name}\nEmail: {email}\nMessage: {message}\nPhone: {phone}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]
        
        send_mail(subject, message, from_email, recipient_list)
        
        return redirect("/")
    else:

        messages.error(request,"Can't upload your feedback")
        return render(request,'index.html')
    

# views.py
# def submit_feedback(request):
    # if request.method == 'POST':
        # Extract form data from request.POST
        # name = request.POST.get('name')
        # email = request.POST.get('email')

        # message = request.POST.get('message')
        # subject = 'New Feedback Submission'
        # message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        # from_email = settings.EMAIL_HOST_USER
        # recipient_list = [settings.EMAIL_HOST_USER]  # Replace with your recipient email address
        
        # send_mail(subject, message, from_email, recipient_list)

        # Redirect or render a success page
        # return HttpResponse('Feedback submitted successfully. Thank you!')

    # Handle GET request if needed
    # return render(request, 'feedback_form.html')
   








#Using forms.py
# def feedback_view(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             # Send email notification
#             subject = 'New Feedback Submission'
#             message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
#             from_email = settings.EMAIL_HOST_USER
#             recipient_list = [settings.EMAIL_HOST_USER]  # Send notification to yourself

#             send_mail(subject, message, from_email, recipient_list)

#             # Optionally, you can redirect or render a success page
#             return render(request, 'feedback/thanks.html')
#     else:
#         form = FeedbackForm()

#     return render(request, 'feedback/form.html', {'form': form})
    


# def send_feedback(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')  # Assuming email is submitted via a form
#         message = request.POST.get('message')  # Assuming feedback message is submitted via a form

#         # Send email
#         send_feedback_email(email, message)

#         # Optionally, you can redirect or render a success page
#         return render(request, 'contact.html')

#     return render(request, 'contact.html')