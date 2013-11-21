FROM yadt/base

ADD res/ /

# yadtshell
RUN yum install -y dummy-config yadtshell yadtbroadcast-client

# dnsmasq
RUN yum install -y dnsmasq

# default: bash
CMD /bin/bash
