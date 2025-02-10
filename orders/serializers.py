from rest_framework import serializers
from orders.models import Order, OrderItem
from menu.models import Menu


class OrderItemSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity', 'price']



class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField(read_only=True)
    menu_items = serializers.ListField(
        child=serializers.DictField(),
        write_only=True
    )

    class Meta:
        model = Order
        fields = '__all__'

    def get_items(self, obj):
        items = OrderItem.objects.filter(order=obj)
        return OrderItemSerializer(items, many=True).data

    def create(self, validated_data):
       menu_items = validated_data.pop('menu_items')
       order = Order.objects.create(**validated_data)
        
       total = 0
       for item in menu_items:
           menu_item = Menu.objects.get(id=item['id'])
           quantity = item['quantity']
           price = menu_item.price * quantity
           total += price
           
           OrderItem.objects.create(
               order=order,
               menu_item=menu_item,
               quantity=quantity,
               price=price
           )
       
       order.total_price = total
       order.save()
       return order