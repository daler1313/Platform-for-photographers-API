from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import OrderDetail
from ..serializers import OrderDetailSerializer,OrderDetailEditSerializer,OrderDetailCreateSerializer



class OrderDetailViewSet(viewsets.ModelViewSet):
  queryset = OrderDetail.objects.all()
  serializer_class = OrderDetailSerializer
  permission_classes = [IsAuthenticated]

  
  def get_serializer_class(self):
    if self.action == "list":
      return OrderDetailSerializer
    if self.action == 'create':
        return OrderDetailCreateSerializer
    elif self.action == 'update' or self.action == 'partial_update':
        return OrderDetailEditSerializer
    return OrderDetailSerializer  

  def update(self, request, *args, **kwargs):
      instance = self.get_object()
      if instance.order.user == self.request.user:
          serializer = OrderDetailEditSerializer(
          instance, data=request.data, partial=True)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data)
      return Response("Вы не имеете доступа к обновлению", status=status.HTTP_403_FORBIDDEN)

  def destroy(self, request, *args, **kwargs):
      instance = self.get_object()
      if instance.order.user == self.request.user:
          instance.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
      return Response("Вы не имеете доступа к удалению", status=status.HTTP_403_FORBIDDEN)


  def list(self, request, *args, **kwargs):
    self.queryset = OrderDetail.objects.filter(order__user=request.user)
    return super().list(request, *args, **kwargs)
