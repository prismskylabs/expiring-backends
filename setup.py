from setuptools import setup


def read(filename):
    with open(filename) as f:
        return f.read()

setup(
    name='expiring-backends',
    version='0.0.1',
    packages=['expiring_backends', ],
    author='Prism Skylabs',
    author_email='dev@prism.com',
    description='django-storages s3boto subclass for absolute URL expiration',
    url='https://github.com/prismskylabs/expiring-backends',
    install_requires=[
        'django-storages',
    ],
    test_suite='tests',
    zip_safe=False
)
