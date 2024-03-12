import json

from django.core.management import BaseCommand

from lms.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Handle function to process payment data and create Payment objects.
        """

        payment_list = json.load(open('users/management/data/payments_data.json'))

        payments_for_create = []
        for payment_item in payment_list:

            user_id = payment_item.get('user')
            if user_id:
                user = User.objects.get(pk=user_id)
                payment_item['user'] = user
                course_id = payment_item.get('course')
                if course_id:
                    course = Course.objects.get(pk=course_id)
                    payment_item['course'] = course
                    payments_for_create.append(Payment(**payment_item))
                else:
                    lesson_id = payment_item.get('lesson')
                    lesson = Lesson.objects.get(pk=lesson_id)
                    payment_item['lesson'] = lesson
                    payments_for_create.append(Payment(**payment_item))

        Payment.objects.bulk_create(payments_for_create)
