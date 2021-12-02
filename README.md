# firooze
#### A project for an apartment complex so that residents can see their debts, notifications, send a message to the board of the complex and ... (using Vue js and Django)

## Technologies used in this project:
- Python 3.x 
- Django 2.2.x
- Django Rest Framework
- Postgresql
- Docker
- Vuejs 3 - Vue Cli - Vue Router
- HTML 5
- CSS 3
- Bootstrap
- Axios




## Intallation:
First **clone** or **download** this project:

	$ git clone https://github.com/mahdi-hdz/firooze.git
	
Then create docker network and volumes as below:

	$ docker volume create firooze_postgresql
	$ docker network create firooze_network
		
You need to create .env file in the backend root file with default values.

	POSTGRES_USER=postgres
	POSTGRES_PASSWORD=postgres
	POSTGRES_DB=postgres

Now run postgresql whit docker-compose:

	$ docker-compose up -d
You can check the docker's containers:

	$ docker ps -a
	
**Output** should be like this:

	CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS                   PORTS                                       NAMES
	0b5014ff6af5   postgres:10    "docker-entrypoint.s…"   6 seconds ago   Up 5 seconds             0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   firooze_postgresql


in firooze-backend create virtual environment and active this:

	$ virtualenv venv 
	$ sourse venv/bin/activate

	
	
when active virtual environment, install the project requirements:

	$ pip install -r requirement.txt
	
for django can identify the change in Models.py you should:

	$ python manage.py makemigrations
	$ python manage.py migrate
	
and run the backend server in localhost:

	$ python manage.py runserver
	
### in firooze_frontend root:

	$ npm install
	$ npm run serve


You may need add your frontend localhost address to crosheaders in settings.py.

**If your django localhost address different as http://127.0.0.1:8000 , you need to change the axios requests address in all vue components.**
	
