from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ We want to store static files in a specific location """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ We want to store media files in a specific location """
    location = settings.MEDIAFILES_LOCATION
