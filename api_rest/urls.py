from rest_framework import routers
from . api import UserViewSet,MembershipViewSet,TribeViewSet,RedViewSet,MinistryViewSet

router = routers.DefaultRouter()

router.register('api/users',UserViewSet,'users')
router.register('api/membership',MembershipViewSet,'memberships')
router.register('api/tribes',TribeViewSet,'tribes')
router.register('api/reds',RedViewSet,'reds')
router.register('api/ministries',MinistryViewSet,'ministries')

urlpatterns = router.urls