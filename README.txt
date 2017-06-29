
=======
Test for F.....io
=======

REST, SQLite3, and Websocket chat application

Brief Description
=================

The application has been implemented in Python 3.6.1. I use the django framework. The project is a small chat app and uses Websocket to handle messages and receives a dummy JSON input (once the server is running) All message are stored in SQlite3 database


Directory's
=============

apps

  Contains two apps:

   - chat
        Contains and uses serializer.py , router.py model.py, handlers, channels and migrations

       - management directory
            holds run_message_server.py

   - home
        is the application holding the views

config
    holds the project setting.py, urls.py and wsgi.py


Virtual Environment
===================

1. Create a virtual environment Python 3.6 installation


2. Install the Python packages using the requirement.txt file
    (run: pip install -r requirements.txt in your shell)


To do!
===============

1. Open a terminals and run the command below:

To start server locally,

```
python3 manage.py runserver
```
To start the chat (Websocket) server
```
python3 manage.py run_message_server
```

2. Use http://127.0.0.1:8000

3. Use http://127.0.0.1:8000/admin to access the message model (user:admin, pass: falcon1234)

4. Use http://127.0.0.1:8000/message for api view, for POST or GET


