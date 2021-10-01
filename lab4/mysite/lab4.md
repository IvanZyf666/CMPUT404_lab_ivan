1. https://github.com/IvanZyf666/CMPUT404_lab_ivan/lab4/

2. Performing system checks...

System check identified no issues (0 silenced).
September 28, 2021 - 15:50:51
Django version 3.1.6, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

3. http://127.0.0.1:8000 : 404 page not found
    http://127.0.0.1:8000/polls/ : hello,world. you're at the polls index.

4.  Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. 

5. from admin page, I can get username/password textbox
    admin.site.register(Department)

6. You're looking at question 38.
You're looking at the results of question 38.
You're voting on question 38.
path('<poll_id>/', views.response_string, name='response_string'),

7. hardcode is hard to change in the future, and does not have good readablity.

8. 
The intention of Generic Views is to reduce boilerplate code when you repeatedly use similar code in several views. You should really use it just for that. Basically, just because django allows something you are doing generically you shouldn't do it, particularly not when your code becomes not to your like.