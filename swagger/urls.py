from django.views.generic import TemplateView
from django.urls import path
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path(
        "openapi",
        get_schema_view(
            title="ToDo API", description="グリーンランドの #やること のAPI", version="v1"
        ),
        name="openapi-schema",
    ),
    path(
        "",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]
