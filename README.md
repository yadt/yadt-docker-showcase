yadt-docker-showcase
====================

or: *yadt meets docker*

Prerequisites
-------------

* [docker](https://www.docker.io/): *an open source project to pack, ship and run any application as a lightweight container*
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
```
