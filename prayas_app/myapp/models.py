from django.db import models
from django.utils.translation import gettext as _

from django.core.validators import MinLengthValidator

# Create your models here.
class Donor(models.Model):
    donor_name = models.CharField(max_length=255, null=False, help_text=_('Please enter your name'), default= None, editable=False,)
    unique_id = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(10)],
        help_text=_('Donor ID'),
        primary_key= True,
        default=None,
        editable=False,
        )
    contact_number = models.CharField(max_length= 255, null=False, blank=False, unique=True, editable=False,)
    blood_group = models.CharField(max_length= 10, help_text=_("Enter donor's blood group"), editable=False,)
    city= models.CharField(max_length= 255, help_text=_("Which city will you be at the time of donation"), editable=False,)
    A= 'Less than 5 days'
    B= '5 to 15 days'
    C= '15 to 30 days'
    D= '30 days to 4 months'
    E= 'Greater than 4 months'
    time_choices= ( (A, 'Less than 5 days'), (B, '5 to 15 days'), (C, '15 to 30 days'), (D, '30 days to 4 months'), (E, 'Greater than 4 months'))
    time_post_recovery= models.CharField(max_length= 255, choices= time_choices, help_text=_('Please select the time passed since recovery'), editable = True,)
    num_days= models.IntegerField(help_text=_('Please enter the number of days since recovery'), null=False, editable= True,)
    email= models.EmailField(max_length= 255, help_text=_('Please enter your email id'), )
    YES= 'Yes'
    NO= 'No'
    CANNOT= 'Cannot donate'
    donate_choices= ((YES, 'Yes'), (NO, 'No'), (CANNOT, 'Cannot donate'))
    has_donated=models.CharField(max_length= 255, choices=donate_choices, help_text=_('Has the person donated?'), editable= True,)
    comments= models.CharField(max_length= 255,)
    
