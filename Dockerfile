# Base image
FROM python:3

# installes required packages for our script
# RUN	apk add --no-cache \
#   bash \
#   ca-certificates \
#   jq

COPY ./* ./erddap_datasetsxml_builder/.
    
# ensure entrypoint script is executable
RUN chmod +x ./erddap_datasetsxml_builder/entrypoint.sh

# install the package
RUN cd ./erddap_datasetsxml_builder && python -m pip install -e .

# file to execute when the docker container starts up
ENTRYPOINT ["./erddap_datasetsxml_builder/entrypoint.sh"]
