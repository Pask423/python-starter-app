#!/bin/bash

timestamp=$(date +%s)
env_name=greeter-service-$timestamp

mamba env create -n $env_name --file environment.yaml && \
eval "$(conda shell.bash hook)" && \
conda activate $env_name && \
python setup.py install && \
greeter-service