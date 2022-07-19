# aqicn-exporter
Local aqicn.org parser and exporter for Prometheus

```
Environment variables used to configure the exporter.
HOST_PORT       Sets port to expose the prometheus metrics on. default to 9090
LATITUDE        Sets the latitude to use for the location
LONGITUDE       Sets the longitude to use for the location
AQICN_TOKEN     Sets the AQICN token to use for the API calls
UPDATE_INTERVAL Sets interval between updates in seconds, default is 10.0 seconds
```

## Run with Docker

Add your configuration to `env.list.example` file and rename it to `env.list`. Then build Docker image:

```
docker build -t oleksiikutuzov/weatherapi-exporter .
```

Then you can run the image in the background with the following command:
```
docker run -d -p HOST_PORT:9090 --restart unless-stopped --env-file env.list --name aqicn-exporter aqicn-exporter
```

To check image status:
```
docker ps -a
```

To stop running image:
```
docker stop aqicn-exporter
```

To start running image:
```
docker start aqicn-exporter
```

To delete:
```
docker rm aqicn-exporter
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

Now let's create configuration file:
```
sudo nano /etc/systemd/system/aqicn-exporter.service
```

And paste the following into it:
```
# /etc/systemd/system/aqicn-exporter.service
[Unit]
Description=AQICN exporter service
After=multi-user.target

[Service]
Type=simple
User=<username>
Restart=always
Environment=HOST_PORT=8080
Environment=LATITUDE=XXXX
Environment=LONGITUDE=XXXX
Environment=AQICN_TOKEN=XXXX
Environment=UPDATE_INTERVAL=10
ExecStart=/usr/bin/python3 /home/<username>/aqicn-exporter/main.py

[Install]
WantedBy=multi-user.target
```

Insert the username in your OS where `<username>` is written. The ExecStart flag takes in the command that you want to run. So basically the first argument is the python path (in my case it’s python3) and the second argument is the path to the script that needs to be executed. Restart flag is set to always because I want to restart my service if the server gets restarted. For more information on this, you can go to this link. Now we need to reload the daemon.
```
sudo systemctl daemon-reload
```

Let’s enable our service so that it doesn’t get disabled if the server restarts.
```
sudo systemctl enable aqicn-exporter.service
```

And now let’s start our service.
```
sudo systemctl start aqicn-exporter.service
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

