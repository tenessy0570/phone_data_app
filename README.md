# Порядок запуска проекта

Откройте консоль, создайте новую папку, перейдите в неё. 
Далее скопируйте следующие в консоль:
```
git clone https://github.com/tenessy0570/phone_data_app.git
cd phone_data_app
```

Далее либо запустите скрипт start.sh:
```
. start.sh
```
Либо введите в консоль команду
```
docker-compose up --build -d --force-recreate
```

Далее перейдите в swagger:
```
http://127.0.0.1:8000/docs
```