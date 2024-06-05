from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import token_refresh
# from core.views import token_obtain_pair

from rest_framework.routers import DefaultRouter

from .apis import ForgotPasswordViewSet, AuditorViewSet
# from audit_task.api import AuditTaskViewSet,AssetDataViewSet,AssetStatusViewSet

router = DefaultRouter()

router.register('forgot_password', ForgotPasswordViewSet, basename='forgot_password')
# router.register('auditor',AuditorViewSet,basename='auditor')
# router.register('audit_task',AuditTaskViewSet,basename='audit_task')
# router.register('asset_data',AssetDataViewSet,basename='asset_data')
# router.register('asset_statuses',AssetStatusViewSet,basename='asset_statuses')