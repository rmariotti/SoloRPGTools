import setuptools
import os

ASSETS_DIR = 'assets'
datafiles = [(d, [os.path.join(d,f) for f in files]) for d, folders, files in os.walk(ASSETS_DIR)]

setuptools.setup(
    name='SoloRPGTools',
    version='0.0.1',
    license='BSD-2-Clause',
    description='Useful tools for solo roleplaying in Jupyter Notebook.',
    packages=[
        'card',
        'character',
        'constants',
        'dice',
        'game',
        'quest',
        'table',
        'render'
    ],
    package_dir={'': 'src'},
    data_files = datafiles,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'solorpgtools=main:main',
        ],
    }
)