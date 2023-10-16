## Info

Code for Python REST API starter with FAST API, Mamba and Hydra.

Full article is available on:
1. [Dzone](https://dzone.com/articles/snake-based-rest-api)
2. [Medium](https://medium.com/@PaskSoftware/python-rest-api-starter-2ff39e7ebbb8)

## Running Locally 

### Building Environment

Before creating the environment install [Mamba](https://mamba.readthedocs.io/en/latest/).

| Operation          | Script                                                        |
|--------------------|---------------------------------------------------------------|
| Create environment | `mamba env create -n greeter-service --file environment.yaml` |
| Update environment | `mamba env update --file environment.yaml --prune`            |

### Starting Application

You can run this application in two separate ways:

* Docker service

> `docker compose build && docker compose up`
>
> It will set up mamba env inside the docker and run whole application with preconfigured settings.

* Python service

> Running application in this manner require setting `GREETER_CONFIG_DIR` environmental variable
> it represents path to a 'config' directory from repository.
>
>`./deploy-local.sh`
>
> Script will create local mamba environment named `greeter-service-${current-timestamp}`
> and use it to build and run python service with greeter app.


You can also run it from IDE like PyCharm as FAST API app, but it is out of the scope of this README



