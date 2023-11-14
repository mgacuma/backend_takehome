# ETL App

### Introduction
This app is a simple ETL pipeline that can be triggered via an API call. A set of CSV files will be processed, derived some features from, and then uploaded into a postgres database table.


### Requirements
To run this app, you will need:
- Python 3.9.x
- [Docker](https://docs.docker.com/get-docker/)

## Build
To build the docker image, run in a new terminal
```
docker-compose build
``` 


## Run
To build and run this app, run 

```
sh run.sh
``` 

This will build and run the container using docker-compose and the provided Dockerfile. 

To run a built image in a container, run 

```
docker-compose up
```

## Trigger
The trigger to run the `etl()` process is by sending a `GET` request to the `/trigger` endpoint. Simply run 

```
curl -i http://localhost:5000/trigger
``` 

or, on a web browser, go to 

```
http://localhost:5000/trigger
``` 

## Postgres Database

The postgres database is a service attached to the app's container. To access the postgres tables, open Docker Desktop, then in the Containers tab, select `backend_takehome`, then `postgres-container`. Once inside, go to the `Terminal` tab and run 
```
psql -U postgres
```
to access the psql cli. Once here, you can run `\dt` to list all tables, or run queries like `SELECT * from users;` to view data inside the table.

## Changing The Data
You can change the data files by adding/modifying the files under `./data` directory. Make sure to include `compounds.csv`, `users_experiments.csv`, and `users.csv` files for etl features to return.
