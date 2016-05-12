try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as file:
    long_description = "Update a file on github"

setup(
    name='push-github',
    version='0.0.1',
    url='https://github.com/jasonmlkang/push-github',
    description='Update a file on github',
    author='Jason Min-Liang Kang',
    license='MIT',
    py_modules=['push_github'],
    long_description=long_description,
    install_requires=['requests==2.7.0'],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points="""
    [console_scripts]
    pushgithub = push_github:run
    """,
    options={
        'bdist_rpm':{
            'build_requires':[
                'python',
                'python-setuptools',
                'requests'
                ],
            'requires':[
                'python',
                'python-setuptools',
                'requests'
            ],
        },
    },
)
