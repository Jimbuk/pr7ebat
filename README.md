### build image 1
```sudo docker build -t fluck-ubunut ./backend```
### build image 2
```sudo docker build -t proxy-nginx ./proxy```

### 1 conteiner
```docker run -p 5000:5000 --network host -it fluck-ubuntu```
### 2 conteiner
```docker run -p 5000:5000 -p 80:80 --network host -it proxy-nginx```
