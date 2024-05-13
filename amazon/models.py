from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
import datetime
# choice values for return tracking status
RETURN_TRACKING_CHOICES = ((1, "INITIATED"), (2, "IN PROGRESS"), (3, "RETURNED"))

# choice values for dispute tracking status
DISPUTE_TRACKING_CHOICES = (
    (1, "RAISED"),
    (2, "ACTIVE"),
    (3, "INACTIVE"),
    (4, "CLOSED"),
    (5, "DUPLICATE"),
)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Customer(BaseModel):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    address = models.TextField(max_length=255)

    def __str__(self):
        return self.name

class Order(BaseModel):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.CharField(max_length=50)
    customer_details = models.ForeignKey("Customer", on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.order_id} for {self.customer_details.name}"

class Return(BaseModel):
    return_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    return_reason = models.TextField(max_length=255)
    return_tracking = models.IntegerField(choices=RETURN_TRACKING_CHOICES, default=1)
    original_order = models.ForeignKey("Order", on_delete=models.CASCADE)

    def __str__(self):
        return f"Return for Order {self.original_order.order_id}"

class Dispute(BaseModel):
    dispute_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    original_order = models.ForeignKey("Order", on_delete=models.CASCADE)
    dispute_reason = models.TextField(max_length=255)
    status_tracking = models.IntegerField(choices=DISPUTE_TRACKING_CHOICES, default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    resolution = models.TextField(max_length=100)

    def __str__(self):
        return f"Dispute for Order {self.original_order.order_id}"
