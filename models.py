from django.db import models

class Question(models.Model):
    SINGLE = 'single'
    MULTIPLE = 'multiple'
    QUESTION_TYPES = [
        (SINGLE, 'Single Choice'),
        (MULTIPLE, 'Multiple Choice')
    ]
#  store the text of the question
    text = models.TextField(verbose_name="Question Text")
    question_type = models.CharField(
        max_length=8,
        choices=QUESTION_TYPES,
        default=SINGLE,
        verbose_name="Type of Question"
    )
#The string representation method returns the text of the question when an instance of Question is printed or used in a string context. This enhances readability, especially in admin interfaces or debug outputs
    def __str__(self):
        return self.text


class Option(models.Model):
# ForeignKey linking each Option to a Question
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE) # related_name='options' allows reverse lookup, where you can access all options related to a question via question.options
    text = models.CharField(max_length=200, verbose_name="Option Text")
    is_correct = models.BooleanField(default=False, verbose_name="Is Correct Answer") # A BooleanField indicating whether the option is the correct answer to the question. It defaults to False, meaning that options are incorrect unless explicitly set to be correct

# The string representation method for the Option model provides a string that includes the text of the option and indicates whether it is correct. The format is "Option Text (Correct)" or "Option Text (Incorrect)," which is particularly useful for quick identification in administrative views or debugging sessions

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Incorrect'})"
