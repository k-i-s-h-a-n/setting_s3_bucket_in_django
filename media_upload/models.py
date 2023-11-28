# # models.py in your media_upload app

# from django.db import models

# class UploadedFile(models.Model):
#     file = models.FileField(upload_to='LCM/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.file.name


from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.core.files.storage import default_storage

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

    def delete(self, *args, **kwargs):
        # Delete the file from S3 when the model instance is deleted
        self.file.delete(save=False)  # This will not call save() method
        super().delete(*args, **kwargs)

# Signal to delete the file from S3 when the model instance is deleted
@receiver(post_delete, sender=UploadedFile)
def delete_file_from_s3(sender, instance, **kwargs):
    if instance.file:
        if default_storage.exists(instance.file.name):
            default_storage.delete(instance.file.name)
