FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y

WORKDIR /usr/app/src

COPY requirements.txt requirements.txt
COPY annalect.py ./

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "./annalect.py" ]