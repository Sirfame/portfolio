# portfolio

Building new personal website with Flask.

To run the Flask app with virtualenv:
```
> source virtualenv/envname/bin/activate
> export FLASK_APP=app
> export FLASK_ENV=development
> flask run
```

Still trying to figure out how to run the actual Flask app with Docker.

To run app.py with docker:
```
> docker build -t blog:latest .  
> docker run -p 5000:5000 blog  
```

To compose with docker:
```
> docker-compose up 
```

For some reason, the docker container sometimes won't be killed with Ctrl+C, had to use
```
> docker kill $(docker ps -q)
```