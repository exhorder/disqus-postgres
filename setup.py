import sys
import warnings

try:
    import multiprocessing
except:
    pass

try:
    from notsetuptools import setup
except ImportError:
    # If you are using namespaces you should **not** allow installation of your package without
    # using the ``notsetuptools`` package.
    warnings.warn('You are missing the ``notsetuptools`` package; falling back to ``setuptools``.')
    from setuptools import setup

from setuptools import find_packages


if 'nosetests' == sys.argv[1]:
    setup_requires = ['nose>=1.0']
else:
    setup_requires = []

tests_require = [
    'nose>=1.0',
    'mock==0.8',
    'unittest2==0.5.1',
]

requires = [
    'psycopg2'
]

entry_points = {
    # 'console_scripts': [
    #     'foo = my_package.some_module:main_func',
    #     'bar = other_module:some_func',
    # ],
}


setup(
    name='disqus-postgres',
    version='0.1.0',
    author="DISQUS",
    author_email="dev@disqus.com",
    package_dir={'': 'src'},
    packages=find_packages("src"),
    install_requires=requires,
    tests_require=tests_require,
    setup_requires=setup_requires,
    test_suite='nose.collector',
    entry_points=entry_points,
    zip_safe=False,
)