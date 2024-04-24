import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
# first ever migration, independent
    initial = True

# this empty list doesnt depend on any other migrations from other apps
    dependencies = []

# migration performing, creating 2 new databases
    operations = [
        
        #This model represents a question in a quiz, storing its content and the type of question
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Question Text")),
                (
                    "question_type",
                    models.CharField(
                        choices=[
                            ("single", "Single Choice"),
                            ("multiple", "Multiple Choice"),
                        ],
                        default="single",
                        max_length=8,
                        verbose_name="Type of Question",
                    ),
                ),
            ],
        ),
        # Represents an answer option to a specific question. It includes the text of the answer, whether it is correct, and which question it belongs to.
        migrations.CreateModel(
            name="Option",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=200, verbose_name="Option Text")),
                (
                    "is_correct",
                    models.BooleanField(
                        default=False, verbose_name="Is Correct Answer"
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        
                        # argument specifies that if the linked Question is deleted, then all associated Option instances will also be deleted
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="options",
                        to="app.question",
                    ),
                ),
            ],
        ),
    ]
