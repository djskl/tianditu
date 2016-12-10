#!/usr/bin/env bash

fuser -k 9090/tcp

fuser -k 9091/tcp

fuser -k 9092/tcp

fuser -k 9093/tcp

fuser -k 9094/tcp

fuser -k 9095/tcp

fuser -k 9096/tcp

fuser -k 9097/tcp

root_dir="$(dirname "$0")"

cd ${root_dir}"/t0"

truncate -s 0 tdt.logs
uwsgi --ini uwsgi.ini

cd "../t1"
truncate -s 0 tdt.logs
uwsgi --ini uwsgi.ini

cd "../t2"
truncate -s 0 tdt.logs
uwsgi --ini uwsgi.ini

cd "../t3"
truncate -s 0 tdt.logs
uwsgi --ini uwsgi.ini

cd "../t4"
truncate -s 0 tdt.logs
uwsgi --ini uwsgi.ini

cd "../t5"
truncate -s 0 tdt.logs
uwsgi --ini uwsgi.ini

cd "../t6"
truncate -s 0 tdt.logs
uwsgi --ini uwsgi.ini

cd "../t7"
truncate -s 0 tdt.logs
uwsgi --ini uwsgi.ini
