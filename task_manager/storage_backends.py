from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = None  # Usa la configuración por defecto del bucket
    file_overwrite = True
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIA_LOCATION
    default_acl = None  # Usa la configuración por defecto del bucket
    file_overwrite = False
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME