from django.db import models


class Question(models.Model):
    """"@remember to change my class name"""
    content_management_service_1 = models.CharField(
        max_length=150, default='Service Item')
    content_management_service_2 = models.CharField(
        max_length=150, default='Service Item')
    content_management_service_3 = models.CharField(
        max_length=150, default='Service Item')
    content_management_service_4 = models.CharField(
        max_length=150, default='Service Item')
    content_management_service_5 = models.CharField(
        max_length=150, default='Service Item')
    content_management_service_6 = models.CharField(
        max_length=150, default='Service Item')
    content_management_service_7 = models.CharField(
        max_length=150, default='Service Item')
    content_management_service_8 = models.CharField(
        max_length=150, default='Service Item')
    content_management_service_9 = models.CharField(
        max_length=150, default='Service Item')
    content_management_service_10 = models.CharField(
        max_length=150, default='Service Item')

    def __str__(self):
        return self.content_management_service_1

    class Meta:
        verbose_name = 'Content Management Items'
        verbose_name_plural = 'Content Management'


