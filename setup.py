from distutils.core import setup

setup(
    name='ParadoxTrading',
    version='0.0.1',
    author='hantian.pang',
    packages=[
        'ParadoxTrading',
        'ParadoxTrading/Chart',
        'ParadoxTrading/Engine',
        'ParadoxTrading/Utils',
        'ParadoxTrading/Indicator/Basic',
        'ParadoxTrading/Indicator/General',
    ],
    install_requires=[
        'tabulate',
        'h5py',
        'psycopg2',
        'pymongo',
        'PyQt5',
        'PyQtChart',
    ]
)