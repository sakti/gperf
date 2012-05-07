from setuptools import setup, find_packages

install_requires = [
    'matplotlib'
]


setup(
    name='gperf',
    version='0.2',
    packages=find_packages(),
    license='BSD',
    author='Sakti Dwi Cahyono',
    author_email='54krpl at gmail dot com',
    keywords='sar sysstat time-based graph',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion'
        ],
    entry_points={'console_scripts':['gperf = gperf.gperf:main']},
    description='Graphing from sysstat sar data into time-based graph',
    long_description=open('README.rst').read(),
    url='https://github.com/sakti/gperf',
)
