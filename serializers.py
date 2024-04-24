from rest_framework import serializers
from .models import Question, Option
# sets up two Django REST Framework (DRF) serializers, OptionSerializer and QuestionSerializer

# This serializer is for the Option model
class OptionSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    class Meta:
        model = Option
        fields = ['id', 'text']

    def get_id(self, obj):
    # Gets the index of the current option in all options and converts it to an ID of the form 'a', 'b', 'c'
        options_list = list(obj.question.options.all().order_by('id'))
        option_index = options_list.index(obj)
        return chr(97 + option_index)  # ASCII 'a' is 97

# This serializer is for the Question model and includes nested serialization for related "option" instances
class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True) # options: Uses the OptionSerializer to serialize the related Option instances. The many=True parameter indicates that a question can have multiple options, and read_only=True ensures these options are not expected from input during serialization, suitable for output serialization only.
    
    correctAnswer = serializers.SerializerMethodField() # SerializerMethodField that computes the correct answers differently based on the question type
    
    class Meta:
    #model: Specifies the Django model that the serializer should serialize
        model = Question
    #fields: Lists the model fields that should be included in the serialized output
        fields = ['id', 'text', 'options', 'correctAnswer', 'question_type']

# found similar code structures on google so I just grabbed multiple ideas and combined it here.
    def get_correctAnswer(self, obj):
        # Return the correct answer according to the question type
        options_list = list(obj.options.all().order_by('id'))
        if obj.question_type == Question.SINGLE:
            correct_option = obj.options.get(is_correct=True)
            index = options_list.index(correct_option)
            return chr(97 + index)
            # For multiple choice questions, multiple options can be correct. The method fetches all correct options using the filter(is_correct=True) method
        elif obj.question_type == Question.MULTIPLE:
            correct_options = obj.options.filter(is_correct=True)
            correct_ids = [chr(97 + options_list.index(opt)) for opt in correct_options]
            return correct_ids
