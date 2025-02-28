from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from user.models import Item
from .serializers import ItemSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getData(request):
    permission_classes = (IsAuthenticated,)

    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
