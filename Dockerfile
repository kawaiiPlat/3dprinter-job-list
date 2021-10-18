FROM ubuntu:18.04
RUN apt-get update-y && apt-get install -y python-pip python-dev && apt-get install -y git vim
CMD ["/bin/bash"]
WORKDIR /test_container
VOLUME [ "/test_container" ]