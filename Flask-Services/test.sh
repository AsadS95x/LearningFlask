#!/bin.bash

declare -a dirs=(Service1 Service2 Service3 Service4)

for dir in ${dirs[@]}; do
    cd ${dir}
    pip3 install -r requirements.txt
    python3 -m pytest --cov=application --cov-report=html
    cd ..
done



