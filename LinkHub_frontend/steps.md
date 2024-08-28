build a components for re use 
using options API to import /component/Peop... to searchview 1-comosition API
crat popupmessage store
install django , djangoframework for rest api
install jwt for authenticatin
install pillow for handling images save for server optimize them
folders in project bk-end init to make it a module, settings fo all DB define templete, wsgi entry pt for server, urls 
 install django-cors-headers set rules or backend to talk to back

 add adress to talk to bkend by add it in setting-CORS-allowd-origis
 CSRF_TRUSTED_ORIGINS
 LinkHub/accaount/moels.py user_creation custom user manager
 make migration
 editing frontend src/stores/user.py as toast and action required innitstore

 in models.py creat class post, attachement  then make migration 
 python manage.py make migrations
 python manage.py make migrate
 localhost:8000/admin/login/?next=/admin/
python manage.py createsuperuser 
mail, name, pass

python manage.y shell >>>>> from accoun.models import post
user = User.object.get(email='    ')
user.id
user.name
post = "ll"


python3 manage.py shell
Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from account.models import User
>>> users = User.objects.all
>>> users = User.objects.all()
>>> users
<QuerySet [<User: abdallah.saleh203@yahoo.com>, <User: m.gharieb89@gmail.com>]>
>>> users
<QuerySet [<User: abdallah.saleh203@yahoo.com>, <User: m.gharieb89@gmail.com>]>
>>> m.gharieb89@gmail.com

 