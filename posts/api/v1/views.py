from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ...models import Post, Category
from .paginations import Pagination



from .serializers import PostSerializer , CategorySerializer
from .permissions import IsOwnerOrReadOnly


class PostView(ModelViewSet):
    serializer_class = PostSerializer
    pagination_class = Pagination
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = {'category':["exact","in"], 'author':["exact"],'status':["exact"]}

    search_fields = ['title', 'content']
    ordering_fields = ['published_date']
    

class CatetegoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()

    
    