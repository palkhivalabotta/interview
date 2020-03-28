from django.db import models


class members(models.Model):
    user_id=models.CharField(max_length=10)
    real_name=models.CharField(max_length=50)
    location=models.CharField(max_length=200)
    #activity=models.OneToOneField(active_periods,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id


class active_periods(models.Model):
    start_time=models.DateTimeField(auto_now_add=False)
    end_time=models.DateTimeField(auto_now_add=False)
    Members = models.ForeignKey(members, on_delete=models.CASCADE, default=False)


