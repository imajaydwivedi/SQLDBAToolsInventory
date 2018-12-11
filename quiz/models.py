from django.db import models

# Create your models here.

class Questiontechnology(models.Model):
    technologyid = models.AutoField(primary_key=True)
    CATEGORY_CHOICES = (
        ('MSSQL', 'SQL Server'),
        ('MySQL', 'MySQL'),
        ('Oracle', 'Oracle'),
    )
    category = models.CharField(
        max_length=20, blank=True, null=True, choices=CATEGORY_CHOICES, default='MSSQL')
    SUBCATEGORY_CHOICES = (
        ('DEV', 'Development'),
        ('Admin', 'Administration'),
        ('Art', 'Architect'),
    )
    subcategory = models.CharField(max_length=20, blank=True, null=True, choices = SUBCATEGORY_CHOICES, default = 'Admin')
    LEVEL_CHOICES = (
        ('L1','Level 01 - Beginner'),
        ('L2','Level 02 - Intermediate'),
        ('L3','Level 03 - Expert'),
        ('L4','Level 04 - SME'),
    )
    # level = models.IntegerField(blank=True, null=True)
    level = models.CharField(max_length=8, blank=True, null=True, choices = LEVEL_CHOICES, default = 'L2')
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'QuestionTechnology'
