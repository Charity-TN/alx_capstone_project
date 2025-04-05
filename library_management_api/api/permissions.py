from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    - Allows anyone to read(GET, HEAD, OPTIONS).
    - Only admins can create, update, delete.
    """

    def has_permission(self, request, view):
        if request.mwthod in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
    
class IsOwnerOrReadOnly(BasePermission):
    """
    - Allows owners to modify their own data.
    - Only can only view.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user