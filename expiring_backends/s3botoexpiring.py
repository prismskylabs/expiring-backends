from datetime import datetime, timedelta
import time

from django.utils.deconstruct import deconstructible

from storages.backends import S3BotoStorage


def midnight_tomorrow():
    # Brute-force calculates unix timestamp of midnight UTC "tomorrow"
    # where tomorrow is "at least one day away"
    two_days = 172800  # 3600 * 24 * 2
    offset = timedelta(seconds=two_days)
    tomorrow = datetime.utcnow().replace(hour=0, minute=0, second=0) + offset
    return int(round(time.mktime(tomorrow.timetuple())))


@deconstructible
class S3BotoExpiringStorage(S3BotoStorage):

    def url(self, name, headers=None, response_headers=None):
        name = self._normalize_name(self._clean_name(name))

        # this option from S3BotoStorage is not supported with signed URLs for now
        # if self.custom_domain:
        #     return "%s//%s/%s" % (self.url_protocol,
        #                           self.custom_domain, filepath_to_uri(name))

        return self.connection.generate_url(
            midnight_tomorrow(),
            method='GET',
            bucket=self.bucket.name,
            key=self._encode_name(name),
            headers=headers,
            query_auth=self.querystring_auth,
            force_http=not self.secure_urls,
            response_headers=response_headers,
            expires_in_absolute=True
        )
