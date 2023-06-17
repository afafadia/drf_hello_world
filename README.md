# Django Rest Framework - Hello World app

## Code Walkthrough

### Environment Setup

1. Clone this repository
2. Navigate to the folder location of this cloned repository on your laptop/PC
3. Create virtual environment: `python3 -m venv venv`
4. Activate virtual environment: `source ./venv/bin/activate`
5. Install packages from "requirements.txt" file: `pip install -r ./requirements.txt`
6. Run command: `python manage.py collectstatic`

## Server Configuration

### Gunicorn

1. Test whether gunicorn is serving django rest framework application (http://localhost:8000) by the following command:
   `gunicorn --workers 5 --bind 0.0.0.0:8000 drf_hello_world.wsgi:application`

### Nginx config

1. Run command: `sudo apt install nginx`
2. Start nginx by the following command: `sudo systemctl start nginx`
3. Check nginx status by the following command: `sudo systemctl status nginx`
4. Run command: `sudo touch /etc/nginx/sites-available/drf_hello_world` and copy/paste the file contents from `./config/drf_hello_world_nginx.conf` to this file
5. Run command: `sudo ln -sf /etc/nginx/sites-available/drf_hello_world /etc/nginx/sites-enabled/`
6. Run command: `sudo nano /etc/nginx/nginx.conf` and change user to current user and save the file
7. Restart nginx: `sudo systemctl restart nginx`
8. Check status of nginx: `sudo systemctl status nginx`
9. In `drf_hello_world/settings.py` file configure ALLOWED_HOSTS to allow your machine's IP address
10. Test whether gunicorn is serving django rest framework application (http://<your_machine_ip_address>) by the following command:
    `gunicorn --workers 5 --bind 0.0.0.0:8000 drf_hello_world.wsgi:application`

### Supervisor config

1. Run command: `mkdir ./etc && touch ./etc/supervisord.conf && chmod +x ./etc/supervisord.conf` and copy/paste the file contents from `./config/supervisord.conf` to this file
2. Run command: `touch ./etc/guni.sh && chmod +x ./etc/guni.sh` and copy/paste the file contents from `./config/guni.sh` to this file
3. Run command: `supervisord`
4. In your browser, navigate to "http://<your_machine_ip_address>" - the browser will render the page corresponding to the view
5. Do some changes in code and then run command `supervisorctl restart all` and again refresh the browser - the browser will render the updated code
