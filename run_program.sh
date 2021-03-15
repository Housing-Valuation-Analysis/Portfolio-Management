#! /bin/sh
#Shell script to run program with one command after repo cloned

python3 setup.py install
pip3 install -r requirements.txt
python3 ./stocks/manage.py runserver