Carcass for Postgres and Django
========================

Technology
----------------
- Docker
- Python 3.4
- Django 1.11
- Postgres 9.5
- Nginx
- Gunicorn
- Supervisor
- Virtualenv


Getting Started with Docker and Docker Compose for Local Development
--------------------------------------------------------------------

### Install Docker

https://docs.docker.com/installation/

### Install Docker Compose

http://docs.docker.com/compose/install/

### Install the app's

In the project books ./book/dev/ (where the `Makefile` file is located), run:

```
make build
```

then

```
make bootstrap
```

then

```
make db
```

then test db

```
psql -U mark -h localhost
```

if all OK, down db

```
make down
```

then migrate db

```
make migrate
```

### To run any command inside the Django Docker container, simply prepend 
```
make shell
```

### This will start the containers in the background.

```
make up
```

When you need finish all containers:

```
make down
```

### View the logs

```
make log
```

### Rebuild Docker containers

```
make rebuild
```

### Clear untagged Docker containers

```
make clear
```

### To view runing Docker containers

```
make ps
```