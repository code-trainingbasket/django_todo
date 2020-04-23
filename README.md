Have your Project Ready -> Project Name : ABCD
requirements.txt:
* Create a virtual environment:
* virtualenv env_name
* Make sure this is NOT in your project directory
* cd env_name
* cd Scripts
* activate
* cd ../..
* cd ABCD
* python manage.py runserver
* If there is an error, remove the errors by installing the correct packages
* Do the aboe step till you have installed all the required packages
* pip install gunicorn
* pin install whitenoise
* pip install django_heroku
* pip freeze > requirements.txt

* In your project directory, create two files: Procfile, runtime.txt
* Procfile-> Content: web: gunicorn ABCD.wsgi --log-file -
* runtime.txt -> Content: python-3.7.5

* In your settings.py file make the following changes
* import django_heroku
* django_heroku.settings(locals()) # At the end of the file
* add this to middleware:
* 'whitenoise.middleware.WhiteNoiseMiddleware',


In your CMD open the directory of your project where you have manage.py file

* git init
* git add -A
* git commit -m "YOUR COMMIT MESSAGE"
* heroku login
* heroku create sitename
* heroku git:remote -a sitename
* git push heroku master

If the above commands ran successfully:
* heroku run python manage.py migrate
* heroku run python manage.py createsuperuser
