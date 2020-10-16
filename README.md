Listing here the important environment configuration before putting all this into a Dockerfile


- Ubuntu 18.04
- Postgres13

```
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql
```

useful
```
sudo service postgresql restart
```

Relative to psycopg2
```
sudo apt install python3-dev libpq-dev
```

Setting up the credentials
```
export CLIENT_ID="youtClientID"
export CLIENT_SECRET="yourClientSecret"
```


- Installing the python env (using pipenv Pipfile):
```
pipenv install
pipenv shell
```

Running the app
```
cd spotify_project/
python manage.py crontab add 
python manage.py runserver 5000
```

Shutting down crontab tasks
```
python manage.py crontab remove
```

# ChallengeBackend

Your goal is to create an app using the [spotify web api](https://developer.spotify.com/documentation/web-api/). You can make for example a [Flask](https://flask.palletsprojects.com/en/1.1.x/) or [Django rest framework](https://www.django-rest-framework.org/) project, it has to be able to authenticate to Spotify to fetch the new releases. Your job is to add two new features:
- A way to fetch data from spotify’s new releases API (/v1/browse/new-releases) and persist in a Postgresql DB (mandatory)
- A route : `/api/artists/` returning a JSON containing informations about artists that have released new tracks recently, from your local copy of today’s spotify’s new releases.

## Project Structure
The spotify auth is provided by us: (follows spotify web api.): it is located in `spotify_auth.py`.
The flow ends with a call to `/auth/callback/` which will give you the necessary access tokens.
To use it, we will provide you with the necessary: CLIENT_ID and CLIENT_SECRET.
Feel free to move it and re-organise as you please, we expect a well organised and clean code. Keep in mind that we want an Authorization Code Flow to see how you handle user authorization.
  
  
## Tech Specifications
- Be smart in your token usage (no unnecessary refreshes)
- Don’t request spotify artists at each request we send you
- The way you store the artists in Postgresql DB is going to be important use an ORM.
- As stated above, to test your server we will `GET /api/artists/` and we expect a nicely organised payload of artists. Make sure to use proper serialization and handle http errors.

All stability, performance, efficiency adds-up are highly recommended.
