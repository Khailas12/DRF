from rest_framework import permissions


# permissions for users rights to CRUD their belongings
class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method is permissions.SAFE_METHODS:
            if not hasattr(obj, 'owner'):
                return True

            return obj.owner == request.user
        return True