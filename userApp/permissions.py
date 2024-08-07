from rest_framework.permissions import BasePermission

from userApp.models import Role


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.role is None:
            return False
        if (request.user.role.name == 'Admin' or request.user.is_superuser) and request.user.is_authenticated:
            return True
        return False
