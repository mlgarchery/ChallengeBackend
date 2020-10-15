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

- Python env (using pipenv):
```
pipenv install
pipenv shell
cd spotify_project/
python manage.py runserver
```