
# YouTube Channel Videos Email Notification


This script sends an email once a week (you can change the duration) with links to all the videos on a specified YouTube channel that were uploaded in the past week (default).

## Installation

To use this script, you will need to have Python 3 installed on your computer. You will also need to install the following packages:
```bash
  requests
  os
  google-auth
  google-auth-oauthlib
  google-auth-httplib2
```
You can install these packages using pip by running the following command:

```bash
pip install requests google-auth google-auth-oauthlib google-auth-httplib2 
```
## Usage/Examples


To use this script, you will need to set the following variables:

- API_KEY: Your YouTube Data API key. ( You need to create a Google Cloud Platform (GCP) project and enable the YouTube Data API in the project. Once you have done this, you can create an API key in the GCP Console and copy it into the API_KEY variable in the script ).

- API_SERVICE_NAME: The name of the YouTube Data API service (which is "youtube").
- API_VERSION: The version of the YouTube Data API that you want to use (which is "v3").
- channel_id: The ID of the YouTube channel that you want to monitor.
- sender_email: The email address that you want to send the weekly video email from.
- recipient_email: The email address that you want to send the weekly video email to.
- password: The password for the email account that you want to send the weekly video email from.
- time_interval: The time interval (in days) that you want to use to determine which videos were uploaded in the past week.

Once you have set these variables, you can run the script by running the following command:

```Way
youtube_channel_videos_email_notification.py
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

This script is free and open source software, released under the MIT License. You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of this software, subject to the conditions of the license.
## FAQ

#### The script sends the email using the SMTP protocol 

- This script sends an email once a week (default) with links to all the videos on a specified YouTube channel.

#### How do I set up and use the script?

- You'll need to obtain an API key from the Google Cloud Console and specify the API key, YouTube channel ID, sender email, recipient email, email password, and time interval in the script.
- You can then run the script to send the weekly  (default) email.

#### Can I customize the email message?

- Yes, you can customize the email message by modifying the msg object in the script. You can change the email subject, sender email, recipient email, and the email body. The email body is constructed by looping through the videos returned by the YouTube API and adding their links to the email body.

#### Can I change the time interval for the weekly (default) email?

-  Yes, you can change the time_interval variable in the script to the number of days you want to go back to check for new videos. For example, if you want to check for new videos uploaded in the past 14 days, you can set time_interval to 14.

#### What email service can I use with this script to send the weekly (default) email updates?

- You can use any email service that supports the SMTP protocol, such as Gmail, Outlook, Yahoo, or your own custom email server. In the script, the email is sent using the SMTP server of Office 365, but you can modify the script to use a different SMTP server if needed. Note that some email services may require you to enable "less secure app access" or generate an "app password" to use their SMTP server from a script like this. Make sure to check your email service's documentation for instructions on how to set up SMTP access.

- Use Outlook (Office 365) becase it is not require "less secure app access"

#### How can I run the script automatically on a schedule?

- You can use a cron job or a scheduled task to run the script automatically on a schedule. For example, you can set up a cron job to run the script every Monday at 9:00 AM.

#### Can I use this script for commercial purposes?

- Yes, you can use this script for commercial purposes, but please be aware that you may need to comply with YouTube's terms of service and data usage policies.





## Documentation


YouTube Channel Videos Email Notification Script:

### Overview:

This script periodically sends an email with links to the videos uploaded in the past week (default) to a specified YouTube channel. It uses the YouTube Data API to retrieve the list of videos and the SMTP protocol to send the email. You can configure the script to use your own API key, email credentials, and email content.

### Requirements:
To use this script, you will need:

- A Google Cloud project with the YouTube Data API enabled and an API key.
- A valid email account with SMTP access, such as Gmail, Outlook, or your own custom email server.
- Python3 installed on your system with the required modules (requests,  google-auth, google-auth-oauthlib, google-auth-httplib2) installed.

### Usage:

**1. Copy or download the script from GitHub to your local machine.
**
**2. Open the script file (youtube_videos_email_notification.py) in your favorite code editor or IDE.
**
**3. Here are the steps to create a YouTube Data API key:
**
- Go to the Google Cloud Console (https://console.cloud.google.com/) and create a new project or select an existing project.

- In the project dashboard, navigate to the APIs & Services section and click on "Dashboard".

- Click on the "+ ENABLE APIS AND SERVICES" button at the top of the page.

- Search for "YouTube Data API" in the search bar and select it from the list of APIs.

- Click on the "Enable" button to enable the API.

- Navigate to the "Credentials" section of the APIs & Services dashboard and click on "+ CREATE CREDENTIALS".

- Select "API key" from the list of options.

- Choose the appropriate restrictions for your API key, such as IP address restrictions or application restrictions.

- Copy the API key and use it in your script to make requests to the YouTube Data API.
- For more information (https://blog.hubspot.com/website/how-to-get-youtube-api-key), YouTube video (https://youtu.be/yuM7KH-JLu8)

4. Update the following variables at the beginning of the script to match your configuration:

- API_KEY: Your Google Cloud project API key.
- API_SERVICE_NAME: The name of the API service to use (always "youtube").
- API_VERSION: The version of the API to use (currently "v3").
- channel_id: The ID of the YouTube channel you want to monitor (e.g., "UCBJycsmduvYEL83R_U4JriQ" for MKBHD).
- sender_email: Your email address.
- recipient_email: The email address of the recipient.
- password: Your email password (or app password if required).
- time_interval: The time interval (in days) for which to retrieve the videos (default is 7 days) you can change it.
- msg['Subject']: The subject of the email message.

5. Save the changes to the script file.

6. Run the script from the command line by typing python: youtube_videos_email_notification.py.

7. The script will retrieve the list of videos uploaded in the past 'time_interval' days to the specified YouTube channel and send an email to the recipient with links to these videos. If no videos are found, the script will send an email with a message indicating that no videos were found.

---

### Code Explanation: The script is divided into several parts, each responsible for a specific task. Here's a brief overview of the main parts of the code and their purpose:

1. Importing the required modules:
The first section of the code imports the required Python modules for the script to run. These include:

• requests: This module is used to send HTTP requests to the YouTube Data API.

• smtplib: This module is used to send the email message using the SMTP protocol.

• datetime: This module is used to manipulate dates and times.

• os: This module provides a way to interact with the file system and is used here to load the environment variables.

• google.auth: This module is used to authenticate with the YouTube Data API using OAuth 2.0.

• google.auth.transport.requests: This module provides the necessary functionality to authenticate with the API using a Python requests object.

• googleapiclient.discovery: This module provides a simple way to interact with the YouTube Data API.

• googleapiclient.errors: This module provides error handling functionality for the YouTube Data API.

• google.oauth2.credentials: This module is used to load and store the OAuth 2.0 credentials.

• google.oauth2.service_account: This module is used to authenticate with the YouTube Data API using a service account.

2.	Configuring the YouTube Data API: The second section of the code sets up the necessary parameters to use the YouTube Data API. These include:

• API_KEY: Your Google Cloud project API key.

• API_SERVICE_NAME: The name of the API service to use (always "youtube").

• API_VERSION: The version of the API to use (currently "v3").

• channel_id: The ID of the YouTube channel you want to monitor (e.g., "UCBJycsmduvYEL83R_U4JriQ" for MKBHD).

3. Configuring the email parameters: The third section of the code sets up the parameters for the email message. These include:

• sender_email: Your email address.

• recipient_email: The email address of the recipient.

• password: Your email password (or app password if required).

• msg['Subject']: The subject of the email message.

4. Configuring the time interval: The fourth section of the code sets up the time interval for which to retrieve the videos (default is 7 days), you can change it.

5. Setting up the message content: The fifth section of the code sets up the email message content. This includes:

• The email body: This is the main content of the email and includes the title and link of each video uploaded to the YouTube channel.

• The video thumbnail images: This section retrieves the thumbnail image of each video and attaches it to the email message.

6. Retrieving the videos from the YouTube Data API:
The sixth section of the code retrieves the list of videos uploaded in the past time_interval days to the specified YouTube channel. It does this by sending a GET request to the YouTube Data API and parsing the response to extract the relevant information.

7. Sending the email: 

The final section of the code sends the email message using the SMTP protocol. It first establishes a connection with the SMTP server using the provided email credentials, then sends the email message to the recipient.
 

-------------
### Example:
Here is example of how to use this script:

I recommend using Outlook instead of Gmail or Yahoo because you won't need to enable the "Less secure apps" feature.

- Example 1: Using the script with Gmail:

    Assuming you have a Gmail account, you can use the script to send an email notification to yourself with links to the videos uploaded in the past week to a specific YouTube channel.

    To use the script with Gmail, follow these steps:

    - Enable "Less secure apps" in your Google account security settings (https://myaccount.google.com/security).
    - Set up the necessary parameters in the script file, including your API key, channel ID, Gmail credentials, and email content.
    - Run the script from the command line by typing python youtube_videos_email_notification.py

* Here's an example of the email message sent by the script:

    " Subject: New videos from MKBHD

    Hi,

    Here are the videos uploaded in the past 7 days by MKBHD:

    1. Title: A Hidden Google Assistant Feature!
    Link: https://www.youtube.com/watch?v=1234567890
    Thumbnail: https://image-1.jpg

    2. Title: The ROG Phone 7 Ultimate is Just Ridiculous!
    Link: https://www.youtube.com/watch?v=0987654321
    Thumbnail: https://image-2.jpg

    3. Title: The Rivian R1S Is... The Best SUV Ever?
    Link: https://www.youtube.com/watch?v=2468101214
    Thumbnail: https://image-3.jpg

    4. Title: The AI Assistant Battle! (2023)
    Link: https://www.youtube.com/watch?v=1357902468
    Thumbnail: https://image-4.jpg

    5. Title: This Voice is Entirely AI...
    Link: https://www.youtube.com/watch?v=7539514568
    Thumbnail: https://image-5.jpg

    6. Title: The Smartphone Awards Midseason 2023!
    Link: https://www.youtube.com/watch?v=1593574682
    Thumbnail: https://image-6.jpg

    7. Title: Dope Tech: Better than Expected!
    Link: https://www.youtube.com/watch?v=7894561230
    Thumbnail: https://image-7.jpg

    

    If you have any questions or concerns, feel free to reply to this email.

    Best regards,
    YouTube Channel Videos Email Notification Bot. "


### Conclusion:
This script provides a simple and automated way to receive email notifications for new videos uploaded to a YouTube channel. By following the instructions in this documentation and customizing the script to your needs, you can easily set up this functionality for your own YouTube channels or for those of your clients or collaborators.    

    
