from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "TestModel"
        verbose_name_plural = "TestModels"

    def __unicode__(self):
        return self.name