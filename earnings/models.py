from django.db import models

class Earnings(models.Model):
	workedYears=models.DecimalField(max_digits=3, decimal_places=1)
	salaryBrutto=models.DecimalField(max_digits=5, decimal_places=0)
	
	def __str__(self):
		return '%d przepracowanych lat: %d zl' %(self.workedYears, self.salaryBrutto)
		
