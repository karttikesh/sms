from django.db import models
from account.models import User

# Create your models here.
class School(models.Model):
    STATE_CHOICES = (
        ('AP', 'Andhra Pradesh'),
        ('AP', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CG', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangāna'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal')
    )
    CITY_CHOICES = (
        ('AR', 'Araria'),
        ('AW', 'Arwal'),
        ('AU', 'Aurangabad'),
        ('BN', 'Banka'),
        ('BG', 'Begusarai'),
        ('BH', 'Bhagalpur'),
        ('BJ', 'Bhojpur'),
        ('BX', 'Buxar'),
        ('DB', 'Darbhanga'),
        ('EC', 'East Champaran'),
        ('GY', 'Gaya'),
        ('GJ', 'Gopalganj'),
        ('JM', 'Jamui'),
        ('JB', 'Jehanabad'),
        ('KM', 'Kaimur'),
        ('KT', 'Katihar'),
        ('KG', 'Khagaria'),
        ('KG', 'Kishanganj'),
        ('LS', 'Lakhisarai'),
        ('MD', 'Madhepura'),
        ('MB', 'Madhubani'),
        ('MG', 'Munger'),
        ('MZ', 'Muzaffarpur'),
        ('NL', 'Nalanda'),
        ('NW', 'Nawada'),
        ('PT', 'Patna'),
        ('PR', 'Purnia'),
        ('RT', 'Rohtas'),
        ('SH', 'Saharsa'),
        ('SM', 'Samastipur'),
        ('SH', 'Sheohar'),
        ('SK', 'Sheikhpura'),
        ('SR', 'Saran'),
        ('ST', 'Sitamarhi'),
        ('SP', 'Supaul'),
        ('SW', 'Siwan'),
        ('VS', 'Vaishali'),
        ('WC', 'West Champaran')
    )
    name = models.CharField(max_length=200)
    address = models.TextField()
    state = models.CharField(max_length=100, choices=STATE_CHOICES)
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    extra_field = models.JSONField(default=dict, null=True, blank=True)
    
    def __str__(self):
        return self.name