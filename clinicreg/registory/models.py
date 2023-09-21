from django.db import models



class DoctorSpecialty(models.Model):
    name = models.CharField(max_length=30, unique=True)


    class Meta:
        verbose_name ='specialty'
        verbose_name_plural = 'specialties'

    def __str__(self):
        return self.name or ''

class Doctor (models.Model):
    lastname = models.CharField(max_length=30)
    spec = models.ForeignKey(DoctorSpecialty,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'doctor'
        verbose_name_plural = 'doctors'

    def __str__(self):
        return self.lastname or ''


class Claim(models.Model):
    nickname=models.CharField(max_length=30)
    doc = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    problem_description = models.TextField(blank=True)
    visittime = models.DateTimeField()
    otherdocs=models.ManyToManyField(Doctor,related_name='docts')

    class Meta:
        verbose_name = 'claim'
        verbose_name_plural = 'claims'

    def __str__(self):
        return self.nickname or ''





