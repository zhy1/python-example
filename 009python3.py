#-*- coding: utf-8 -*-  
#coding=utf-8


UPDATE: This is no longer necessary with Python3.4. It installs pip3 as part of the stock install.

I ended up posting this same question on the python mailing list, and got the following answer:

# download and install setuptools
curl -O https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
python3 ez_setup.py
# download and install pip
curl -O https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
python3 get-pip.py
Which solved my question perfectly. After adding the following for my own:

cd /usr/local/bin
ln -s ../../../Library/Frameworks/Python.framework/Versions/3.3/bin/pip pip
So that I could run pip directly, I was able to:

# use pip to install
pip install pyserial
or:

# Don't want it?
pip uninstall pyserial