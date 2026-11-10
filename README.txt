CODERED CERTIFICATE GENERATOR — DJANGO

Features
- Django-authenticated admin portal (no password exposed in JavaScript)
- Certificate live preview and editing
- Default mentor signature: static/images/devadathan-signature.png
- Upload a different signature in the browser when needed
- QR code, certificate/company IDs, HD PDF and PNG downloads
- Original certificate design, fonts, and JavaScript libraries retained

LOCAL SETUP (Windows PowerShell)
1. Extract this ZIP and open the project folder.
2. Create a virtual environment:
   py -m venv venv
   .\venv\Scripts\Activate.ps1
3. Install dependencies:
   pip install -r requirements.txt
4. Create the database:
   python manage.py migrate
5. Create your admin login:
   python manage.py createsuperuser
6. Start:
   python manage.py runserver
7. Open http://127.0.0.1:8000/

LOGIN
Use the username and password created with createsuperuser.
Do not use a hard-coded shared password.

DEPLOYMENT
- Set DJANGO_SECRET_KEY to a secure random value.
- Set DJANGO_DEBUG=False.
- Set DJANGO_ALLOWED_HOSTS to your actual domain(s).
- Build static assets with: python manage.py collectstatic --noinput
- Start command: gunicorn config.wsgi:application
- For production, configure persistent storage for SQLite or switch to PostgreSQL.
- Configure HTTPS at the hosting provider.

NOTE
The browser's uploaded replacement signature is saved in that browser's localStorage only.
The supplied signature is the default static signature included in the project.
