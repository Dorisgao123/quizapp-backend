from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer

class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# MVC M：Model V: views C: controller
