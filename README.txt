CODERED CERTIFICATE GENERATOR — PUBLIC DJANGO APP

FEATURES
- Public certificate generator: no user login or signup.
- No admin login or Django admin portal.
- Certificate live preview and editing.
- Default mentor signature: static/images/devadathan-signature.png.
- Upload a replacement signature in the browser.
- QR code, certificate/company IDs, HD PDF and PNG downloads.
- Original certificate design, fonts, and JavaScript libraries retained.

LOCAL SETUP (Windows PowerShell)
1. Extract this ZIP and open the codered-certificate folder.
2. Create and activate a virtual environment:
   py -m venv venv
   .\venv\Scripts\Activate.ps1
3. Install dependencies:
   pip install -r requirements.txt
4. Start the website:
   python manage.py runserver
5. Open http://127.0.0.1:8000/

No createsuperuser, login, signup, or admin setup is required.

RENDER DEPLOYMENT
Build Command:
   pip install -r requirements.txt && python manage.py collectstatic --noinput

Start Command:
   gunicorn config.wsgi:application

Environment Variables:
- DJANGO_SECRET_KEY: set a long, random secret value.
- DJANGO_DEBUG: False
- DJANGO_ALLOWED_HOSTS: your actual Render hostname (and custom domain if used).

The project does not install Django admin, auth, sessions, or contenttypes apps,
so there are no account/admin database migrations or admin-user dependencies.
Static files are served by WhiteNoise. The certificate is generated in the
visitor's browser; this app does not store generated certificates in a database.

NOTE
A replacement signature uploaded in the browser is saved only in that browser's
localStorage. The supplied signature is the default static signature included
in the project.
