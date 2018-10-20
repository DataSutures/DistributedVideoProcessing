FROM bvlc/caffe:cpu
MAINTAINER datasutures "datasutures@gmail.com"

ENV TERM=xterm\
    TZ=US\
    DEBIAN_FRONTEND=noninteractive

ADD colorize.py

RUN apt-get update \
  && apt-get install -y python-tk \
  && git clone -b master --single-branch https://github.com/richzhang/colorization.git \
  && mv colorize.py ./colorization/colorization/colorize.py \
  && cd ./colorization \
  && /models/fetch_release_models.sh
  
WORKDIR /workspace/colorization/colorization

