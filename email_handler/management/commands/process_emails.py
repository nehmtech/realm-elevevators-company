from django.core.management.base import BaseCommand
from django.core import mail


class Command(BaseCommand):
    help = 'Process incoming emails'

    def handle(self, *args, **options):
        connection = mail.get_connection()
        connection.username = 'quotes@realmelevators.com'
        connection.password = 'Realmelevators2023'
        connection.open()

        messages = connection.get_messages()
        for message in messages:
            # process the message
            print(message.subject)

        connection.close()
