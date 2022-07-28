# weatherapi-exporter
Local weatherapi.com parser and exporter for Prometheus

```
Environment variables used to configure the exporter.
HOST_PORT           Sets port to expose the prometheus metrics on. default to 9090
LOCATION            Sets the location to use for the location
WEATHERAPI_TOKEN    Sets the weatherapi token to use for the API calls
UPDATE_INTERVAL     Sets interval between updates in seconds, default is 10.0 seconds
```

## Run with Docker

You can run the image in the background with the following command:
```
docker run -d -p 8090:9090 --restart unless-stopped -e HOST_PORT=9090 -e LOCATION=XXXXXX -e WEATHERAPI_TOKEN=XXXXXX -e UPDATE_INTERVAL=10.0 --name weatherapi-exporter oleksiikutuzov/weatherapi-exporter
```

To check image status:
```
docker ps -a
```

To stop running images:
```
docker stop weatherapi-exporter
```

To start running the image:
```
docker start weatherapi-exporter
```

To delete:
```
docker rm weatherapi-exporter
```
## Run with Docker-compose

Create a `docker-compose.yml` file and add your configuration to it:

```
version: "3"

services:
  weatherapi-exporter:
    container_name: weatherapi-exporter
    image: oleksiikutuzov/weatherapi-exporter:latest
    restart: always
    ports:
      - 8090:9090
    environment:
      HOST_PORT: 9090
      LOCATION: XXXXXX
      WEATHERAPI_TOKEN: XXXXXX
      UPDATE_INTERVAL: 10.0
```

Then run the image with the following command:

```
docker-compose up -d
```
### To update the image:

```
docker pull oleksiikutuzov/weatherapi-exporter
```

And use the `docker-compose` command again:

```
docker-compose up -d
```

## Run with systemd

Almost all versions of Linux come with systemd out of the box, but if your’s didn’t come with it then you can simply run the following command:
```
sudo apt-get install systemd
```

To check which version of systemd you have simply run the command:
```
systemd --version
```

Now let's create the configuration file:
```
sudo nano /etc/systemd/system/weatherapi-exporter.service
```

And paste the following into it:
```
# /etc/systemd/system/weatherapi-exporter.service
[Unit]
Description=weatherapi exporter service
After=multi-user.target

[Service]
Type=simple
User=<username>
Restart=always
Environment=HOST_PORT=8080
Environment=LOCATION=XXXX
Environment=WEATHERAPI_TOKEN=XXXX
Environment=UPDATE_INTERVAL=10
ExecStart=/usr/bin/python3 /home/<username>/weatherapi-exporter/main.py

[Install]
WantedBy=multi-user.target
```

Insert the username in your OS where `<username>` is written. The ExecStart flag takes in the command that you want to run. So basically the first argument is the python path (in my case it’s python3) and the second argument is the path to the script that needs to be executed. The restart flag is set to always because I want to restart my service if the server gets restarted. For more information on this, you can go to this link. Now we need to reload the daemon.
```
sudo systemctl daemon-reload
```

Let’s enable our service so that it doesn’t get disabled if the server restarts.
```
sudo systemctl enable weatherapi-exporter.service
```

And now let’s start our service.
```
sudo systemctl start weatherapi-exporter.service
```

Now our service is up and running.

### There are several commands you can do to start, stop, restart, and check status.

To stop the service:
```
sudo systemctl stop name_of_your_service
```
To restart:
```
sudo systemctl restart name_of_your_service
```

To check status:
```
sudo systemctl status name_of_your_service
```

