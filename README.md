# **Travel Stories API**

Travel Stories is a social networking platform targeted towards everyone that loves to travel, want to share their adventures with others and keep track of feature destinations to visit. 

Travel Stories offers a spaces for users to document and share their travel experiances as stories. All stories can be liked and commented on so that the user can engage with the community. A story can also be saved, which will then connect it to a user bucket list. In the bucket list all feature destinations that the user wants to visit can be listed along with notes of what activites the users wiches to do at that location. This enables the user to document and organise their travel plans and stay connected to their favorite content creators. 

This project was built in two parts. This app makes up the back-end API, powered by Django REST Framework. The front-end was built with React and the live site can be found [here](https://travel-stories2-eeac1d39adbb.herokuapp.com/).

[Link to the live Travel Stories API](https://travel-stories-api2-af9d4146e908.herokuapp.com/)

[Link to the Back End API Repo](https://github.com/sarasm93/travel-stories-api2)

![An image of the deployed front-end app on different screen sizes](documentation/readme-intro.png)

## **Project goals**
The main objective with the platform is to inspire to travel, by engage people to share their travel stories, meet new people, discover new places to visit and in the end - travel more!

### **User goals**
A user can have more than one goal when visiting the platform. And one user may have different goals compared to another. Some users may only want to look at stories and be inspired. Some users may want to be inspired but also inspire others by sharing their own tavel stories and use the platform to communicate with other travelers by commenting and liking their stories. Some users might want to document their insipriation by saving a story from another user, build a bucket list and use the saved story as a tag on a bucket list item.

### **Site owner goals**
The goal is to provide the users with a reliable platform and a good user experiance that doesn´t take a way any of the inspiration and joy provided by the travel stories. The site should encurage continued user interactions and be of high quality. To make this possible the site should be intuitive, accessible and well structured. 

## **UX**

### **User Stories**
- As a admin I can create a ERD diagram so that I can easily work with the database and see how data is connected.
- As a admin I can add authentication and authorization so that only the owner of a profile can edit it.
- As a admin I can create the travel story app so that users can create a travel story to share with others, and so that travel story data can be saved, displayed and managed.
- As a admin I can create the comment app so that users can comment on travel stories and so that comment data can be saved, displayed and managed.
- As a admin I can create the like app so that users can like travel stories, and so that like data can be saved, displayed and managed.
- As a admin I can create the save app so that users can save a travel story that they like, and so that save data can be saved, displayed and managed.
- As a admin I can create the destination app so that users can create a bucket list with saved destinations as items, and so that destination data can be saved, displayed and managed.
- As a admin I can create the profile app so that users can create an account, and so that user data can be saved, displayed and managed.
- As a user I can add mh own story as a tag on a destionation so that I can use the story as a reminder of how great my last trip to a destination was and what I did.
- As a admin I can create a readme.md file so that anyone interested in the project can read about the project and the development of it.
- As a admin I can deploy/distribute my app so that everyone else can see it and use it.

## **Agile Development**
The app was built using an agile approach, with a GitHub project board, milestones, labels and issues. The GitHub project board can be found [here](https://github.com/users/sarasm93/projects/11). Everthing that needed to be done to develop this app was divided into user stories with tasks. All user stories mentioned above were created with GitHub issues. The agile development iterations are created with milestones, i.e. all issues were linked to a milstone. Labels have been used to priorities which issues are most important by create labels namned "must have", "should have", "could have" and "wont´t have". 

## **Data models and database**
The ERD diagram shown below was made with [Lucid Charts](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier2_mixed_search_brand_exact_&km_CPC_CampaignId=1520850463&km_CPC_AdGroupID=57697288545&km_CPC_Keyword=lucid%20charts&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433237648&km_CPC_TargetID=kwd-64262996435&km_CPC_Country=9062397&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=CjwKCAjwwb6lBhBJEiwAbuVUSp5GJupY-n0T0KIxQyga5tojqyWYZIbI3dXIpvdCgxbxCcPYgxb-_RoCMJAQAvD_BwE) and shows the structure of the PostgreSQL database used in this project. It visualises the types of data models required and the relationships between them. 

Django AllAuth was used for the user model and user authentication system.

The profile model was created so the user can create and save stories and create bucket list destination items that can be edited and deleted. 

The destination model holds all information about at destination item that a user can add to it´s bucket list, such as creator of the item, destination, activities, story tags and priority. 

The travel story model holds all information about a story, such as creator, title, destination, content, image and creation date.  

The save model makes it possible for the user to connect a bucket list destination item to a travel story by saving the story. 

The like model holds all information about a like, i.e. which user has made it and on which story. 

The comment model holds all information about a comment - which user has made it and on which story, the content of the comment and the creation date. 

![ERD diagram showing the project data models and the relationships between them - image 1](documentation/models1.png)
![ERD diagram showing the project data models and the relationships between them - image 2](documentation/models2.png)

## **Features**
The Travel Stories API consists of six apps - stories, comments, likes, saves, destinations and profiles. Each app endpoint can be reached by adding the corresponding endpoint URL to the main URL https://travel-stories2-eeac1d39adbb.herokuapp.com/. Destinations data is only accessible for the owner of the destionation data, through the front end website. The api superuser can access and manage the back end by logging in to the backend through the Django adminsite. 

## **Testing**
The site has been tested so that it works on different browsers. It has been tested on Google Chrome, Microsoft Edge, Firefox and Samsung Internet.

### **Manual testing**


### **Validator testing**
The Python code has been validated with the [CI Python Linter](https://pep8ci.herokuapp.com/). 


### **Resolved problems and bugs**
Kuuuuuuuuuuuuuunde inte nå destinations data från front end - visade sig att jag kopplat destination modelen fel... Skulle kopplas till User, inte Profile. Detta orsakade ett annat fel, dvs. att filtret för denna model inte fungerade, dvs. att det inte gick att filtrera på owner av destinations. Så fort probnlemet med modellen hade lösts så kunde ett fungerande filter läggas till. 

## **Deployment**
The back-end API app was deployed to Heroku from GitHub with the following steps:

1. Create an external database using [ElephantSQL](https://www.elephantsql.com/). When logged in to your ElephantSQL account, click on “Create New Instance”, choose a plan and give it a name. Then select a region, click the "Review" button to view the details for your plan and finally click "Create instance". 

2. Create a Heroku app by logging in to your Heroku account. Click the "New" button in the top right corner and then "Create new app". Give it a name, choose a region and then click the "Create app" button. 

3. Attach the external database. 
	- In the Heroku app that you created, you need to create environment variables, called Config Var at Heroku. This is done under the "Settings"-tab in the top menu. Click the tab. On the settings page scroll down to the Config Vars-section and click the "Reveal Config Vars"-button. 
	- Go back to your ElephantSQL account, and from the dashboard click on the database instance name for the project. When in the project instance, copy the ElephantSQL database url by clicking on the copy icon. In the Config Vars section in at Heroku, add this url to the VALUE field and add DATABASE_URL to the KEY field. 
	- In your workspace, create a file called env.py in the top level directory. Add env.py to the list of files in your gitignore file. In the env.py file, import the os library and add the ElephantSQL DATABASE_URL. Below that, also add `os.environ['DEV'] = '1'`. You also need to choose and add a SECRET_KEY value like this: `os.environ.setdefault('SECRET_KEY', 'your-secret-key')`. The key also needs to be added as a config var at Heroku. Add SECRET_KEY in the KEY field and the secret key in the VALUE field. 

4. Set up Cloudinary by installing it and the Pillow library. When logged in to your account on Cloudinary, copy your url on the Cloudinary dashboard and paste it into the env.py file, like you did with the SECRET_KEY and DATABASE_URL. Then go to Heroku and add the url to the config vars. Add CLOUDINARY_URL in the KEY field and your url in the VALUE field. If you deploy your app early on in the project process, also add DISABLE_COLLECTSTATIC in KEY field and 1 to VALUE field (remove it before final deployment). Add Cloudinary Libraries to the list of installed apps in settings.py. Then also add static files settings in settings.py to tell Django to use Cloudinary. Type:
	
```
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

5. Preparation in your IDE:
- Go to settings.py. Start by adding:
```
import os

if os.path.isfile("env.py"):
    import env
```

- Install django rest: pip3 install djangorestframework. Install the django-rest-auth library and django-all-auth (pip3 install 'dj-rest-auth[with_social]') and add the following code to the list of installed apps:

```
'rest_framework',
'rest_framework.authtoken',
'dj_rest_auth',
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
```

- Add a SITE_ID setting and set it to 1. s
- Go to your app urls.py file and add the following code to the urlpatterns list: 

```
path('api-auth/', include('rest_framework.urls')),
path('dj-rest-auth/', include('dj_rest_auth.urls')),
path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
```
- Go back to settings.py and 
- To connect to the database created, install dj_database_url and psycopg2 with the following command: `pip3 install dj_database_url==0.5.0 psycopg2`. Import dj_database_url to your settings.py file. In the settings.py file, remove the default database configuration and add this instead (the print message at the end is to confirm that connection has been made with the database):

```
 if 'DEV' in os.environ:
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
 else:
     DATABASES = {
         'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
     }
     print('Connected!')
```
- Then remove the default secret key and replace it with this code: SECRET_KEY = os.getenv('SECRET_KEY'). I.e. use the environment variable instead. 
- Temporarely comment out `os.environ['DEV'] = '1'` in your env.py file to make it possible for your IDE to connect to the database. 
- Save all files and make a dry run of your migrations in the terminal with this command: `python3 manage.py makemigrations --dry-run`. If you see the `Connected!` message in the terminal the connection to the database works, which means you can remove the `Connected!` print statement and make the migrations with these commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
- Then create a superuser for the database with the command `python3 manage.py createsuperuser` and the follow the steps. 

6. To confirm that the data has been created in your database on ElephantSQL, go to ElephantSQL and the page for your database. Click on "BROWSER" in the left hand side navigation bar. Click the "Table queries" button and select auth_user. Then click "Execute”. When you click the button your superuser details should be displayed. If they are, then it´s confirmed that your tables have been created and data can be added. 

7. Install gunicorn, which is needed for the project to run on Heroku. Go to your workspace again and in the terminal write the command: pip3 install gunicorn django-cors-headers. Then you need to create a requirements.txt file: pip3 freeze --local > requirements.txt

8. Create a file on the top level directory called Procfile and add this code: 
```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn drf_api.wsgi
```

9. In the settings.py file, add corsheaders to installed apps and at the top of the middleware add `corsheaders.middleware.CorsMiddleware`. Also add your Heroku hostname to allowed hosts, together with your local host. 

10. Next, set the ALLOWED_ORIGINS for the network requests and anable sending cookies in cross-origin requests. Under the middleware list in settings.py, add:
```
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

CORS_ALLOW_CREDENTIALS = True
``` 

11. Change the DEBUG value from True to `'DEV' in os.environ`, which means that DEBUG will be True if the DEV environment variable exists but False it´s not i.e. in production. Go to env.py and comment DEV back in again. Then save all files, add, commit and push your code to GitHub.

12. Add JWT tokens functionality
- Install the djangorestframework-simplejwt package. With the below code, use the DEV value you created above to differentiate between development and production mode: 

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )], }
```
- Add JWT_AUTH attributes with the below code. This will allow front end app and the API deployed to different platforms and the cookies will not be blocked. 

```
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
```

13. Set the JSON Renderer by adding:

```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```

14. Update the requirements.txt file. Then go to Heroku and the dashboard for your app. Scroll to the top menu and click the "Deploy"-tab. Scroll to the "Deployment method"-sction and select GitHub. In the "Connect to Github"-section that shows up, click on "Connect to GitHub". When the connecting is done you will see a search bar where you can search for the repository name. Click on the "Connect"-button that shows up when Heroku has found your repository. Scroll further down and choose either to deploy automatically by clicking the "Enable Automatic Deploys" or deploy manually by clicking the "Deploy Branch"-button. When the deployment is finished you can go to the "Settings"-tab again and scroll down to the "Domains"-section where you can find the link to your deployed app. To open your app you can also click the "Open app" button. When you open your app, you root message should show up.

15. Fix bug in dj-rest-auth
- The bug won´t allow users to log out. The issue is connected to the samesite attribute. To fix it create a views.py file in your app folder and import JWT_AUTH with this code:

```
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
```
- Then, write a new logout view that sets both jwt tokens to empty strings and also pass samesite=JWT_AUTH_SAMESITE. Add this code:

```
@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
```
- Include the logout view in urls.py by importing it and add it to the urlpatterns list above the default dj-rest-auth urls. Then push the code to GitHub, and if you have chosen to manually deploy your app at Heroku make sure you deploy it again. 
- In order to use the API with the front end app, add two new environment variables. Go to your allowed hosts in settings.py and copy the string/link for your Heroku app. Go to your app at Heroku, and then the settings tab. Add a config var with the key value of ALLOWED_HOST and paste in the string you copied from settings.py. Go back to settings.py and replace the heroku link with `os.environ.get('ALLOWED_HOST')`.
- To add the next variable, you need to follow the below steps. They are adapted to work with Gitpod as this app was developed with Gitpod. The steps will make your app more secure by affecting how Gitpod works and let your workspace be connected to our API when gitpod rotates the workspace URL.
- In your settings.py file add: `import re`
- Then, in the `if 'CLIENT_ORIGIN' in os.environ:...` code, replace the else statement and body with the following code:

```
if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```
- Go to your deployed front end app and copy the url for the app. Then go back to Heroku and add a config var with the key CLIENT_ORIGIN and paste in the url you just copied as value. Then you need to go to your development environment for your front end app and copy the url for the development version of that app. At Heroku, add one more config var with the key CLIENT_ORIGIN_DEV and paste in the copied url for the development version. Then push the code to GitHub, and if you have chosen to manually deploy your app at Heroku make sure you deploy it again. 

## **Technologies, Languages, Frameworks, Libraries, Programs and Sites used**

### **Languages**
- Python 

### **Frameworks**
- [Django Rest Framwork](https://www.django-rest-framework.org/) - main Python web framework used to develop this API
- [Django](https://www.djangoproject.com/)

### **Extensions**
- [JSONView](https://chrome.google.com/webstore/detail/jsonvue/chklaanhfefbnpoihckbnefhakgolnmc) - to view correctly formatted JSON in the browser
- [ES7 React/Redux/GraphQl/React-Native](https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets) - snippets that allow fast typing of code with shortcuts

### **Software and Sites**
- [Git and GitHub](https://github.com/)- version control and as agile tool
- [Cloudinary](https://cloudinary.com/) - image hosting and management
- [ElephantSQL](https://www.elephantsql.com/) - free database service that hosts the PostgreSQL database for this project 
- [Lucidchart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier2_mixed_search_brand_exact_&km_CPC_CampaignId=1520850463&km_CPC_AdGroupID=57697288545&km_CPC_Keyword=lucidchart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433237648&km_CPC_TargetID=kwd-33511936169&km_CPC_Country=9062397&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=Cj0KCQjwnMWkBhDLARIsAHBOftrLqk9mpk7BpbSpfCB82TCw4CoQ4k4-1IqLKE5G5i3Cs5Q-3_ysvx4aAtpTEALw_wcB) - create database model schema

### **Other dependencies**
- [django-rest-auth](https://pypi.org/project/django-rest-auth/) - provides a set of REST API endpoints for Authentication and Registration
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication
- [Psycopg2](https://pypi.org/project/psycopg2/) - Python-PostgreSQL database adapter, in order to use Python code (instead of SQL) to do Postgres commands 
- [dj_database_url](https://pypi.org/project/dj-database-url/) - method returning a Django database connection dictionary
- [Pillow](https://pypi.org/project/Pillow/8.2.0/) - Python Imaging Library 
- [urllib3](https://pypi.org/project/urllib3/1.26.15/) - user-friendly HTTP client for Python used by many components in Python, such as requests and pip
- [PyJWT](https://pypi.org/project/PyJWT/) - JSON Web Token implementation in Python
- [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server acting as the web server for the project

## **Credits**
This project was developed as a portfolio submission project as part of [Code Institute's](https://codeinstitute.net/se/) Diploma in Full Stack Software Development and Code Institute's walkthrough project [Moments](https://github.com/Code-Institute-Solutions/moments) and the [api setup-project for Moments](https://github.com/Code-Institute-Solutions/drf-api) has been used as a tempalates for this project. I have then made customizations and expanded it by adding new features and functionality. 

I used the readme.md file for my [Cinerama Cinema project](https://github.com/sarasm93/cinerama-cinema) as base for the readme.md file for this project and used some text from it as well. Inspiration for the readme was also gotten from the [Garden Diaries project](https://github.com/EmelieMarkkanen/p5-garden-diary/tree/main#features) and the [Gear Addict project](https://github.com/Matthew-Hurrell/gear-addict#components).

[Lonely planet](https://www.lonelyplanet.com/) has partly been used to get ideas about what to include in this project.

Code fomr this [Stackoverflow page](https://stackoverflow.com/questions/1117564/set-django-integerfield-by-choices-name) was used in the destination model so that priority choices could be display when creating a destination.
 
## **Acknowledgements**
I want to thank Code institute and my mentor Antonio Rodriguez for all the valuable support and help during the development of this project.