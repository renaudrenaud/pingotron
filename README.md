# pingotron
Ping hosts write in postgres and show the results in grafana

## Prerequistes
1. one instance of Postgresql
2. grafana for the monitoring dahsboard

## Install

1. git clone the project on your disk
2. directory change 
3. install the python requirements

```
git clone https://github.com/renaudrenaud/pingotron.git
cd pingotron
pip install -r requirements.txt
```

## Settings
1. edit the env_var.sh file and write down your values
2. source the env variables file using:

```
nano env_var.sh
source env_var.sh
```

**parameters**
| Parameter| Meaning|
| ------------- | ------------- |
|PG_URL="192.168.1.120" | define the URL for the postgresql server |
|PG_PORT="5432" | postresql port for comunication  | 
|PG_USER="postgres" | user name|
|PG_PASSWORD="postgres" | password for the user|
|PG_DB="postgres" | database name|
|HOSTNAME1="192.168.195.133" | which ip to ping|

Please note you can ping until 100 hostnames add a parameter for each one like

```
HOSTNAME0="192.168.196.100"
HOSTNAME1="192.168.196.101"
HOSTNAME2="192.168.196.102"
...
```


## Usage

```
python3 pingotron.py
```
