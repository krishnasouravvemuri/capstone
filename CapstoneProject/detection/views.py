from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .emotion_detector import analyze_emotion
from .recommender import recommend_links

@api_view(["POST"])
@parser_classes([MultiPartParser])
def detect_emotion(request):
    """POST an image frame and get detected emotion."""
    try:
        image_file = request.FILES["image"]
        result = analyze_emotion(image_file.read())
        return Response(result)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(["GET"])
def get_recommendation(request):
    """GET /api/recommend/?emotion=happy&mode=spotify"""
    emotion = request.GET.get("emotion")
    mode = request.GET.get("mode", "spotify")
    url = recommend_links(emotion, mode)
    if url:
        return Response({"recommendation_url": url})
    return Response({"error": "Invalid mode or emotion."}, status=400)
