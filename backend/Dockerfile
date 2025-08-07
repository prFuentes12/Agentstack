FROM python:3.13.4-slim-bullseye

#Create python virtual environment

RUN python -m venv /opt/venv 
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

#copy local_folder/file container_destination
COPY  requirements.txt /tmp/requirements.txt

#RUN whitin_container_while_building
RUN pip install -r /tmp/requirements.txt

COPY ./src .