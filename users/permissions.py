from rest_framework import permissions


class IsOwnerOrAdminOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners or admins of an object.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS or request.user.is_staff:
            return True

        return obj.pk == request.user.pk
