FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip && apt-get install git -y && apt install nginx -y

RUN git clone https://github.com/Jimbuk/pr7ebat.git

ONBUILD RUN mv /pr7ebat/proxy/nginx.conf /etc/nginx/nginx.conf

ONBUILD CMD ["nginx","-g","daemon off;"]

WORKDIR /pr7ebat/

RUN pip install --no-cache-dir -r ./backend/requirements.txt

EXPOSE 5000

CMD ["python3", "./backend/aaaaaaaaaaaaaaaa.py"]