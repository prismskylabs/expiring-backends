# expiring-backends

Django storage backend that subclasses S3BotoStorage from https://github.com/jschneier/django-storages to add boto 2.x "expires_in_absolute" functionality.

This generates the same URL for a signed S3 request for up to a day, making it easier for browsers/proxies to cache content served from S3.
 
The code here is largely based on discussion in tickets on the django-storages project and was placed here so that:
 
* it didn't need to be merged into django-storages, potentially breaking other parts
* it wouldn't be stuck on an ancient fork of django-storages
