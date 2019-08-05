from django.core.management.base import BaseCommand, CommandError
from polls.models import Question, Author, Choice
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
import csv
import sys


class Command(BaseCommand):
    """Django command to import polls from a given CSV file"""

    help = "Import polls from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str,
                            help="""Enter with pathname of your CSV file. 
                            Example: python manage.py import_from_csv pgdata/polls.csv""")

    def handle(self, *args, **options):
        result = options['filename']
        if result:
            self.stdout.write(self.style.SUCCESS(
                'Saving to the database...'))
            return read_csv(result[0])


def read_csv(path):
    result = []
    with open(settings.BASE_DIR + path, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        col_names = [x.lower() for x in next(reader)]
        # Look through each line and construct dict
        [result.extend([dict(zip(col_names, line))]) for line in reader]

        save_to_database(result)


def save_to_database(polls):

    for poll in polls:
        try:
            Author.objects.get(name=poll['author'])
        except ObjectDoesNotExist:
            author = Author(name=poll['author'])
            author.save()

        try:
            Question.objects.get(question_text=poll['question'])
            sys.stderr.write(
                "Poll '{0}' is already in the database\n".format(poll['question']))
        except ObjectDoesNotExist:
            question = Question(
                question_text=poll['question'], pub_date=poll['pub_date'], author=author)
            question.save()

            for i in range(1, len(poll.values())-2):
                choice = Choice(question=question,
                                choice_text=poll['choice'+str(i)])
                choice.save()
