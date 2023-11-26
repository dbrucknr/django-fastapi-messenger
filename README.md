1. `poetry init`
2. `poetry shell`
3. `poetry add django fastapi pydantic pydantic_settings uvloop httptools uvicorn`
4. `django-admin startproject server .`
5. `python manage.py startapp users`
6. Build custom user in users.models
7. Set new user in settings.py and register app
8. `python manage.py makemigrations users`
9. `python manage.py migrate`
10. Build custom forms for CustomUser for admin panel in users app
11. Register User changes in admin.py
12. Create a superuser:  `python manage.py createsuperuser`
13. Visit: http://127.0.0.1:8000/admin/ and log in to confirm changes worked.
14. `python manage.py startapp conversations`
15. Add new conversations app to `settings.py`
16. Build new conversations models
17. `python manage.py makemigrations`
18. `python manage.py migrate`
19. Register new models in admin
20. Begin modifying `asgi.py` to support fastapi + uvicorn libs
21. Fix staticfile issue for admin panel since we are switching to uvicorn
    - Add `STATIC_ROOT = os.path.join(BASE_DIR, 'static', )` to `settings.py`
    - Add
    ```
            from django.conf.urls.static import static
            from django.conf import settings

            urlpatterns = [.
            .....] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    ```
    into `server/urls.py`
22. Run: `python manage.py collectstatic --noinput`
23. run server with `uvicorn server.asgi:application --reload`
24. Verify Django app has been mounted by visiting (static assets should work): `http://127.0.0.1:8000/admin/`
25. Begin building API system in conversations - new folder / router
26. register the new api router in `asgi.py`
27. Verify new GET routes in browser:
    - `http://localhost:8000/api/conversations`
    - `http://localhost:8000/api/conversations/1`


### Helpful Tips
- Did you accidently commit file(s) you didn't intend to commit?

Add them to the `.gitignore` file and then:

### Remove the files from the index (not the actual files in the working copy)
$ git rm -r --cached .

# Add these removals to the Staging Area...
$ git add .

### ...and commit them!
$ git commit -m "Clean up ignored files"
