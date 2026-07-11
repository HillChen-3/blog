Title: Building RESTful APIs with Django REST Framework
Date: 2025-12-05 09:15
Category: Python
Tags: django, rest, api, python, backend
Slug: django-rest-framework-guide
Cover: images/drf-cover.jpg

Django REST Framework (DRF) is a powerful and flexible toolkit for building Web APIs in Django.

## Why DRF?

- **Web browsable API**: A developer-friendly interface for testing APIs
- **Authentication policies**: Built-in support for multiple auth methods
- **Serialization**: Simple yet powerful data serialization
- **ViewSets & Routers**: Reduce boilerplate code significantly

## Setup

```bash
pip install djangorestframework
```

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## Creating a Serializer

```python
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at']
```

## Views with ViewSets

```python
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
```

## URL Routing

```python
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
urlpatterns = router.urls
```

## Authentication

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

## Conclusion

Django REST Framework makes it incredibly easy to build robust, production-ready APIs. Its integration with Django's ORM and its extensive feature set make it the go-to choice for Django-based API development.
