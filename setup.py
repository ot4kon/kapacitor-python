import setuptools

long_description = ''
with open('README.md') as f:
  long_description = f.read()

# TODO: read requirements file here
requires=['requests==2.22.0', 'six==1.12.0']
test_requires=['mock', 'nose']

setuptools.setup(
    name='kapacitor',
    version='0.0.1',
    author='ot4kon',
    author_email='hubgrt.hubgrt@gmail.com',
    description='Simple Kapacitor Client',
    long_description=long_description,
    url='https://github.com/ot4kon/kapacitor-python',
    license='MIT License',
    packages=setuptools.find_packages(exclude=['tests']),
    test_suite='tests',
    tests_require=test_requires,
    install_requires=requires,
    extras_require={'test': test_requires},
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
