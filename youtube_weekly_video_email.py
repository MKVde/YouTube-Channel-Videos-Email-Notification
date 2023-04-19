# This Python script code sends an email containing links, title and thumbnail to all the videos uploaded to a specified YouTube channel in the past week

import requests
import smtplib
import os
import google.auth
import google.auth.transport.requests
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from google.oauth2.credentials import Credentials


# Set up YouTube Data API
API_KEY = 'YOUR_API_KEY' # you need to create a Google Cloud Platform (GCP) project and enable the YouTube Data API in the project. Once you have done this, you can create an API key in the GCP Console and copy it into the API_KEY variable in the script.
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
channel_id = 'channel_id'  # Channel ID of the YouTube channel you want to monitor: Ex:'UCBJycsmduvYEL83R_U4JriQ' this is channel ID for MKBHD

# Set up email parameters
sender_email = 'YOUR_SENDER_EMAIL'
password = 'YOUR_EMAIL_PASSWORD'
recipient_email = 'YOUR_RECIPIENT_EMAIL'

# Set up time interval
time_interval = 7 # days, you can change the preiod of time you want

# Set up message content
msg = MIMEMultipart()
msg['Subject'] = 'New videos uploaded in the past week, check it'
msg['From'] = sender_email
msg['To'] = recipient_email

# Get the date and time of 7 days ago
seven_days_ago = (datetime.now() - timedelta(days=time_interval)).strftime('%Y-%m-%dT%H:%M:%SZ')

# Set up YouTube API request parameters
params = {
    'key': API_KEY,
    'channelId': channel_id,
    'part': 'snippet',
    'type': 'video',
    'order': 'date',
    'publishedAfter': seven_days_ago,
    'maxResults': 50
}


# Send a GET request to the YouTube Data API to get the videos uploaded in the past week
url = f'https://www.googleapis.com/youtube/{API_VERSION}/search'
response = requests.get(url, params=params, timeout=140)
json = response.json()


# Loop through the videos and add their links to the email body
if 'items' in json:
    for video in json['items']:
        video_url = f'https://www.youtube.com/watch?v={video["id"]["videoId"]}'
        video_title = video['snippet']['title']
        video_thumbnail_url = video['snippet']['thumbnails']['medium']['url']
        body = f'<p><a href="{video_url}">{video_title}</a></p>'
        msg.attach(MIMEText(body, 'html'))

        # Download and attach the video thumbnail
        thumbnail_image_data = requests.get(video_thumbnail_url).content
        image = MIMEImage(thumbnail_image_data)
        msg.attach(image)

# Send the email
if 'items' in json:
    with smtplib.SMTP("smtp.office365.com", 587) as server: # Here I use outlook email you can change it if you want to use different email service
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
    print(f'Successfully sent email with {len(json["items"])} videos.')
else:
    print('No videos found.')

