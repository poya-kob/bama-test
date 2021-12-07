import datetime
import string
import os
import random


def create_year_choices(start_year: int, end_year=None):
    if start_year < 1980:
        start_year = 1980
    if not end_year:
        end_year = (datetime.datetime.now().year + 1)
    year_choices = [(r, r) for r in range(start_year, end_year)]
    return year_choices


def create_number_of_payments(num_of_pay=2):
    payment_choices = [(num, f"{num} pays") for num in range(1, (num_of_pay + 1))]
    return payment_choices


def get_file_name(filepath):
    size = 8
    chars = string.ascii_uppercase + string.digits
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    name = ''.join(random.choice(chars) for _ in range(size))
    return name, ext


def upload_image_path(instance, filename):
    date = datetime.datetime.now()
    name, ext = get_file_name(filename)
    new_name = f"{name}{ext}"
    return f"{type(instance).__name__}/{date.year}/{date.month}/{date.day}/{new_name}"
