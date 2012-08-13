from wedding.settings.{{ environment }} import *

DATABASES['default']['NAME'] = '{{ db }}'

EMAIL_SUBJECT_PREFIX = '[wedding-{{ environment }}] '
