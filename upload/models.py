from django.db import models
from django.core.validators import FileExtensionValidator


class Document(models.Model):
    document = models.FileField(verbose_name="Arquivo",
                                validators=[FileExtensionValidator(allowed_extensions=['xlsx', 'xls'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    imported = models.BooleanField(default=False)
