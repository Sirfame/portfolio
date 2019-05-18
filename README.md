# portfolio

Building new personal website with Flask.

To run with virtualenv:
```
> export FLASK_APP=app.py
> flask run
```

To run with docker:
```
> docker build -t blog:latest .  
> docker run -p 5000:5000 blog  
```

To compose with docker:
```
> docker-compose up 
```