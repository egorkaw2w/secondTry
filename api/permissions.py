from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)

class CustomDjangoModelPermissions(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        model_cls = getattr(view, 'queryset', None).model
        if not model_cls:
            logger.error("No model found in view queryset")
            return False
        app_label = model_cls._meta.app_label
        model_name = model_cls._meta.model_name
        logger.debug(f"User: {request.user}, Is authenticated: {request.user.is_authenticated}, Method: {request.method}, Model: {app_label}.{model_name}")
        if not request.user.is_authenticated:
            logger.debug("User is not authenticated")
            return False
        perms = self.get_required_permissions(request.method, model_cls)
        if not perms:
            logger.debug(f"No permissions required for method {request.method}")
            return request.method in ('OPTIONS', 'HEAD')
        has_perm = request.user.has_perms(perms)
        logger.debug(f"Required permissions: {perms}, User has permissions: {has_perm}")
        return has_perm

class CustomCategoryPermissions(CustomDjangoModelPermissions):
    pass

class CustomMaterialPermissions(CustomDjangoModelPermissions):
    pass

class CustomProductPermissions(CustomDjangoModelPermissions):
    pass

class CustomOrderPermissions(CustomDjangoModelPermissions):
    pass

class CustomOrderItemPermissions(CustomDjangoModelPermissions):
    pass

class CustomRolePermissions(CustomDjangoModelPermissions):
    pass

class CustomUserRolePermissions(CustomDjangoModelPermissions):
    pass

class CustomReviewPermissions(CustomDjangoModelPermissions):
    pass

class CustomPaymentPermissions(CustomDjangoModelPermissions):
    pass