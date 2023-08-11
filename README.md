python3 -m venv venv
source venv .venv
pip install -r requirements.txt

django-admin startproject dcrm

python manage.py startapp website

docker network create demo-network

How to run mysql
https://www.appsdeveloperblog.com/ahow-to-start-mysql-in-docker-container/

docker run -p 3306:3306 --name main-mysql -e MYSQL_ROOT_PASSWORD=password mysql:5.7.37'

Solve subprocess-exited-with-error exit 1 mysql pip install

Make sure activate venv
brew install mysql pkg-config


https://pypi.org/project/mysqlclient/


python manage.py migrate

winpty python manage.py createsuperuser