from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3,blank=True)
    name = models.CharField(max_length=128,blank=True)
    to = models.CharField(max_length=3,blank=True)
    fromm = models.CharField(max_length=3,blank=True)
        
class Flight(models.Model):
    flight_number = models.CharField(max_length=2048,blank=True)
    take_off = models.DateTimeField(auto_now_add=False)
    landing = models.DateTimeField(auto_now_add=False)
    to = models.ForeignKey(Airport,max_length=3,on_delete=models.DO_NOTHING, null=True, blank=True,related_name="where")
    fromm = models.ForeignKey(Airport,max_length=3,on_delete=models.DO_NOTHING, null=True, blank=True, related_name="going")
    
    def __str__(self):
        return self.flight_number
