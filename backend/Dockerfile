FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip
RUN apt-get install git -y
RUN git clone https://github.com/Jimbuk/pr7ebat.git
RUN pip install --no-cache-dir -r /pr7ebat/backend/requirements.txt
EXPOSE 5000
CMD ["python3","/pr7ebat/aaaaaaaaaaaaaaaa.py"]