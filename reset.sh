#!/usr/bin/env bash

echo "---------- fuser -k 9090/tcp"
fuser -k 9090/tcp

echo "---------- fuser -k 9091/tcp"
fuser -k 9091/tcp

echo "---------- fuser -k 9092/tcp"
fuser -k 9092/tcp

echo "---------- fuser -k 9093/tcp"
fuser -k 9093/tcp

echo "---------- fuser -k 9094/tcp"
fuser -k 9094/tcp

echo "---------- fuser -k 9095/tcp"
fuser -k 9095/tcp

echo "---------- fuser -k 9096/tcp"
fuser -k 9096/tcp

echo "---------- fuser -k 9097/tcp"
fuser -k 9097/tcp


root_dir="$(dirname "$0")"

cd $root_dir

echo "---------- pulling source code..."
git reset --hard origin/master
git clean -f
git pull
git checkout master

echo "---------- python setup.py install"
rm -rf /usr/lib/python2.7/site-packages/tianditu-1.0-py2.7.egg
python setup.py install