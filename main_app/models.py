from django.db import models


IMAGE_TYPE_CHOICES = (
    ('bridal', 'Bridal'),
    ('party', 'Party'),
    ('reception', 'Reception'),
)


class GalleryImages(models.Model):
    """
    # Model holds the gallery images of all types
    # fields:
        - name (char)
        - src (char)
        - alt (char)
        - image_type (selection)
        - online_link (boolean)
    """
    name = models.CharField(max_length=30)
    src = models.CharField(max_length=500)
    alt = models.CharField(max_length=15)
    image_type = models.CharField(max_length=15, choices=IMAGE_TYPE_CHOICES, default='bridal')
    online_link = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Gallery Images"


class BrandsWeUse(models.Model):
    """
    # Model holds the items involved in a particular makeup type
    # Fields:
        - name (char)
        - src (char)
        - alt (char)
        - online_link (boolean)
    """
    name = models.CharField(max_length=30)
    src = models.CharField(max_length=500)
    alt = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Brands Used"


class ContactUs(models.Model):
    """
    # Model holds the items involved in a particular makeup type
    # Fields:
        form:
            - name (char)
            - email (emailField)
            - subject (char)
            - message (textArea)
    """
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Us"


class MakeupOffers(models.Model):
    """
    # Model holds offers
    # fields:
        - start_date (datetime)
        - end_date (datetime)
        - message (char)
    """
    name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    message = models.CharField(max_length=255)
    direction = models.CharField(max_length=10, default="left")
    speed = models.IntegerField(default=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Makeup Offers"


class MakeupServiceType(models.Model):
    """
    # Model holds the items involved in a particular makeup type
    # fields:
        - name (char)
        - available (boolean)
    """
    name = models.CharField(max_length=30)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Makeup Service Types"


class MakeupService(models.Model):
    """
    # Model holds the items involved in a particular makeup type
    # fields:
        - name (char)
        - price (Integer)
        - makeupServiceType (ManyToManyField MakeupServiceType)
    """
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    makeup_service = models.ManyToManyField(MakeupServiceType, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Makeup Services"
