from rest_framework import serializers
from .models import Customer, Order, Return, Dispute

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'name', 'address']

class OrderSerializer(serializers.ModelSerializer):
    customer_details = serializers.PrimaryKeyRelatedField(
        queryset=Customer.objects.all())  # Nested serializer for customer_details

    class Meta:
        model = Order
        fields = ['order_id', 'item', 'customer_details']

class ReturnSerializer(serializers.ModelSerializer):
    original_order = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all())  # Nested serializer for original_order

    class Meta:
        model = Return
        fields = ['return_id', 'return_reason', 'return_tracking', 'original_order']

class DisputeSerializer(serializers.ModelSerializer):
    original_order = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all())  # Nested serializer for original_order

    class Meta:
        model = Dispute
        fields = ['dispute_id', 'original_order', 'dispute_reason',
                  'status_tracking', 'created_at', 'updated_at']
