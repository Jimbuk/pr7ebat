FROM ubuntu:latest

LABEL description="Boyko Dmitry Vyacheslavovich INBO-11-20"

RUN apt-get update && apt-get install -y python3 python3-pip && apt-get install git -y && apt install nginx -y && apt-get install -y wget && apt-get install -y postgresql-client

RUN git clone https://github.com/Jimbuk/pr7ebat.git

ONBUILD RUN mv /pr7ebat/proxy/nginx.conf /etc/nginx/nginx.conf && echo "Сборка и заруск произведены. Автор Бойко Д.В."

ONBUILD CMD ["nginx","-g","daemon off;"]

RUN wget -i ./pr7ebat/img.png https://www.mirea.ru/upload/medialibrary/80f/MIREA_Gerb_Colour.png

WORKDIR /pr7ebat/

RUN pip install --no-cache-dir -r ./backend/requirements.txt

COPY app.py /app.py

ADD app.py /app.py

EXPOSE 5000

CMD ["python3", "./backend/aaaaaaaaaaaaaaaa.py"]