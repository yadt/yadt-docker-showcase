FROM yadt/base

# add local repo
ADD res/repo-minion /repo-minion
ADD res/etc/yum.repos.d/ /etc/yum.repos.d/

# install yadt-minion
RUN yum install -y yadt-minion

# disable all remote repos
RUN mv /etc/yum.repos.d/CentOS*.repo /etc/yum.repos.d/epel*.repo /tmp

# define default command
CMD /usr/sbin/sshd -D
