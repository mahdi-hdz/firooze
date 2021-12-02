# firooze
A project for an apartment complex so that residents can see their debts, notifications, send a message to the board of the complex and ... (using Vue js and Django)

Technologies used in this project:
	Python 3.x
	Django 2.2.x
	Django Rest Framework
	Postgresql
	Docker
	Vuejs 3 - Vue Cli - Vue Router
	HTML 5
	CSS 3
	Bootstrap
	Axios




Intallation:
	first clone or download this project:
		git clone https://github.com/mahdi-hdz/firooze.git
	
	
		docker volume create firooze_postgresql
		docker network create firooze_network
		
		You need to create .env file in the backend root file with default values.

			POSTGRES_USER=postgres
			POSTGRES_PASSWORD=postgres
			POSTGRES_DB=postgres

docker-compose up -d
	in firooze-backend directory:
	virtualenv venv 
	
	sourse venv/bin/activate
	pip install -r requirement.txt
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver
	
in firooze_frontend root:
npm install
npm run serve

You may need add your frontend localhost address to crosheaders in settings.py.
If your django localhost address different as http://127.0.0.1:8000 , you need to change the axios requests address in all vue components.
	
