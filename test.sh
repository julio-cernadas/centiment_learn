#!/usr/bin/env bash

clear
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
rm master.db
python3 setup/schema.py
echo "Starting test server"
echo ""
python3 run/wsgi.py
