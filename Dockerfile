FROM registry.redhat.io/ubi9/python-311

EXPOSE 12312

VOLUME /config

COPY syslogserver.py /opt/app-root/src/

USER root

RUN dnf -y update \
 && dnf clean all

USER default

CMD ["python3", "syslogserver.py"]
