from django.db import models
from django.utils.text import slugify

# Create your models here.





class machine(models.Model):
    manu = models.CharField(max_length=64, default='Haddad')
    modell = models.CharField(max_length=64,default='Ultradreher')
    year = models.IntegerField(default=2016) 
    name = models.CharField(max_length=64)
    domain = models.SlugField(unique=True)
    desc = models.TextField(null=True, blank=True)
    image = models.ImageField(default='machine/default.png', upload_to='machine')
    model = models.BinaryField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.domain:
            t_slug = slugify(self.name)
            origin = 1
            unique_slug = t_slug
            while machine.objects.filter(domain=unique_slug).exists():
                unique_slug = '{} {}'.format(t_slug, origin)
                origin += 1
            self.domain = unique_slug
        super().save(*args, **kwargs)

class product_typ(models.Model):
    name = models.CharField(max_length=64)
    time = models.FloatField(default=10)

    def __str__(self):
        return self.name

class production(models.Model):
    product = models.ForeignKey(product_typ, default=None,blank=True, null=True, on_delete=models.CASCADE)
    machine = models.ForeignKey(machine, default=None,blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    tooltime = models.FloatField()
    machinetime = models.FloatField()
    tolarance = models.FloatField()

class order(models.Model):
    product = models.ForeignKey(product_typ, default=None, on_delete=models.CASCADE)
    machine = models.ForeignKey(machine, default=None,blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class tool_change(models.Model):
    machine = models.ForeignKey(machine, default=None,blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)