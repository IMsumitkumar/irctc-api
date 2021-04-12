from django.db import models

# Create your models here.
class Travel(models.Model):
    FROM = [
        ('Andhra Pradesh','Andhra Pradesh'),
        ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
        ('Arunachal Pradesh','Arunachal Pradesh'),
        ('Assam','Assam'),
        ('Bihar','Bihar'),
        ('Chandigarh','Chandigarh'),
        ('Chhattisgarh','Chhattisgarh'), 
        ('Dadar and Nagar Haveli','Dadar and Nagar Haveli'),
        ('Daman and Diu','Daman and Diu'), 
        ('Delhi', 'Delhi'), 
        ('Lakshadweep','Lakshadweep'), 
        ('Puducherry','Puducherry'), 
        ('Goa','Goa'), 
        ('Gujarat','Gujarat'),
        ('Haryana','Haryana'),
        ('Himachal Pradesh','Himachal Pradesh'), 
        ('Jammu and Kashmir','Jammu and Kashmir'), 
        ('Jharkhand','Jharkhand'), 
        ('Karnataka', 'Karnataka'),
        ('Kerala','Kerala'), 
        ('Madhya Pradesh','Madhya Pradesh')
    ]
    TO = [
        ('Andhra Pradesh','Andhra Pradesh'),
        ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
        ('Arunachal Pradesh','Arunachal Pradesh'),
        ('Assam','Assam'),
        ('Bihar','Bihar'),
        ('Chandigarh','Chandigarh'),
        ('Chhattisgarh','Chhattisgarh'), 
        ('Dadar and Nagar Haveli','Dadar and Nagar Haveli'),
        ('Daman and Diu','Daman and Diu'), 
        ('Delhi', 'Delhi'), 
        ('Lakshadweep','Lakshadweep'), 
        ('Puducherry','Puducherry'), 
        ('Goa','Goa'), 
        ('Gujarat','Gujarat'),
        ('Haryana','Haryana'),
        ('Himachal Pradesh','Himachal Pradesh'), 
        ('Jammu and Kashmir','Jammu and Kashmir'), 
        ('Jharkhand','Jharkhand'), 
        ('Karnataka', 'Karnataka'),
        ('Kerala','Kerala'), 
        ('Madhya Pradesh','Madhya Pradesh')
    ]
    SEC = [
           ('EA','Anubhuti Class(EA)'),
           ('1A','AC First Class(1A)'), 
           ('EC','Exec. Chair Car(EC)'),
           ('2A', 'AC 2Tier (2A)'), 
           ('FC','First CLass(FC)'),
           ('3A','AC 3 Tier(3A)'),
           ('3E','AC 3Economy (3E)'),
           ('CC','AC Chair car(CC)')
        ]

    d_from = models.CharField(choices = FROM, max_length=50, default='Assam')
    d_to = models.CharField(choices = TO, max_length=50, default='Assam')
    date = models.DateField(auto_now_add = False)
    section = models.CharField(choices = SEC, max_length=50, default='EA')

    concession = models.BooleanField(default=False)
    with_data = models.BooleanField(default=False)
    train_available = models.BooleanField(default=False)

    def __str__(self):
        return self.section


