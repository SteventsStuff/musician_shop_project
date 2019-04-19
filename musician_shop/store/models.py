from django.db import models


import json


class Store(models.Model):
    objects = models.Manager()

    prod_title = models.CharField(max_length=50, verbose_name="Product name")
    prod_img = models.ImageField(blank=True, null=True, upload_to="prod_photos/%Y/%m/%D/",
                                 verbose_name="Product image")
    prod_description = models.TextField(null=True, blank=True, verbose_name="Product description")
    prod_materials = models.CharField(max_length=250, verbose_name="Made of", null=True, blank=True)
    prod_manufacturer_id = models.ForeignKey("Manufacturer", null=True,
                                             on_delete=models.CASCADE, verbose_name="Manufacturer")
    prod_year = models.CharField(max_length=4, null=True, blank=True)
    prod_currency = models.ForeignKey("Currency", on_delete=models.PROTECT, verbose_name="Currency")
    prod_price = models.DecimalField(max_digits=10, decimal_places=2)  # need to calculated!
    prod_availability = models.BooleanField(null=True, default=True)
    prod_analog = models.ForeignKey("Analog", null=True, on_delete=models.CASCADE, verbose_name="Analog")
    prod_accessories = models.ForeignKey("Accessories", null=True, on_delete=models.CASCADE, verbose_name="Accessories")
    prod_department = models.ForeignKey("Department", null=True, on_delete=models.CASCADE, verbose_name="Department")
    prod_comments = models.ForeignKey("Comments", null=True, on_delete=models.CASCADE, verbose_name="Comments")
    prod_rate = models.IntegerField(null=True, blank=True, verbose_name="Rate")  # need to calculated!

    # place to add cal funcs

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"
        ordering = ["-prod_title"]


class Manufacturer(models.Model):
    objects = models.Manager()

    manufac_name = models.CharField(max_length=50, db_index=True, verbose_name="Manufacturer name")
    manufac_country = models.CharField(max_length=60, verbose_name="Country")
    manufac_city = models.CharField(max_length=60, verbose_name="City")
    manufac_address = models.CharField(max_length=150, verbose_name="Address")
    manufac_email = models.EmailField(verbose_name="Email")
    manufac_phone = models.CharField(max_length=65, verbose_name="Contact phone")

    class Meta:
        verbose_name_plural = "Manufacturers"
        verbose_name = "Manufacturer"
        ordering = ["-manufac_name"]


class Currency(models.Model):
    cur_USD = models.DecimalField(max_digits=4, decimal_places=2)
    cur_EUR = models.DecimalField(max_digits=4, decimal_places=2)
    cur_UAH = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = "Currency"
        ordering = ["-cur_USD"]


class Analog(models.Model):
    analog_id_list = models.CharField(max_length=200)

    def set_analogs(self, x):
        self.analog_id_list = json.dumps(x)

    def get_analogs(self):
        return json.loads(self.analog_id_list)

    class Meta:
        verbose_name_plural = "Analogs"
        verbose_name = "Analog"


class Accessories(models.Model):
    accessories_id_list = models.CharField(max_length=200)

    def set_accessories(self, x):
        self.accessories_id_list = json.dumps(x)

    def get_accessories(self):
        return json.loads(self.accessories_id_list)

    class Meta:
        verbose_name = "Accessory"
        verbose_name_plural = "Accessories"


class Department(models.Model):
    department_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Departments"
        verbose_name = "Department"
        ordering = ["-department_name"]


class Comments(models.Model):
    content = models.TextField(null=True, blank=True, verbose_name="Content")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Published date")

    class Meta:
        verbose_name_plural = "Comments"
        verbose_name = "Comment"
        ordering = ["-published"]
