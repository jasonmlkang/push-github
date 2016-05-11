try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as file:
    long_description = "Update README.md file on a github repository"

setup(
    name='update-github-readme',
    version='0.0.1',
    url='https://github.com/jasonmlkang/update-github-readme',
    description='Update README.md file on a github repository',
    author='Jason Kang',
    license='MIT',
    py_modules=['update_github_readme'],
    long_description=long_description,
    install_requires=[],
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
    entry_points = """
[console_scripts]
pushGithub = update_github_readme:run
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
