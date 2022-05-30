# How to run project locally with Django

1. Clone the repo. 

```
$ git clone https://github.com/yaucp/FinverseInterview
$ cd FinverseInterview
```

2. Start a new virtual environment with venv
```
$ python3 -m venv myvenv
$ source myvenv/bin/activate
```

3. Install djano
`$ pip install django`

4. Make migrations
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

5. Create a new superuser
`$ python3 manage.py createsuperuser`

6. Run server with port 4000
`$ python3 manage.py runserver 4000`
