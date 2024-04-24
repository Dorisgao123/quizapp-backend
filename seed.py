from django.core.management.base import BaseCommand
from app.models import Question, Option
import random

class Command(BaseCommand):

# a brief description of what the command does
    help = 'Seeds the database with random questions and options'

# *args, **kwargs; These capture any additional positional or keyword arguments that might be passed to the command (not used in this script)
    def handle(self, *args, **kwargs):
        questions = [
            ("What is 1 + 1 equal to?", 'single', [("2", True), ("5", False), ("8", False)]),
            ("Which of the following is a ball game?", 'multiple', [("basketball", True), ("soccer", True), ("car racing", False)]),
            ("How many hours are there in a day?", 'single', [("12", False), ("24", True), ("72", False)]),
            ("What colors do traffic lights consist of?", 'multiple', [("red", True), ("black", False), ("green", True)]),
            ("How to calculate the area of a rectangle?", 'single', [("length * width", True), ("length * pi", False), ("Width * pi", False)])
        ]

        for text, q_type, options in questions:
            q = Question(text=text, question_type=q_type)
            q.save()
            for option_text, is_correct in options:
                Option(question=q, text=option_text, is_correct=is_correct).save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))
