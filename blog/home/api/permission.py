from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only access for anyone
        if request.method in SAFE_METHODS:
            return True
        # Write access only for the post's owner
        return obj.author == request.user
