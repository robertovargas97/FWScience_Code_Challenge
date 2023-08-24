from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Fetches the planets data by using a specific query and then inserts the data into a database."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **kwargs):

        print("--- The command worked ---")
