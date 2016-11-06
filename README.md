# Fbstats
## A Simple django project that does
1. Log in user with Facebook
2. Use Facebook Graph API to pull some user data.
3. Manipulate the data and get some interesting results.
4. Use the API to post to Facebook timeline.

##Installation
1. Clone the repo.
2. cd fbstats
3. pip install -r requirements.txt
4. create mysql database fbstats.
5. python manage.py migrate
6. python manage.py runserver
7. View 127.0.0.1:8000 on your browser.

## Periodic Task
Gets page info, page posts and posts like from facebook api
and updates the database every hour.

###To run the periodic task, you need to do the following steps.
1. Rabbitmq: Install Rabbitmq
2. sudo rabbitmq-server -detached
3. sudo rabbitmqctl add_user santosh mirage
4. sudo rabbitmqctl add_vhost myvhost
5. sudo rabbitmqctl set_permissions -p myvhost santosh ".*" ".*" ".*"
6. sudo rabbitmq-server -detached
7. python manage.py runserver
8. celery -A fbstats beat
9. celery -A fbstats worker -l debug

This will update the database with new posts every hour at 0 minutes.