![](https://1000logos.net/wp-content/uploads/2017/07/Docker-Logo-768x227.png)

## Docker UI using FLASK and javascript

Following requirement you should satisfy for running this project.

1. Flask
2. Docker

using following command you can install Flask:-
```
pip install Flask
```

Download Docker from here:-
```
https://download.docker.com/linux/
```

change following files in docker daemon and start daemon:-

```
Navigate to /lib/systemd/system in your terminal and open docker.service file
vim /lib/systemd/system/docker.service

Find the line which starts with ExecStart and append -H=tcp://0.0.0.0:2375

replace 0.0.0.0 with docker host ip in your flask file 

Reload the docker daemon
systemctl daemon-reload

Restart the container
sudo service docker restart
```
Now using Following command run your application:-
```shell
set FLASK_ENV = development or production
flask run
```
