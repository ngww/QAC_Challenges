# an argument for the python version
# by default this is for version 3.6.8, but it can be modified
ARG PYTHON_VERSION=3.6.8

# the base image to build from which is ready to run
# Python code immediately
FROM python:${PYTHON_VERSION}

# RUN command to make a new directory and WORKDIR sets the working directory
RUN mkdir /flask-blog
WORKDIR /flask-blog

# COPY all into the flask blog directory
COPY . /flask-blog

# COPY requirements and RUN to install all the requirements
COPY . requirements.txt
RUN pip install -r requirements.txt

# environment variables
ENV MYSQL_USER your-username
ENV MYSQL_PASS your-password
ENV MYSQL_URL your-host
ENV MYSQL_DB your-database-name
ENV SECRET_KEY your-secret-key

# the application runs on port 5000
EXPOSE 5000

# an entrypoint has been set here
# the Python binary is executed, with the correct script as an argument
ENTRYPOINT ["/usr/local/bin/python", "app.py"]
