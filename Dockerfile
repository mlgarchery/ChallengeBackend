FROM python:3.6-buster

#installing cron
RUN apt update
RUN apt install -y cron

RUN pip install pipenv

# adding the sources
ADD spotify_fetcher /usr/src/spotify_fetcher

WORKDIR /usr/src/spotify_fetcher/

# adding the env files
COPY Pipfile Pipfile.lock ./

# pipenv dependencies system installation
RUN pipenv install --system --deploy

# settings DJANGO_SETTINGS_MODULE for "python manage.py" to
# take into account production environment
RUN export DJANGO_SETTINGS_MODULE=spotify_fetcher.settings.production

#static file serving for production
RUN python manage.py collectstatic