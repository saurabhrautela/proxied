# Proxied
Proof of concept showing how to restrict application's access on the Web to whitelisted domain names.

## Overview

We have a flask application that fetches and displays a web page. We want that the application should only be able to access some whitelisted domain names.

For this we can use a proxy server and redirect all the requests through it. The application server should be deployed in a private subnet to make sure no program can bypass the proxy.

In this application `tinyproxy` is used. Some important configuration in it are:
1. `Filter`: define location of file containing list of domain names to be filtered.
2. `FilterDefaultDeny`: if it's value is yes, the proxy server denies requests to all the domain names except the ones mentioned in the `Filter`.
3. `Upstream`: input value in case the proxy server has to access the Web using some other proxy server.

For more information visit [the Tinyproxy website](https://tinyproxy.github.io/).

## Steps to access application

* Create `requirements.txt` file.

```bash
pip3 install pipenv
pipenv lock -r >> requirements.txt
```
 
* Build `app` and `tinyproxy` docker images.
```bash
docker-compose build
```

* Run containers
```bash
docker-compose up -d
```

* Access the application at:
    * `http://0.0.0.0/allowed`:
        Get list of all allowed domain names.
    * `http://0.0.0.0`:
        Access web interface to send requests.

* Update file `./tools/tinyproxy/filter` and rebuild docker image to change list of domain names allowed by the proxy.

**Note**: The `upstream` functionality does not work if you use `alpine` base image and install `tinyproxy` using `apk` tool. This may be because it is not compiled with the functionality, I did not explore much as I am fine with `ubuntu` and a bit short on time but feel free to explore and update.
