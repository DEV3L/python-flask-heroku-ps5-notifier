from setuptools import setup, find_packages

requirements = []

with open('requirements.txt') as file:
    for line in file:
        if line:
            requirements.append(line)

setup(
    name='python_flask_heroku_ps5_notifier',
    packages=find_packages(),
    version='0.1',
    description='A Python Flask application that can searches and notifies through Twillio when a PS5'
                ' console/digital is available.',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    url='https://github.com/DEV3L/python-flask-heroku-ps5-notifier',
    keywords=['dev3l', 'heroku', 'python', 'twillio', 'flask'],
    install_requires=[
        requirements
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
