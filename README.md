1. `poetry init`
2. `poetry shell`
3. `poetry add django fastapi pydantic pydantic_settings uvloop httptools uvicorn`
4. `django-admin startproject server .`
5. `python manage.py startapp users`
6. Build custom user in users.models
7. Set new user in settings.py
8. `python manage.py makemigrations users`
9. `python manage.py migrate`
10. Build custom forms for CustomUser for admin panel in users app
11. Register User changes in admin.py
12. Create a superuser:  `python manage.py createsuperuser`
13. Visit: http://127.0.0.1:8000/admin/ and log in.


### Helpful Tips
- Did you accidently commit file(s) you didn't intend to commit?

Add them to the `.gitignore` file and then:

### Remove the files from the index (not the actual files in the working copy)
$ git rm -r --cached .

# Add these removals to the Staging Area...
$ git add .

### ...and commit them!
$ git commit -m "Clean up ignored files"
