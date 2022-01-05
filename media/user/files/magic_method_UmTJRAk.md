magic_method
======
<div dir="rtl">
مجیک متود یا داندر متود ها تابع های خاصی هستند که میتوانید در طراحی کلاس از آن هااستفاده کنید.مجیک متودها با دابل اندر اسکور مشخص می شوند.ومی توانید با دستورات built inبایتون فراخوانی شود





<div dir="rtl">
1-subclasscheck

این متود چک می کند که آیا کلاس مورد نظر زیر مجموعه یک کلاس دیگر هست یا نه و true,false بر می گرداند همیچنین می توان آن را با دستور ()issubclass صدا کنید.

class A:
  pass

class B(A):
  pass
  
issubclass(A,B)-> False

issubclass(B,A)->True
<div dir="rtl">
2-instancecheck

این تابع چک می کند آیا آبجکت مورد نظر نمونه ای از کلاس مورد نظر است یا نه.
class A:
    pass

a = A()

isinstance(a,A)->True
<div dir="rtl">
3-__dir__

این تابع که با دستور ()dir نیز فرا خوانده می شود یک لیست از تمام متغیرها و متود های یک آبجکت بر می گردانند.





<div dir="rtl">
4-__repr__
با کمک این تابع میتوانید آبجکت ساخته شده از کلاستان را به صورت استرینگ نشان دهید.


class preson

  def __init__(self,name):
  
  self.name = name
  
  def __repr__(self):
  repr = "preson{"+self.name+"}"
  
preson1 = preson(mahdi)

print(repr(preson1))---> preson{mahdi}

<div dir="rtl">
5-__sizeof__

این تابع مقدار حافظه اشغال شده توسط بک آبجکت را نشان می دهد و می توان آن را با  دستور ()sys.getsizeof نیز فرا خواند.

        
        

