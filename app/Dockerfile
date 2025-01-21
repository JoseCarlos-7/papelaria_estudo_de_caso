FROM apache/airflow:2.9.3-python3.11 AS airflow
ADD requirements.txt /
USER root
RUN apt-get update && apt-get install -y wget lsb-release inetutils-tools
RUN wget https://dev.mysql.com/get/mysql-apt-config_0.8.24-1_all.deb
RUN DEBIAN_FRONTEND=noninteractive dpkg -i mysql-apt-config_0.8.24-1_all.deb
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C
RUN apt-get update
RUN apt install -y mysql-client
RUN apt-get update
RUN apt-get install -y unixodbc
RUN apt-get install -y mdbtools
USER airflow
RUN pip install --no-cache-dir pip setuptools wheel tornado
RUN pip install --no-cache-dir -r /requirements.txt
ENV TZ="America/Sao_Paulo"

FROM jupyter/minimal-notebook:python-3.11 AS jupyter
WORKDIR /app
ADD requirements.txt /
USER root
RUN apt-get update
RUN apt-get install -y unixodbc
RUN apt-get install -y mdbtools
RUN apt-get install -y default-mysql-client
USER jovyan
RUN pip install --no-cache-dir pip setuptools wheel tornado
RUN pip install --no-cache-dir -r /requirements.txt
ENV TZ="America/Sao_Paulo"
CMD ["jupyter", "lab", "--NotebookApp.token=0"]

FROM squidfunk/mkdocs-material AS mkdocs
WORKDIR /app
ADD mkdocs.yaml /app

FROM python:3.11 AS fastapi
WORKDIR /app
ADD requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
RUN pip install --no-cache-dir fastapi uvicorn
EXPOSE 80
CMD ["uvicorn", "fast:app", "--host", "0.0.0.0", "--port", "80"]

