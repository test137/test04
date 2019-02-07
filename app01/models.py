from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=32)
    price_policy_list = GenericRelation("PricePolicy")


class DegreeCourse(models.Model):
    title = models.CharField(max_length=32)
    price_policy_list = GenericRelation("PricePolicy")

class PricePolicy(models.Model):
    price = models.IntegerField()
    period = models.IntegerField()

    # table_name = models.CharField(verbose_name='table_name')
    # object_id = models.CharField(verbose_name='class_id')

    content_type = models.ForeignKey(ContentType, verbose_name='table_name', on_delete=models.CASCADE)
    object_id = models.IntegerField(verbose_name='class_id')

    content_object = GenericForeignKey('content_type', 'object_id')
