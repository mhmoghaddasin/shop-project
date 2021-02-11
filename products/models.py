from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse
# from django.db.models import Q

# from djangoratings.fields import RatingField
# Create your models here.

User = get_user_model()


class Brand(models.Model):
    name = models.CharField(_('name'), max_length=50)
    slug = models.SlugField(_('slug'), )
    image = models.ImageField(verbose_name=_('image'), upload_to='brand/image/')
    details = models.CharField(_('details'), max_length=250)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_('name'), max_length=150)
    slug = models.SlugField(_('slug'), db_index=True)
    details = models.TextField(_('details'), max_length=250)
    image = models.ImageField(verbose_name=_('image'), upload_to='category/image/')
    parent = models.ForeignKey('self', verbose_name=_("Parent"), on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='children', related_query_name='children')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.slug

    @property
    def get_subcategory(self):
        return Category.objects.filter(parent=self)

    @property
    def sum_product_category(self):
        return Product.objects.filter(
            models.Q(category=self) | models.Q(category__parent=self) | models.Q(category__parent__parent=self)).count()

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"category_slug": self.slug})


class Product(models.Model):
    name = models.CharField(_('name'), max_length=50)
    slug = models.SlugField(_('slug'), )
    category = models.ForeignKey("products.Category", related_name='product', related_query_name='product',
                                 verbose_name=_("category"), on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey("products.Brand", related_name='product', verbose_name=_("brand"),
                              on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(verbose_name=_('image'), upload_to='product/image/')
    details = models.TextField(_('details'), max_length=250)
    rating = models.IntegerField(verbose_name=_("rating"), blank=True, null=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"product_slug": self.slug})


class ProductMeta(models.Model):
    product = models.ForeignKey("products.Product", related_name='productmeta', related_query_name='productmeta',
                                verbose_name=_("product"), on_delete=models.CASCADE, null=True, blank=True)
    label = models.CharField(_('label'), max_length=250)
    value = models.DecimalField(_('value'), max_digits=100, decimal_places=10)

    class Meta:
        verbose_name = _('ProductMeta')
        verbose_name_plural = _('ProductMetas')

    def __str__(self):
        return self.product.name


class Image(models.Model):
    product = models.ForeignKey("products.Product", related_name='images', related_query_name='images',
                                verbose_name=_("product"), on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(verbose_name=_('image'), upload_to='extraproductimage/image/')

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __str__(self):
        return self.product, 'image'


class ShopProduct(models.Model):
    shop = models.ForeignKey("accounts.Shop", related_name='ShopProduct', verbose_name=_("shop"),
                             on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey("products.Product", related_name='off', verbose_name=_("product"),
                                on_delete=models.CASCADE,
                                null=True, blank=True)
    price = models.IntegerField(_('price'), )
    quantity = models.IntegerField(_('quantity'), )
    copoun = models.FloatField(verbose_name=_('copoun'), null=True, blank=True)

    class Meta:
        verbose_name = _('ShopProduct')
        verbose_name_plural = _('ShopProducts')

    def __str__(self):
        return self.product.name


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name=_('user'), on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey("products.Product", related_name='comment', verbose_name=_("product"),
                                on_delete=models.CASCADE)
    content = models.TextField(_('content'), )

    # rating = RatingField(range=5)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return self.user, self.product, 'comment'


class Like(models.Model):
    user = models.ForeignKey(User, related_name='like', related_query_name='like', verbose_name=_('user'),
                             on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey("products.Product", related_name='like', related_query_name='like',
                                verbose_name=_("product"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')

    def __str__(self):
        return self.user, self.product, 'like'
