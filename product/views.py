from rest_framework import generics
from .models import *
from .serializers import *
from warehouse.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# List and Create view
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
# Retrieve view


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]





class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        previous_amount = product.amount
        new_amount = int(request.data.get('amount', previous_amount))
        new_status = request.data.get('status', product.status)

        # Check if status is being changed to 'sotildi'
        if new_status == 'sotildi':
            if new_amount < previous_amount:
                # Subtract the amount and keep the product in Product table
                product.amount -= new_amount
                product.save()

                # Create a SoldProduct entry with the specified new amount
                SoldProduct.objects.create(
                    name=product.name,
                    cost=product.cost,
                    amount=new_amount,
                    note=product.note,
                    add_time=timezone.now(),
                    status='sotildi',
                    category=product.category,
                )
                log_message = (
                    f"Partial sale: {new_amount} of {product.name} moved to SoldProduct. "
                    f"Remaining amount in Product: {product.amount}."
                )

            else:
                # Move the entire product to SoldProduct and delete from Product table
                SoldProduct.objects.create(
                    name=product.name,
                    cost=product.cost,
                    amount=new_amount,
                    note=product.note,
                    add_time=timezone.now(),
                    status='sotildi',
                    category=product.category,
                )
                product.delete()
                log_message = f"Full sale: {product.name} moved to SoldProduct with amount {new_amount}."

            return Response({'status': 'Product updated successfully', 'log': log_message})

        # If status is not 'sotildi', update other fields without creating SoldProduct
        response = super().update(request, *args, **kwargs)
        return response



# Delete view
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
