FROM python:3.6-buster

#installing cron and running it
RUN apt update
RUN apt install -y cron
RUN service cron restart

RUN pip install pipenv

ADD spotify_fetcher /usr/src/spotify_fetcher

WORKDIR /usr/src/spotify_fetcher/

COPY Pipfile Pipfile.lock ./

# pipenv dependencies system installation
RUN pipenv install --system --deploy

# settings DJANGO_SETTINGS_MODULE for "python manage.py" to
# take into account production environment
RUN export DJANGO_SETTINGS_MODULE=spotify_fetcher.settings.production

#static file serving for production
RUN python manage.py collectstatic

# setting up the crontab
RUN python manage.py crontab add
