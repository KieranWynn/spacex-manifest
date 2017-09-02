"""A microservice acting as a source of info on all SpaceX flights to date. This content is not endorsed by SpaceX
and should not be treated as official information. This is a personal project only.
See:
https://github.com/KieranWynn/spacex-manifest
"""

from setuptools import setup

setup(
    name='spacex_manifest',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',

    description='A fully featured, pythonic library for representing and using quaternions.',
    long_description="A fully featured, pythonic library for quaternion representation, manipulation, 3D animation and geometry.",

    # The project's main homepage.
    #download_url='https://github.com/KieranWynn/spacex-manifest/tarball/0.1.0',
    url='https://github.com/KieranWynn/spacex-manifest',

    # Author details
    author='Kieran Wynn',
    author_email='KieranWynn@users.noreply.github.com',

    # Choose your license
    license='MIT',

    # What does your project relate to?
    keywords=['spacex', 'physics'],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['spacex_manifest'],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'Flask-API',
        'sqlalchemy',
        'psycopg2'
    ],

    # Set Pytest as a requirement for running tests
    tests_require=[
        'pytest',
        'requests',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={},

)
