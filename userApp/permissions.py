from rest_framework.permissions import BasePermission


class IsAgent(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'Agent' and request.user.is_authenticated:
            return True
        return False


class IsAshir(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'Ashir' and request.user.is_authenticated:
            return True
        return False


class IsKurator(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'Kurator' and request.user.is_authenticated:
            return True
        return False
