from django.db import models


class Manufacturer(models.Model):
    mfg = models.CharField(max_length=20)

    def __str__(self):
        return self.mfg


class Category(models.Model):
    cat = models.CharField(max_length=20)

    def __str__(self):
        return self.cat


class Image(models.Model):
    bike = models.ForeignKey("Bike", related_name="images", on_delete=models.CASCADE)
    image = models.URLField(max_length=400)


class Bike(models.Model):
    year = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=400)
    price = models.IntegerField(blank=True, null=True)
    first_post = models.TextField()
    cat = models.ForeignKey("Category", on_delete=models.CASCADE)
    mfg = models.ForeignKey(
        "Manufacturer", on_delete=models.CASCADE, blank=True, null=True
    )
    post_date = models.DateField()

    @property
    def to_dict(self):
        data = {"first_post": json.loads(self.first_post)}
        return data

    def __str__(self):
        return self.title[0:20]
