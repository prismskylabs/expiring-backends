import mock
import datetime
import time

from django.test import TestCase

from expiring_backends import s3botoexpiring

__all__ = (
    'S3BotoExpiringTestCase',
)


# copied from https://github.com/jschneier/django-storages/blob/master/tests/test_s3boto.py
class S3BotoTestCase(TestCase):
    @mock.patch('storages.backends.s3boto.S3Connection')
    def setUp(self, S3Connection):
        self.storage = s3botoexpiring.S3BotoExpiringStorage()
        self.storage._connection = mock.MagicMock()


class S3BotoExpiringTestCase(S3BotoTestCase):
    def test_storage_url(self):
        """
        Test saving a file with expires_in_absolute set
        """
        name = 'test_storage_expiration.txt'
        url = 'http://aws.amazon.com/%s' % name
        self.storage.connection.generate_url.return_value = url
        self.assertEquals(self.storage.url(name), url)
        offset = datetime.timedelta(seconds=172800)
        midnight_tomorrow = datetime.datetime.utcnow().replace(hour=0, minute=0, second=0) + offset
        midnight_tomorrow_epoch = int(round(time.mktime(midnight_tomorrow.timetuple())))
        self.storage.connection.generate_url.assert_called_with(
            midnight_tomorrow_epoch,
            method='GET',
            bucket=self.storage.bucket.name,
            key=name,
            query_auth=self.storage.querystring_auth,
            force_http=not self.storage.secure_urls,
            headers=None,
            response_headers=None,
            expires_in_absolute=True
        )
