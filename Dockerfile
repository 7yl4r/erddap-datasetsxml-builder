# Base image
FROM python:3

# installes required packages for our script
# RUN	apk add --no-cache \
#   bash \
#   ca-certificates \
#   jq

RUN mkdir erddap_datasetsxml_builder
COPY . erddap_datasetsxml_builder/

# ensure entrypoint script is executable
RUN chmod +x erddap_datasetsxml_builder/entrypoint.sh

# install poetry for installing the python package
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir poetry \
 && poetry config settings.virtualenvs.create false
# install the python package
RUN cd erddap_datasetsxml_builder && poetry install --no-dev

# file to execute when the docker container starts up
ENTRYPOINT ["erddap_datasetsxml_builder/entrypoint.sh"]
