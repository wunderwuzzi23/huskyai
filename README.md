# Husky AI

This repo contains Husky AI training material, the web server and model file if you would like to follow along the Machine Learning Attack Series and try various attacks yourself.

![HuskyAI](https://embracethered.com/blog/images/2020/husky-ai.jpg)


## Running Husky AI yourself

The Husky AI web application is in the `/webapp` folder.

```
docker build . -t huskyai_webapp
docker run -p 8000:20080 huskyai_webapp
```

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

### Production Web Server

The way Husky AI is hosted in production currently is by using `flock` and a simple `crontab` entry:

```
sudo crontab -e
```

Use `flock` to make sure Python web server is running at all times (simple solution):

```
* * * * * /usr/bin/flock -n /tmp/huskyai.lock su - husky -c "cd /opt/huskyai/ && python huskyai.py"
```


# Machine Learning Attack Series - Overview

![Machine Learning Attack Series](https://embracethered.com/blog/images/2020/ml-attack-series.jpg)

## Machine Learning Basics and Building Husky AI

* [Getting the hang of machine learning](/blog/posts/2020/machine-learning-basics/)
* [The machine learning pipeline and attacks](/blog/posts/2020/husky-ai-walkthrough/)
* [Husky AI: Building a machine learning system](/blog/posts/2020/husky-ai-building-the-machine-learning-model/)
* [MLOps - Operationalizing the machine learning model](/blog/posts/2020/husky-ai-mlops-operationalize-the-model/)

## Threat Modeling and Strategies 

* [Threat modeling a machine learning system](/blog/posts/2020/husky-ai-threat-modeling-machine-learning/)
* [Grayhat Red Team Village Video: Building and breaking a machine learning system](https://www.youtube.com/watch?v=-SV80sIBhqY)
* [Assume Bias and Responsible AI](/blog/posts/2020/machine-learning-attack-series-assume-bias-strategy/) 

## Practical Attacks and Defenses

* [Brute forcing images to find incorrect predictions](/blog/posts/2020/husky-ai-machine-learning-attack-bruteforce/) 
* [Smart brute forcing](/blog/posts/2020/husky-ai-machine-learning-attack-smart-fuzz/) 
* [Perturbations to misclassify existing images](/blog/posts/2020/husky-ai-machine-learning-attack-perturbation-external/) 
* [Adversarial Robustness Toolbox Basics](/blog/posts/2020/husky-ai-adversarial-robustness-toolbox-testing/)
* [Image Scaling Attacks](/blog/posts/2020/husky-ai-image-rescaling-attacks/)
* [Stealing a model file: Attacker gains read access to the model](/blog/posts/2020/husky-ai-machine-learning-model-stealing/) 
* [Backdooring models: Attacker modifies persisted model file](/blog/posts/2020/husky-ai-machine-learning-backdoor-model/)
* [Repudiation Threat and Auditing: Catching modifications and unauthorized access](/blog/posts/2020/husky-ai-repudiation-threat-deny-action-machine-learning/)
* [Attacker modifies Jupyter Notebook file to insert a backdoor](/blog/posts/2020/cve-2020-16977-vscode-microsoft-python-extension-remote-code-execution/)
* [CVE 2020-16977: VS Code Python Extension Remote Code Execution](/blog/posts/2020/cve-2020-16977-vscode-microsoft-python-extension-remote-code-execution/)
* [Using Generative Adversarial Networks (GANs) to create fake husky images](/blog/posts/2020/machine-learning-attack-series-generative-adversarial-networks-gan/)
* [Using Azure Counterfit to create adversarial examples(/blog/posts/2020/huskyai-using-azure-counterfit/)]

## Miscellaneous

* [Participating in the Microsoft Machine Learning Security Evasion Competition - Bypassing malware models by signing binaries](/blog/posts/2020/microsoft-machine-learning-security-evasion-competition/)
* [Husky AI Github Repo](https://github.com/wunderwuzzi23/huskyai/)
