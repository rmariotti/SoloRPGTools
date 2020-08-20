import setuptools
import os

ASSETS_DIR = 'assets'
datafiles = [(d, [os.path.join(d,f) for f in files]) for d, folders, files in os.walk(ASSETS_DIR)]

class CleanCommand(setuptools.Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')

setuptools.setup(
    name='SoloRPGTools',
    version='0.0.1',
    license='BSD-2-Clause',
    description='Useful tools for solo roleplaying in Jupyter Notebook.',
    packages=setuptools.find_packages(where="./src"),
    package_dir={'': 'src'},
    data_files = datafiles,
    include_package_data=True,
    entry_points={
        'console_scripts': ['solorpgtools=cmd_scripts.new_game:main'],
    },
    cmdclass={
        'clean': CleanCommand,
    }
)
