from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone


class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_account')
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.user.email})"


class Category(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    category_image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    status = models.CharField(max_length=255,default="Disabled")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title[:50])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    title = models.TextField()
    description = models.TextField(blank=True)
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    status = models.CharField(max_length=255,default="Disabled")

    class Meta:
        unique_together = ('category', 'slug')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title[:50])
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.title} > {self.title}"



class ProductAttribute(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class ProductAttributeValue(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='attributes')
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.product.name} - {self.attribute.name}: {self.value}"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='product_sub_category', null=True, blank=True)
    name = models.TextField()
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='product_thumbnails/', null=True, blank=True)
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    meta_image = models.ImageField(upload_to='product_meta_images/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True,default="Disabled")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name[:50])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product_images/')
    IMAGE_TYPES = [
        ('Primary', 'Primary'),
        ('Gallery', 'Gallery'),
        ('Lifestyle', 'Lifestyle'),
        ('Shade Swatch', 'Shade Swatch'),
        ('Ingredients', 'Ingredients'),
        ('How To Use', 'How To Use'),
        ('Texture', 'Texture'),
        ('Packaging', 'Packaging')
    ]
    image_type = models.CharField(max_length=50, choices=IMAGE_TYPES, default='Gallery')
    display_order = models.PositiveIntegerField(default=0)

    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"


class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_variant')
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='variant_images/', null=True, blank=True)
    # Cosmetics Variant enhancements
    shade_name = models.CharField(max_length=255, blank=True, null=True)
    shade_code = models.CharField(max_length=50, blank=True, null=True)
    shade_family = models.CharField(max_length=100, blank=True, null=True)
    shade_hex = models.CharField(max_length=7, blank=True, null=True)
    volume = models.CharField(max_length=50, blank=True, null=True)
    pack_size = models.CharField(max_length=50, blank=True, null=True)

    status = models.CharField(max_length=255,default="Disabled")

    # ── Shipping Dimensions (required for Shiprocket) ──
    weight   = models.DecimalField(max_digits=5, decimal_places=2, default=0.5, help_text='Weight in kg')
    length   = models.DecimalField(max_digits=6, decimal_places=2, default=1.0, help_text='Length in cm')
    breadth  = models.DecimalField(max_digits=6, decimal_places=2, default=1.0, help_text='Breadth in cm')
    height   = models.DecimalField(max_digits=6, decimal_places=2, default=1.0, help_text='Height in cm')

    @property
    def volumetric_weight(self):
        return (self.length * self.breadth * self.height) / 5000

    def __str__(self):
        return self.name


class Highlight(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_highlight')
    icon = models.ImageField(upload_to='highlight_icons/', null=True, blank=True)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class APlusContent(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_content')
    image = models.ImageField(upload_to='aplus_images/', null=True, blank=True)
    image_alt = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.product.name
    
class Offer(models.Model):

    # ── Trigger Type ──
    TRIGGER_CHOICES = [
        ('coupon',    'Coupon Code'),
        ('automatic', 'Automatic'),
    ]

    # ── Condition Type ──
    CONDITION_TYPE_CHOICES = [
        ('none',          'No Condition'),
        ('min_order',     'Minimum Order Amount'),
        ('min_quantity',  'Minimum Quantity'),
        ('product',       'Specific Product in Cart'),
        ('category',      'Specific Category in Cart'),
        ('sub_category',  'Specific Sub Category in Cart'),
        ('first_order',   'First Order Only'),
    ]

    # ── Action Type ──
    ACTION_TYPE_CHOICES = [
        ('percentage_off',  'Percentage Off'),
        ('flat_off',        'Flat Amount Off'),
        ('free_shipping',   'Free Shipping'),
        ('free_product',    'Free Product Added to Cart'),
        ('bundle_price',    'Fixed Bundle Price'),
        ('bogo',            'Buy X Get Y Free'),
    ]

    # ── Status ──
    STATUS_CHOICES = [
        ('Active',   'Active'),
        ('Inactive', 'Inactive'),
        ('Expired',  'Expired'),
        ('Scheduled','Scheduled'),
    ]

    # ── Core ──
    title       = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    trigger     = models.CharField(max_length=20, choices=TRIGGER_CHOICES)
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    # ── Coupon Specific ──
    coupon_code      = models.CharField(max_length=50, unique=True, null=True, blank=True)
    usage_limit      = models.PositiveIntegerField(null=True, blank=True, help_text='Leave blank for unlimited')
    used_count       = models.PositiveIntegerField(default=0)
    one_per_customer = models.BooleanField(default=False)

    # ── Condition ──
    condition_type     = models.CharField(max_length=30, choices=CONDITION_TYPE_CHOICES, default='none')
    min_order_amount   = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text='Used when condition is min_order')
    min_quantity       = models.PositiveIntegerField(null=True, blank=True, help_text='Used when condition is min_quantity')
    condition_product  = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True, related_name='condition_offers')
    condition_category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='condition_offers')
    condition_sub_category = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True, blank=True, related_name='condition_offers')

    # ── Action ──
    action_type      = models.CharField(max_length=30, choices=ACTION_TYPE_CHOICES)
    discount_value   = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text='Percentage or flat amount')
    max_discount_cap = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text='Max discount allowed (for percentage off)')

    # ── Free Product / BOGO ──
    free_product     = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True, related_name='free_in_offers')
    free_variant     = models.ForeignKey('Variant', on_delete=models.SET_NULL, null=True, blank=True, related_name='free_in_offers')
    buy_quantity     = models.PositiveIntegerField(null=True, blank=True, help_text='Buy X — for BOGO')
    get_quantity     = models.PositiveIntegerField(null=True, blank=True, help_text='Get Y free — for BOGO')

    # ── Bundle ──
    bundle_products  = models.ManyToManyField('Product', blank=True, related_name='bundle_offers')
    bundle_price     = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # ── Stacking ──
    stackable        = models.BooleanField(default=False, help_text='Can this stack with other discounts?')
    priority         = models.PositiveIntegerField(default=0, help_text='Higher number = applied first')

    # ── Validity ──
    valid_from       = models.DateTimeField()
    valid_to         = models.DateTimeField()

    # ── Auto ──
    created_at       = models.DateTimeField(default=timezone.now)
    updated_at       = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-priority', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.get_trigger_display()} — {self.get_action_type_display()})"

    def is_valid(self):
        now = timezone.now()
        return self.status == 'Active' and self.valid_from <= now <= self.valid_to

    def is_usage_limit_reached(self):
        if self.usage_limit is None:
            return False
        return self.used_count >= self.usage_limit
    
class Support(models.Model):
    name       = models.CharField(max_length=255)
    email      = models.EmailField()
    phone      = models.CharField(max_length=15, blank=True)
    subject    = models.CharField(max_length=255)
    message    = models.TextField()
    status     = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} — {self.subject}"
    
class Cart(models.Model):
    customer         = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True, blank=True, related_name='carts')
    session_key      = models.CharField(max_length=255, null=True, blank=True)
    is_abandoned     = models.BooleanField(default=False)
    recovery_email_1 = models.BooleanField(default=False)
    recovery_email_2 = models.BooleanField(default=False)
    recovery_email_3 = models.BooleanField(default=False)
    created_at       = models.DateTimeField(default=timezone.now)
    updated_at       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart — {self.customer or self.session_key}"


class CartItem(models.Model):
    cart     = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant  = models.ForeignKey(Variant, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

# Order Managment

class Order(models.Model):

    STATUS_CHOICES = [
        ('pending',          'Pending'),
        ('payment_failed',   'Payment Failed'),
        ('paid',             'Paid'),
        ('processing',       'Processing'),
        ('shipped',          'Shipped'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered',        'Delivered'),
        ('cancelled',        'Cancelled'),
        ('return_requested', 'Return Requested'),
        ('returned',         'Returned'),
        ('refunded',         'Refunded'),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('razorpay', 'Razorpay'),
        ('cod',      'Cash on Delivery'),
    ]

    # ── Display ID ──
    display_order_id = models.CharField(max_length=50, unique=True, null=True, blank=True, db_index=True)

    # ── Customer ──
    customer       = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    email          = models.EmailField()
    phone          = models.CharField(max_length=15)

    # ── Shipping Address ──
    full_name      = models.CharField(max_length=255)
    address_line_1 = models.TextField()
    address_line_2 = models.TextField(blank=True)
    city           = models.CharField(max_length=100)
    state          = models.CharField(max_length=100)
    pincode        = models.CharField(max_length=10)
    country        = models.CharField(max_length=100, default='India')

    # ── Pricing ──
    subtotal       = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount       = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    gst_total      = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total          = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # ── Offer / Coupon ──
    offer          = models.ForeignKey(Offer, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    coupon_code    = models.CharField(max_length=50, blank=True)

    # ── Razorpay ──
    payment_method      = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='razorpay')
    razorpay_order_id   = models.CharField(max_length=255, blank=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True)
    razorpay_signature  = models.CharField(max_length=500, blank=True)
    payment_status      = models.CharField(max_length=50, default='pending')

    # ── Shiprocket ──
    shiprocket_order_id    = models.CharField(max_length=255, blank=True)
    shiprocket_shipment_id = models.CharField(max_length=255, blank=True)
    awb_code               = models.CharField(max_length=255, blank=True)
    courier_name           = models.CharField(max_length=255, blank=True)
    shipping_status        = models.CharField(max_length=255, blank=True)
    estimated_delivery     = models.DateField(null=True, blank=True)

    # ── Shipping Dimensions Snapshot ──
    # Stored at time of order so Shiprocket payload is always accurate
    # even if variant dimensions are later edited
    total_weight   = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text='Total order weight in kg')
    total_length   = models.DecimalField(max_digits=8, decimal_places=2, default=1, help_text='Longest item length in cm')
    total_breadth  = models.DecimalField(max_digits=8, decimal_places=2, default=1, help_text='Widest item breadth in cm')
    total_height   = models.DecimalField(max_digits=8, decimal_places=2, default=1, help_text='Combined height of all items in cm')

    # ── Order ──
    status         = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    notes          = models.TextField(blank=True)
    created_at     = models.DateTimeField(default=timezone.now)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.id} — {self.full_name} — {self.status}"


class OrderItem(models.Model):
    order   = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    variant = models.ForeignKey(Variant, on_delete=models.SET_NULL, null=True, blank=True)

    # ── Snapshot at time of order ──
    # Never changes even if product/variant is edited or deleted later
    product_name  = models.CharField(max_length=255)
    variant_name  = models.CharField(max_length=255, blank=True)
    price         = models.DecimalField(max_digits=10, decimal_places=2)
    gst           = models.DecimalField(max_digits=5, decimal_places=2)
    quantity      = models.PositiveIntegerField(default=1)
    total         = models.DecimalField(max_digits=10, decimal_places=2)

    # ── Dimension Snapshot per item ──
    weight  = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    length  = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    breadth = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    height  = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product_name} x {self.quantity}"


# ============================================================
# CONTENT MANAGEMENT SYSTEM
# Reference: Corporate Impact — github.com/mediabigscoopstudio/Corporate-Impact
#
# NOTE: Raw Wish already contains a 'Category' model used for
# e-commerce products.  The content-management category is named
# 'ArticleCategory' here to avoid any collision with that model.
# Field names and behaviour are otherwise a faithful port of the
# Corporate Impact Category model.
# ============================================================


# ── ArticleCategory ─────────────────────────────────────────────────────────

class ArticleCategory(models.Model):
    """Content-management category (articles/blog), distinct from the
    e-commerce Category model that already exists in this app."""

    title           = models.CharField(max_length=255)
    description     = models.TextField()
    meta_title      = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords   = models.CharField(max_length=255)
    slug            = models.SlugField(unique=True, blank=True)
    created_at      = models.DateTimeField(default=timezone.now)

    status = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default='Enabled',
    )

    display_order = models.PositiveIntegerField(
        default=0,
        blank=True,
        null=True,
    )

    show_in_nav = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order', 'title']
        verbose_name        = 'Article Category'
        verbose_name_plural = 'Article Categories'

    def save(self, *args, **kwargs):
        # Auto-generate slug from title on first save
        if not self.slug:
            self.slug = slugify(self.title)

        # Auto-place new categories at the end of the display order
        if not self.pk:
            last_order = ArticleCategory.objects.order_by('-display_order').first()
            self.display_order = (
                last_order.display_order + 1
                if last_order else 1
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ── Author ───────────────────────────────────────────────────────────────────

class Author(models.Model):
    """Article author profile.  Optionally linked to a Django User account."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='author_profile',
        null=True,
        blank=True,
    )
    name        = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    email       = models.EmailField(unique=True, blank=True, null=True)
    DOB         = models.DateField(blank=True, null=True)
    location    = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to='authors/')

    # Social links
    facebook_url  = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url  = models.URLField(blank=True, null=True)
    twitter_url   = models.URLField(blank=True, null=True)

    slug       = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    status     = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        # Generate a unique slug from the author name
        if not self.slug:
            base_slug = slugify(self.name)
            slug  = base_slug
            count = 1
            while Author.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base_slug}-{count}'
                count += 1
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# ── Article ──────────────────────────────────────────────────────────────────

class Article(models.Model):
    """Core article / blog-post content model."""

    title    = models.CharField(max_length=1500)
    author   = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='articles',
    )
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.CASCADE,
        related_name='articles',
    )

    description = models.TextField(blank=True, null=True)

    # TL;DR section
    tldr_title = models.CharField(max_length=1500, blank=True, null=True)
    tldr       = models.TextField(blank=True, null=True)

    # SEO metadata
    meta_title       = models.CharField(max_length=1500)
    meta_description = models.TextField()
    meta_keywords    = models.CharField(max_length=1500)

    # Body
    content = models.TextField(blank=True, null=True)

    # Engagement counters
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    # URL
    slug = models.SlugField(unique=True, blank=True, max_length=1500)

    # Timestamps
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # Status
    status = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default='Enabled',
    )

    # Visual customisation (banner colour overrides)
    title_colour             = models.CharField(max_length=100, blank=True)
    banner_background_colour = models.CharField(max_length=100, blank=True)
    remaining_text_colour    = models.CharField(max_length=100, blank=True)

    # Images
    banner_image    = models.ImageField(upload_to='articles/banners/',    blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to='articles/thumbnails/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Generate a collision-free slug from the article title
        if not self.slug:
            base_slug = slugify(self.title)
            slug  = base_slug
            count = 1
            while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base_slug}-{count}'
                count += 1
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ── ArticleFAQ ───────────────────────────────────────────────────────────────

class ArticleFAQ(models.Model):
    """Frequently-asked questions attached to an Article.
    Supports multiple FAQ entries per article (one-to-many)."""

    article  = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='faqs',
    )
    question = models.CharField(max_length=500)
    answer   = models.TextField()

    class Meta:
        verbose_name        = 'Article FAQ'
        verbose_name_plural = 'Article FAQs'

    def __str__(self):
        return self.question


# ── ArticleHowTo ─────────────────────────────────────────────────────────────

class ArticleHowTo(models.Model):
    """Step-by-step how-to instructions attached to an Article.
    Supports multiple ordered steps per article (one-to-many)."""

    article   = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='howto_steps',
    )
    step_name = models.CharField(max_length=300)
    step_text = models.TextField()

    class Meta:
        verbose_name        = 'Article How-To Step'
        verbose_name_plural = 'Article How-To Steps'

    def __str__(self):
        return self.step_name
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.email


# ============================================================
# SUPPORT & ORDER MANAGEMENT EXTENSIONS
# ============================================================

class SequenceCounter(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.PositiveIntegerField(default=1)

    @classmethod
    def get_next_value(cls, name):
        from django.db import transaction
        with transaction.atomic():
            counter, created = cls.objects.select_for_update().get_or_create(name=name)
            val = counter.value
            counter.value += 1
            counter.save()
            return val


class SupportQuery(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('BOT_HANDLING', 'Bot Handling'),
        ('ESCALATED', 'Escalated'),
        ('HUMAN_REVIEW', 'Human Review'),
        ('ACTION_REQUIRED', 'Action Required'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('NORMAL', 'Normal'),
        ('HIGH', 'High'),
        ('URGENT', 'Urgent'),
    ]

    support_id    = models.CharField(max_length=50, unique=True, db_index=True)
    customer      = models.ForeignKey(Customers, on_delete=models.CASCADE, related_name='support_queries')
    order         = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='support_queries')
    order_item    = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, null=True, blank=True)
    product       = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    
    category      = models.CharField(max_length=100)
    priority      = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='NORMAL')
    status        = models.CharField(max_length=50, choices=STATUS_CHOICES, default='OPEN')
    assigned_to   = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_support_queries')
    
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    last_customer_message_at = models.DateTimeField(null=True, blank=True)
    last_agent_message_at    = models.DateTimeField(null=True, blank=True)
    resolved_at   = models.DateTimeField(null=True, blank=True)
    closed_at     = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.support_id} - {self.customer}"

    def save(self, *args, **kwargs):
        if not self.support_id:
            seq = SequenceCounter.get_next_value('support_queries')
            self.support_id = f"#{seq:04d}RWCS"
        super().save(*args, **kwargs)


class SupportMessage(models.Model):
    SENDER_TYPES = [
        ('CUSTOMER', 'Customer'),
        ('BOT', 'Bot'),
        ('AGENT', 'Agent'),
        ('SYSTEM', 'System'),
    ]
    
    support_query = models.ForeignKey(SupportQuery, on_delete=models.CASCADE, related_name='messages')
    sender_type   = models.CharField(max_length=20, choices=SENDER_TYPES)
    sender_user   = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    message       = models.TextField()
    is_internal   = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message on {self.support_query.support_id} by {self.sender_type}"

class Wishlist(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True, blank=True, related_name='wishlists')
    session_key = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Wishlist for {self.customer if self.customer else self.session_key}"

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='wishlist_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.SET_NULL, null=True, blank=True)
    added_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('wishlist', 'product', 'variant')

    def __str__(self):
        return f"{self.product.name} in Wishlist"
