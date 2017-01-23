# expiring-backends

Django storage backend that subclasses S3BotoStorage from https://github.com/jschneier/django-storages to add boto 2.x "expires_in_absolute" functionality.

This generates the same URL for a signed S3 request for up to a day, making it easier for browsers/proxies to cache content served from S3.
 
The code here is largely based on discussion in tickets on the django-storages project and was placed here so that:
 
* it didn't need to be merged into django-storages, potentially breaking other parts
* it wouldn't be stuck on an ancient fork of django-storages

## Installation

Not on pypi and don't plan to be.

        pip install git+https://github.com/prismskylabs/expiring-backends.git

## Configuration

In your Django settings module, set:
 
        DEFAULT_FILE_STORAGE = 'expiring_backends.s3botoexpiring.S3BotoExpiringStorage'

Old versions that were patched into django-storages modified their behavior based on ``AWS_QUERYSTRING_ABSOLUTE_EXPIRE_MODE`` set to ``True`` in the Django settings module, but now it is assumed if you use this Storages backend then it is assumed you want absolute expiration.
