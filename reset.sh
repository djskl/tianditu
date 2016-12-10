#!/usr/bin/env bash

root_dir="$(dirname "$0")"

cd $root_dir

#echo "---------- pulling source code..."
git pull

echo "---------- python setup.py install"
rm -rf /usr/lib/python2.7/site-packages/tianditu-1.0-py2.7.egg
python setup.py install
rm -rf build
rm -rf dist
rm -rf tianditu.egg-info
