from django.contrib.auth.models import Permission # type: ignore
from django.contrib.contenttypes.models import ContentType# type: ignore
from authenticate_system import permission_config


def add_permission(role,user):
    role_permission = permission_config.PERMISSION_CONFIG.get(role,{})
    for model,permissions  in role_permission.items():
        content_type=ContentType.objects.get_for_model(model)
        for perm_codename in permissions:
            permission=Permission.objects.get(content_type=content_type,codename=f"{perm_codename}_{model._meta.model_name}")
            user.user_permissions.add(permission)