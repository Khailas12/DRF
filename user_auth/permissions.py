from rest_framework import permissions


# permissions for users rights to CRUD their belongings
class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def had_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.owner == request.user