#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['artemis_sysmon'],
    package_dir={'': 'src'},
    scripts=['scripts/artemis_sysmon']
)

setup(**d)
