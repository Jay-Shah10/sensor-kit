FROM arm64v8/ubuntu
RUN sudo apt-get update
RUN sudo apt-get upgrade
RUN sudo apt install python3

WORKDIR /usr/scr/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python3", "app.py"]