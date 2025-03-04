from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import F, Func, Sum
from django.db.models.sql import Query


# Create your models here.

class AssetsModel(models.Model):
    interest_rate = models.FloatField(null=False, blank=False, default=21.0, verbose_name=u'Процентная ставка')
    dividend_stock = models.PositiveIntegerField(verbose_name=u'Дивидендные акции', validators = [MinValueValidator(0)])
    growth_stock = models.PositiveIntegerField(verbose_name=u'Акции роста',validators = [MinValueValidator(0)])
    state_bond = models.PositiveIntegerField(verbose_name=u'ОФЗ',validators = [MinValueValidator(0)])
    corporate_floater = models.PositiveIntegerField(verbose_name=u'Корпоративные флоатеры',validators = [MinValueValidator(0)])
    gold = models.PositiveIntegerField(verbose_name=u'Золото',validators = [MinValueValidator(0)])
    
    

    # For returning data in ADMIN SITE
    def __str__(self):
        return "AssetsModel"
    

    

        
        
    
    
        
   


    
    