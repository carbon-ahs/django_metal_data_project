from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CoreModelTest(models.Model):
    """Model definition for CoreModelTest."""

    # TODO: Define fields here
    title = models.CharField(_("Titel"), max_length=50)

    class Meta:
        """Meta definition for CoreModelTest."""

        verbose_name = "CoreModelTest"
        verbose_name_plural = "CoreModelTests"

    def __str__(self):
        """Unicode representation of CoreModelTest."""
        pass

    def get_title_by_id(pk):
        coreModelObject = CoreModelTest.objects.get(pk=pk)
        return coreModelObject


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MetalBidPrice(TimeStampMixin):
    """Model definition for MetalBidPrice."""

    # TODO: Define fields here
    material = models.CharField(_("Material"), max_length=50)
    bid_price = models.FloatField(_("Bid Price"))

    class Meta:
        """Meta definition for MetalBidPrice."""

        verbose_name = "MetalBidPrice"
        verbose_name_plural = "MetalBidPrices"

    def __str__(self):
        """Unicode representation of MetalBidPrice."""
        return f"{self.material} - {self.bid_price}"


class LmePriceTrend(models.Model):
    """Model definition for LmePriceTrend."""

    # TODO: Define fields here
    entry_date = models.DateField(_("Entry Date"))
    data_source = models.CharField(_("Data Source"), max_length=50)
    material = models.CharField(_("Material"), max_length=50)
    bid_price = models.FloatField(_("Bid Price"))
    ask_price = models.FloatField(_("Ask Price"))
    currency = models.CharField(_("Currency"), max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for LmePriceTrend."""

        verbose_name = "LmePriceTrend"
        verbose_name_plural = "LmePriceTrends"

    def __str__(self):
        """Unicode representation of LmePriceTrend."""
        return f"{self.material} - {self.bid_price}"
