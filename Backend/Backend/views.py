from rest_framework import viewsets
from models import TestModel


class TestView(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return {"ok": True}