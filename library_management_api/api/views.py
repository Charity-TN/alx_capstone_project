from rest_framework.decorators import action
from .models import Book, User, Transaction
from rest_framework import viewsets, status, 
from .serializers import BookSerializer, UserSerializer, TransactionSerializer, TrackingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import logging
from django.utils import timezone

# Create your views here.

#Setup logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#Book Viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.get()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'code'

    @action(detail=True, methods=['post'])
    def checkout(self, request, code=None):
        book = self.get_object()
        if book.copies_available > 0:
            Transaction.objects.create(user=request.user, book=book)
            book.copies_available -= 1
            book.save()
            logger.info(f"{request.user.username}checked out book '{book.title}'")
            return Response({'message': 'Book checked out successfully'}, status=status.HTTP_201_CREATED)
        else:
            logger.warning(f"Checkout failed for '{book.title}' - No copies available")
            return Response({'error': 'No copies available'}, status=status.HTTP_400_BAD_REQUEST)








