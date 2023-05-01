FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip && apt-get install git -y

RUN git clone https://github.com/Jimbuk/pr7ebat.git

WORKDIR /pr7ebat/backend

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "aaaaaaaaaaaaaaaa.py"]