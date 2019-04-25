from django.db import models


class Store(models.Model):
    objects = models.Manager()
    ITEM_TYPES = (
        ('Акустическая гитара', 'acoustic guitar'),
        ('Электрогитара', 'electric guitar'),
        ('Укулеле', 'ukulele'),
        ('Микрофон', 'mics'),
        ('Синтезакоры', 'keyboards'),
        ('Барабаны', 'drums'),
        ('Аксессуары', 'accessories'),
        ('Звукоизоляция', 'sound insulation'),
    )

    prod_title = models.CharField(max_length=50, verbose_name="Product name")
    prod_url = models.CharField(max_length=50, verbose_name="Product_URL", blank=True, null=True)
    prod_img = models.ImageField(blank=True, null=True, upload_to="prod_photos/", verbose_name="Product image")
    prod_type = models.CharField(max_length=20, null=True, blank=True, choices=ITEM_TYPES, verbose_name="Type")
    prod_description = models.TextField(null=True, blank=True, verbose_name="Product description")
    prod_materials = models.CharField(max_length=250, verbose_name="Made of", null=True, blank=True)
    prod_manufacturer_id = models.ForeignKey("Manufacturer", null=True, blank=True,
                                             on_delete=models.SET_NULL, verbose_name="Manufacturer")
    prod_year = models.CharField(max_length=4, null=True, blank=True)
    prod_currency_info = models.ForeignKey("Currency", blank=True, null=True,
                                           on_delete=models.SET_NULL, verbose_name=" Current currency")
    prod_origin_price = models.DecimalField(null=True, max_digits=10, decimal_places=2, verbose_name="Original price")
    prod_updated_price = models.DecimalField(null=True, max_digits=10, decimal_places=2, verbose_name="Actual price")
    prod_availability = models.BooleanField(null=True, default=True)
    prod_analog = models.ForeignKey("Analog", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Analog")
    prod_department = models.ForeignKey("Department", null=True, blank=True, on_delete=models.SET_NULL,
                                        verbose_name="Department")
    prod_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Rate")
    prod_counter = models.IntegerField(null=True, blank=True, default=0, verbose_name="Rate counter")

    def print_availability(self):
        if self.prod_availability:
            return "Есть на складе!"
        else:
            return "Нет в наличии"

    def print_materials(self):
        if self.prod_materials == "-":
            return "Нету информации"
        else:
            return self.prod_materials

    def __str__(self):
        return f"Product (name: {self.prod_title},  price: {self.prod_origin_price})"

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"
        ordering = ["pk"]


class Manufacturer(models.Model):
    objects = models.Manager()
    types = (
        ('g', 'guitars'),
        ('d', 'drums'),
        ('k', 'keyboards'),
        ('u', 'ukulele'),
        ('m', 'mics'),
        ('s', 'sound insulation'),
        ('a', 'all')
    )

    manufac_name = models.CharField(max_length=50, null=True, blank=True, db_index=True, verbose_name="Company name")
    manufac_type = models.CharField(max_length=20, null=True, blank=True, choices=types, verbose_name="Type")
    manufac_site = models.URLField(null=True, blank=True, verbose_name="Web-site")
    manufac_country = models.CharField(max_length=60, null=True, blank=True, verbose_name="Country")
    manufac_city = models.CharField(max_length=60, null=True, blank=True, verbose_name="City")
    manufac_address = models.CharField(max_length=150, null=True, blank=True, verbose_name="Address")
    manufac_email = models.EmailField(null=True, blank=True, verbose_name="Email")
    manufac_phone = models.CharField(max_length=65, null=True, blank=True, verbose_name="Contact phone")

    def __str__(self):
        return f"{self.manufac_name}, {self.manufac_country}"

    class Meta:
        verbose_name_plural = "Manufacturers"
        verbose_name = "Manufacturer"
        ordering = ["-manufac_name"]


class Currency(models.Model):
    objects = models.Manager()

    cur_USD = models.DecimalField(max_digits=10, decimal_places=8, default=0.0)
    cur_EUR = models.DecimalField(max_digits=10, decimal_places=8, default=0.0)
    cur_RUB = models.DecimalField(max_digits=10, decimal_places=8, default=0.0)
    published_date = models.DateTimeField(null=True, blank=True, auto_now_add=True,
                                          db_index=True, verbose_name="Published date")

    def __str__(self):
        # return f"(USD: {self.cur_USD},  EUR: {self.cur_EUR}, RUB: {self.cur_RUB})"
        return f"(USD: {self.cur_USD})"

    class Meta:
        verbose_name_plural = "Currency"
        verbose_name = "Currency"
        ordering = ["-published_date"]


class Analog(models.Model):
    analog_id_list = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.analog_id_list

    class Meta:
        verbose_name_plural = "Analogs"
        verbose_name = "Analog"


class Department(models.Model):
    objects = models.Manager()

    department_name = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name_plural = "Departments"
        verbose_name = "Department"
        ordering = ["-department_name"]


class Comments(models.Model):
    objects = models.Manager()

    content = models.TextField(null=True, blank=True, verbose_name="Content")
    comment_to = models.ForeignKey(Store, null=True, blank=True, on_delete=models.SET_NULL,
                                   verbose_name="Product")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Published date")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "Comments"
        verbose_name = "Comment"
        ordering = ["-published"]


class Order(models.Model):
    object = models.Manager()

    cust_first_name = models.CharField(max_length=50, verbose_name="Name")
    cust_last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Second name")
    cust_address = models.CharField(max_length=250, null=True, blank=True, verbose_name="Address")
    cust_phone = models.CharField(max_length=20, verbose_name="Phone")
    cust_email = models.EmailField(max_length=150, verbose_name="Content")
    product = models.ForeignKey(Store, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Product")

    def __str__(self):
        return f"Order #{self.pk}"

    class Meta:
        verbose_name_plural = "Orders"
        verbose_name = "Order"
        ordering = ["pk"]
