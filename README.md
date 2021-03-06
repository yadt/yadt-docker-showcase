yadt-docker-showcase
====================

or: *yadt meets docker*


Prerequisites
-------------

* [docker](https://www.docker.io/): *an open source project to pack, ship and run any application as a lightweight container*
  * (strongly recommended) use docker as [non-root user](http://docs.docker.io/en/latest/use/basics/#why-sudo)

* [bash](http://www.gnu.org/software/bash/) *Bash is the shell, or command language interpreter, that will appear in the GNU operating system.*


tl;dr
-----

```bash
# download base image, update to newest versions, create several images
# for different yadt roles (minion, shell, broadcaster, ...)
./build-containers


# (re)starts docker daemon, configures web ui
# visit http://localhost:9000/
./prepare-showcase


# starts yadt showcase: 5 minions, and one broadcaster
# visit http://localhost:8080/hosts-overview.html?target=showcase&col_width=10
./start-showcase 5 maxcols


# do something with yadtshell, for example:
start service://* -p 5

stop service://minion*/*

# ...
```

for more commands, see the
[cheatsheet](http://www.yadt-project.org/cheatsheet-0.2.pdf)
and the [wiki](https://github.com/yadt/yadtshell/wiki).

```bash
# when getting tired of yadt:
# stop all minions, simply run
./stop-showcase

# then exit the yadtshell with
exit
```


Next Steps
----------

* improving documentation
* creating a dedicated vagrant box (so you dont have to fiddle around with docker installations)
* more robust start- and stop-showcase scripts

* refactoring the yadtshell system tests

