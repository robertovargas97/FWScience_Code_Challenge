from planets_api import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"planets", views.PlanetViewSet, basename="planets-url")

urlpatterns = router.urls
