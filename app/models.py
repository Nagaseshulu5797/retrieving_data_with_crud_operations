from django.db import models

# Create your models here.


class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=20,null=False)
    loc=models.CharField(max_length=20,null=False)

    def __str__(self):
        return str(self.deptno)
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=20)
    job=models.CharField(max_length=20)
    mgr=models.IntegerField()
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField(null=True,blank=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)


    def __str__(self):
        return self.ename