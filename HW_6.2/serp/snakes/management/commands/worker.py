from django.core.management.base import BaseCommand
from snakes.models import Snake

class Command(BaseCommand):
    help = 'Work with db'

    def handle(self, *args, **options):
        print('Hello from command')
        # # Удаление
        Snake.objects.all().delete()
        snake_example_1 = Snake.objects.create(name='Vanda', age=5)
        snake_example_1.save()
        snake_example_2 = Snake.objects.create(name='Liza', age=2)
        snake_example_2.save()