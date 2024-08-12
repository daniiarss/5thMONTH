from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from rest_framework import status
from .serializers import ProductSerializer

@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'message': 'Product not found'})
    product = Product.objects.get(id=id)
    data = ProductSerializer(product).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def product_list_api_view(request):
    # step1: Collect all products
    products = Product.objects.all()

    # step2: Reformat products to list of Dictionaries
    list_ = ProductSerializer(instance=products, many=True).data
    # step3: Return Response
    return Response(data=list_, status=status.HTTP_200_OK)

