# Husky AI - Overview  

Husky AI is part of my [machine learning attack series](https://embracethered.com/blog/posts/2020/machine-learning-attack-series-overview/). This repo contains the models and code to run the Husky AI web server.

Have fun learning more about machine learning!

![HuskyAI](https://embracethered.com/blog/images/2020/husky-ai.jpg)


## Running Husky AI yourself

The Husky AI web application is in the `/webapp` folder.

```
docker build . -t huskyai_webapp
docker run -p 8000:20080 huskyai_webapp
```


The application is then available at: https://localhost:8000/

## Manual installation and setup

```
pip install -r requirements.txt
```

```
#generate a key pair (e.g. for testing on localhost)
openssl ecparam -genkey -name secp384r1 -out server.key
openssl req -new -x509 -sha256 -key server.key -out server.crt -days 7300  -subj '/CN=localhost:8000/O=huskyai/C=US'
```

```
python huskyai.py
```

The application is then available at: http://localhost:20080



### Web Server

The way Husky AI is hosted in production currently is by using `flock` and a simple `crontab` entry:

```
sudo crontab -e
```

Use `flock` to make sure Python web server is running at all times (simple solution):

```
* * * * * /usr/bin/flock -n /tmp/huskyai.lock su - husky -c "cd /opt/huskyai/ && python huskyai.py"
```

# Threat Model

![Threat Model](https://raw.githubusercontent.com/wunderwuzzi23/huskyai/main/threat_model/husky-ai-machine-learning-threat-model.png)
