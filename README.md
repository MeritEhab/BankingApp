# BankingApp
A simple application to manage (CRUD) users and their bank account data (IBAN)

### Installation

Create a virtualenv for the project, and run:

```pip install -r requirements.txt```

Run python ```manage.py migrate```

### Usage

To make an account run 
```python manage.py createsuperuser```

Then run ```python manage.py runserver```

Head for homepage
http://localhost:8000/

This application enables admin users to login with google account, in order to do this follow these steps:

- Go to the Google Google Developers Console and then click on create button.

- Enter project name e.g 'Django App'. Wait for a few seconds your project should be created

- On the right side there is credentials tab, select it.

- Click on Create Credentials then OAuth Client ID. Select the application type Web app, Give any name of your choice and Enter any name in 'Product name shown to users' under OAuth Consent Screen tab.

- Enter the following in Authorized redirect URIs:
  http://localhost:8000/auth/complete/google-oauth2/
- Now click on library under the APIs and services tab and then search for google+, in the search results click on Google+ API and then click Enable.

- Now, Copy the Client ID and Client Secret Under settings.py

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY =''  #Paste CLient Key

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '' #Paste Secret Key


