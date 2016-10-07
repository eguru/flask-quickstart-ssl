# Flask Quickstart With SSL Enabled

The Quickstart project provide a quick setup to a dummy project that has a database and admin panel that is running over HTTPS. This project only gives bare minimum code required to get started.

For other quickstart projects, refer to the following projects:

* [Flask Quickstart] (https://github.com/eguru/flask-quickstart)
* [Flask Quickstart With Database] (https://github.com/eguru/flask-quickstart-database)
* [Flask Quickstart With Database And Admin] (https://github.com/eguru/flask-quickstart-database-admin)

# Installation

First, simply get a copy of the project:

```
git clone https://github.com/eguru/flask-quickstart-ssl.git
```

Now, create a virtual environment, see virtualenv installation [here] (https://virtualenv.pypa.io/en/stable/installation/):

```
cd flask-quickstart-ssl/
virtualenv venv
```

Activate the virtual environment:

```
source venv/bin/activate
```

Install the Flask framework:

```
pip install flask
```

Install the Flask's SQLAlchemy extension:

```
pip install flask_sqlalchemy
```

Install the Flask's Admin extension:

```
pip install flask_admin
```

Generate private key:

```
openssl genrsa -out server.key 1024
```

Generate Certificate Signing Request (CSR):

```
openssl req -new -key server.key -out server.csr
```

Generate Self-Signed certificate:

```
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```

see [this](http://anubhav83.in/2016/10/07/webrtc-serve-localhost-https/) blog for more details.

Now, simply start the server:

```
python server.py
```

Open up your web browser and enter the following location:

```
https://localhost:8080

or 

https://<your_ip>:8080

```

Access the admin panel from the following location:
```
https://localhost:8080/admin

or

https://<your_ip>:8080/admin
```
