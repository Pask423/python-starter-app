FROM condaforge/mambaforge

WORKDIR /greeter-service

COPY environment.yaml environment.yaml

RUN mamba env create -n greeter-service --file environment.yaml

COPY api api
COPY config config
COPY setup.py setup.py

ENV PATH /opt/conda/envs/greeter-service/bin:$PATH

RUN /bin/bash -c "source activate greeter-service" && python setup.py install