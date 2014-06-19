from setuptools import setup

setup(
    name='onetimepad',
    
    version='1.2',
    description='A hacky implementation of One-time pad',
    long_description=open('README.rst').read(),

    py_modules=['onetimepad'],

    url='http://jailuthra.in/onetimepad',
    author='Jai Luthra',
    author_email='me@jailuthra.in',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Topic :: Security :: Cryptography',
    ],

    entry_points={
        'console_scripts': [
            'onetimepad = onetimepad:main',
        ],
    },
)
