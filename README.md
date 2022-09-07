# capstoneProject
  - Captone project is is responsible for creating movies and managing and assigning actors to those movies, creating a system to simplify and streamline your process.
## Motivation
  - I developed this project to make use of the knowledge you acquired in this nanodegree and hence gain confidence in these skills
  - I wanted to contribute something to the open-source community by building this tool
### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip3 install -r requirements.txt
```
#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.


- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

### Set up the Database

You must go .env file and replace your config

With Postgres running, create a `postgres` database:

```bash
createbd postgres
```

### Run the Server
<!-- From within the `./src` directory first ensure you are working using your created virtual environment. -->

I implement API in the app.py, so you should set up the FLASK_APP environment variable used to run the app.

- For CMD

```bash
set FLASK_APP=app.py

```

- For PowerShell

```bash
$env:FLASK_APP = "app"

```

To run the server, execute:

```bash

flask run --reload

```

The `--reload` flag will detect file changes and restart the server automatically.
#### Create a new Auth0 Account
1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:actors`
    - `get:actors-detail`
    - `post:actors`
    - `patch:actors`
    - `delete:actors`
    - `get:movies`
    - `get:movies-detail`
    - `post:movies`
    - `patch:movies`
    - `delete:movies`
6. Create new roles for:
   - Casting Assistant
     - can `get:actors`
     - can `get:actors-detail`
     - can `get:movies`
     - can `get:movies-detail`
   - Casting Director
     - can perform all actions a Casting Assistant has and...
     - can `patch:movies`
     - can `patch:actors`
     - can `delete:actors`
     - can `post:actors`
   - Executive Producer  
    - can perform all actions

## User info
1. Casting Assistant
    - username: castingassistant@gmail.com
    - password: Admin@123
    - token: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik4yUWNsenU5cDZNaGNta29zWXU4NCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRhbmx0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MzE0YThhMzQzYjY2YjY2OTkwNzJmYTkiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY2MjU0MjgwMiwiZXhwIjoxNjYyNTUwMDAyLCJhenAiOiI3QlR2ZDhFNlRNVFJJbWNsRFVOUU1MdWZ2R1daNTdPayIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDphY3RvcnMtZGV0YWlsIiwiZ2V0Om1vdmllcyIsImdldDptb3ZpZXMtZGV0YWlsIl19.nyT8nh3LenjtMGKsXrP7b01M22wK1S9vuIw-419lkCrkh0KfDi_bBz_NR2Qcc81EK-FkpkMUgk8S3QUn8dZ46YkWax5qOKM3-y-DX0HVayijAk1WXUCluKYvrX9vvbANNbSRwUAKOMsxsgWVPeHaPaiu1HrhEb9GoYzQK0BmkytYSeDSx-dmOb9QMlEiYBKxtcdXQkEGIIJSxVpA-XXer4Trvo8vIzACFSsE65V_EX85DQQkbRnLgTeB7H9V2uPT2YVD-9T3yWDpz-1l6tiLALsmw8n2BcN9nXsqM_yHFXTOcVn7cjF107Do1mYMWXEp0VSso5K9whdDYMfHSLdnFw
2. Casting Director
    - username: castingdirector@gmail.com
    - password: Admin@123
    - token: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik4yUWNsenU5cDZNaGNta29zWXU4NCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRhbmx0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MzE0YThjZjQ0YjBjNjM0ZTUyM2EwZGQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY2MjU0MjY4MCwiZXhwIjoxNjYyNTQ5ODgwLCJhenAiOiI3QlR2ZDhFNlRNVFJJbWNsRFVOUU1MdWZ2R1daNTdPayIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6YWN0b3JzLWRldGFpbCIsImdldDptb3ZpZXMiLCJnZXQ6bW92aWVzLWRldGFpbCIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.FFBAQDoiqs0VhfQDesZR5sy1gA9-OpfJi8F2qX2K9841k1XsH719SEhVYOHmAAliAz6GEiPTEEa04a6IR5g6wo4U2u0Py6AV5_VRlH2IZsa9rXnscXUnrRt-Y4L_b4rH112SPAYKOtkGd3Ydn563j-4ddJE7NxRZrQHwG7tkehkkvKT3oQPfcreQbG_hHtRg1YYi_LGK_Qu4_2kJJaZAs6RYheiIQvxiA_8tgWpkBQ2Ag7AT8H8R6dDF3WUJHKqZej0ahFSM5CEYQzO7hw11Fh7Fgj0dKXHNLFXcF-2kosp-6spgZxVEHzPeICQS-euhMF1P6lP7CHEoyCeooxcGBg
3. Executive Producer
    - username: executiveproducer@gmail.com
    - password: Admin@123
    - token: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik4yUWNsenU5cDZNaGNta29zWXU4NCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRhbmx0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MzE0YThmMGRlODBkODlmNzc3N2JjOGMiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY2MjU1NTA2NiwiZXhwIjoxNjYyNTYyMjY2LCJhenAiOiI3QlR2ZDhFNlRNVFJJbWNsRFVOUU1MdWZ2R1daNTdPayIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0OmFjdG9ycy1kZXRhaWwiLCJnZXQ6bW92aWVzIiwiZ2V0Om1vdmllcy1kZXRhaWwiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.TRQEAg5gC1AWRLRbUE8B7OGSp2_oGPZbewm3sLpfmgYAuJ6s2n21mYHJVNnVb1nV42hNV28m7GSfmgxyHv6S-sfKmQ2f1_cPkC3uoXPgFwVXunx29YwydKp4SFDkhT7wDNSLJXyXdt11mX55D3UHTKjwBlXnhJ1Y0GhP_rmbQ51y4UCABFO-zkCtqeFRACDDd8JWAecaKaP9jFsI5t_CtmJ9rIBQmDwBC5a9m7AL1iG_OEMcMzTEHmC9IJiOFtcQIAptWixEP-FMAjTBorr_ZPqHazyJgj4bX587wfptN5nnB54WSqU9oZW61SZQqgcO16l8rj872UKVISINDnj01w
## Link deploy
https://myapp-21012000.herokuapp.com/