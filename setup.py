from codecs import open

from setuptools import setup, find_packages


setup(
    name="django-evostream",
    version='0.1',
    author="Tomasz Jakub Rup",
    author_email="tomasz.rup@gmail.com",
    url='https://github.com/tomi77/django-evostream',
    description='Manage EvoStream Media Server',
    long_description=open("README.md").read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    license='MIT',
    packages=find_packages()
)
