FROM arm64v8/ubuntu
RUN apt-get update
RUN apt-get upgrade -y
RUN apt install python3 -y
RUN apt-get install python3-pip -y

WORKDIR /usr/scr/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "app.py"]