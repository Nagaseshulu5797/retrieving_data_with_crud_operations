from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def dispaly_dept(request):
    LOD=Dept.objects.all()
    d={'dept':LOD}
    return render(request,'dispaly_dept.html',d)

def display_emp(request):
    LOE=Emp.objects.all()

    #LOE=Emp.objects.get(sal='5000')
    LOE=Emp.objects.filter(sal='3000')
    LOE=Emp.objects.filter(deptno='30')

    #Below command arrange the ascending order
    LOE=Emp.objects.order_by('ename')

    #Below command arrange the descending order
    LOE=Emp.objects.order_by('-ename')

    # We can perform slicing also
    LOE=Emp.objects.all()[0:10:1]
    LOE=Emp.objects.all()[0::1]

    #We can asecnding order and descending order of legths
    LOE=Emp.objects.order_by(Length('ename').desc())
    LOE=Emp.objects.order_by(Length('ename'))

    #EXCLUDE
    #By using exclude whatever you dont want that can be removed
    LOE=Emp.objects.exclude(deptno='30')

    #FIELD LOOKUPS
    LOE=Emp.objects.filter(sal__gt='2000')
    LOE=Emp.objects.filter(sal__lt='3000')
    LOE=Emp.objects.filter(sal__gte='3000')
    LOE=Emp.objects.filter(sal__lte='1500')

    #DATE FORMATE
    LOE=Emp.objects.filter(hiredate__year='1981')
    LOE=Emp.objects.filter(hiredate__month='04')
    LOE=Emp.objects.filter(hiredate__day='03')

    #DATE FORMATE USING FIELD LOOKPS
    LOE=Emp.objects.filter(hiredate__month__lt='04')
    LOE=Emp.objects.filter(hiredate__month__gt='04')
    LOE=Emp.objects.filter(hiredate__month__lte='04')
    LOE=Emp.objects.filter(hiredate__month__gte='04')

    LOE=Emp.objects.filter(hiredate__year__lt='1981')
    LOE=Emp.objects.filter(hiredate__year__lte='1981')
    LOE=Emp.objects.filter(hiredate__year__gt='1981')
    LOE=Emp.objects.filter(hiredate__year__gte='1981')

    LOE=Emp.objects.filter(hiredate__day__lt='20')
    LOE=Emp.objects.filter(hiredate__day__lte='20')
    LOE=Emp.objects.filter(hiredate__day__gt='20')
    LOE=Emp.objects.filter(hiredate__day__gte='20')

    #Like Operations
    LOE=Emp.objects.filter(ename__startswith='s')
    LOE=Emp.objects.filter(ename__startswith='k')
    LOE=Emp.objects.filter(ename__endswith='h')
    LOE=Emp.objects.filter(ename__endswith='g')
    LOE=Emp.objects.filter(ename__contains='s')
    LOE=Emp.objects.filter(ename__in=('SMITH','ALLEN'))
    LOE=Emp.objects.filter(ename__regex='[a-zA-Z]{5}')
    LOE=Emp.objects.filter(Q(job='MANAGER') & Q(deptno=20))

    d={'emp':LOE}
    return render(request,'display_emp.html',d)

