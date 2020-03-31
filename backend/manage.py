#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
<<<<<<< HEAD
<<<<<<< HEAD:backend/manage.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')
>>>>>>> c506cbd1d71bd82a448fd1435d17cb2f48643490:backend/Lib/site-packages/django/conf/project_template/manage.py-tpl
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
>>>>>>> c506cbd1d71bd82a448fd1435d17cb2f48643490
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


<<<<<<< HEAD
if __name__ == '__main__':
=======
if __name__ == "__main__":
>>>>>>> c506cbd1d71bd82a448fd1435d17cb2f48643490
    main()
