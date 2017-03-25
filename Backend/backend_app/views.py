from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from SentimentClassifier.SentimentClassifier import SentimentClassifier


sentiment_classifier = SentimentClassifier()


@api_view(['GET', 'POST'])
def test_view(request, format=None):
    if request.method == 'GET':
        return JsonResponse({"ok": True, "message": "GET to test_view"}, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        print request.data
        return JsonResponse({"ok": True, "received": request.data["sent"]}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def classify(request, format=None):
    if request.method == 'GET':
        return JsonResponse({}, safe=False, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        print request.data
        return JsonResponse({}, safe=False, status=status.HTTP_200_OK)