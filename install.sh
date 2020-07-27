#!/bin/bash
# TODO: - probably a more pythonic way exist

python setup.py sdist bdist_wheel
python setup.py install