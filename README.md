<div align="center">
<h1>Django Job Portal Project</h1>

> Still in Development

[View Project online](https://django-job-portal-project.onrender.com/)

</div>

</br>

<details>
<summary>Project Deployment Guide</summary>

## Project deployment:

- Add those in requirements.txt
    ```text
    Django==5.0.4
    gunicorn==21.2.0
    pillow==10.3.0
    whitenoise==6.6.0
    ```
- Go to `settings.py` and modify as below:
    ```python
    DEBUG = False
    ALLOWED_HOSTS = ["*"] # This can be also set as default domain after deployment
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'whitenoise.runserver_nostatic', # This must be added before 'django.contrib.staticfiles'
        'django.contrib.staticfiles',
        'portfolioapp',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware', # This must be added here after SecurityMiddleware & SessionMiddleware
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    # Add those at the end
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles/'
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
    ```
- Now go to render and select web service from New
- Select Github repo of the project
- Now in project setting page write Project Name (unique)
- Select Region, Branch
- Set Build command `pip install -r requirements.txt`
- Set start command `gunicorn jobProject.wsgi:application` # here jobProject is the project name
- Choose Instance Type `Free` and start deploy.

</details>

<details>
<summary>Features</summary>

## Features
- Currently user can Sign up as Job seeker or Job Recruiter
- User can modify their profile
- User can change password
- Job Recruiter can add, update, delete job
- Currently Job Seeker can view job only

</details>