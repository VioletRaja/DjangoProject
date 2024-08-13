from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .import views
from django.contrib import messages
import requests
from .models import *
from googleapiclient.discovery import build
from django.http import JsonResponse
from django.shortcuts import render
import googlemaps



def send_feedback_email(email, message,request):
    subject = 'Thanks for Your Feedback'
    context = {
        'message': message,
    }
    html_content = render_to_string('email.html', context)
    text_content = strip_tags(html_content)  # Strip HTML tags for plain text email
    
    email = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    email.attach_alternative(html_content,"text/html")
    
    email.send()
    messages.success(request,"Thanks For you'r feedback")
    # message = f'Thank you for your feedback: {message}'
    # from_email = settings.EMAIL_HOST_USER
    # recipient_list = [email]

    # send_mail(subject, message, from_email, recipient_list)




# Your Google API key
API_KEY = 'AIzaSyDBE0aKYvWyfVQh2nEzsDfkeDYscYkHYdw'


def get_place_reviews(place_id):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?placeid={place_id}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'result' in data and 'reviews' in data['result']:
            return data['result']['reviews']
    return []

def fetch_reviews(request): 

    api_key = 'settings.GOOGLE_API_KEY'
    place_id = 'settings.GOOGLE_PLACE_ID'

    # gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
    # place_details = gmaps.places().get(placeid=place_id).execute()

    # reviews = place_details.get('reviews', [])
    # rating_counts = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}

    # for review in reviews:
    #     rating_counts[review['rating']] += 1
    #     # Save the review to the database
    #     Review.objects.create(
    #         username=review['author_name'],
    #         rating=review['rating'],
    #         comment=review['text']
    #     )

    # return JsonResponse({'reviews': reviews, 'rating_counts': rating_counts})











# def reviews_view(request):
#     place_id = 'ChIJlVDAZWNZqDsRyWXjxw9bLwM'  # Replace with the actual Place ID
#     reviews = get_place_reviews(place_id)
#     print(reviews)
#     return render(request, 'index.html', {'reviews': reviews})