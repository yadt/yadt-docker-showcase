FROM centos

# add local repo
#ADD res/repo-base /repo-base
#ADD res/etc/yum.repos.d/ /etc/yum.repos.d/
ADD res/ /

# install epel repos
RUN yum install -y /repo-base/epel-*.rpm

# update to latest
RUN yum update -y

# install/configure sshd
RUN yum install -y openssh-server
RUN mkdir /var/run/sshd/
RUN sed -ri "s/^#PermitRootLogin yes/PermitRootLogin yes/g;s/^UsePAM yes/#UsePAM yes/g;s/^#UsePAM no/UsePAM no/g;" /etc/ssh/sshd_config
RUN service sshd start

# install/configure ssh + keys
RUN yum install -y openssh-clients
RUN ssh-keygen -q -t rsa -f /root/.ssh/id_rsa -N ""
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys

# install/configure sudo
RUN yum install -y sudo
RUN sed -ri '/^Defaults[[:space:]]*requiretty/s/^/#/' /etc/sudoers
