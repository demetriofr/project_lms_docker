from rest_framework.serializers import ValidationError


EXCEPT = 'https://www.youtube.com/'


class ExceptYouTubeValidator:
    """Checks the text for links to ensure there are no links to resources other than YouTube"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if not tmp_val.startswith(EXCEPT):
            raise ValidationError('All links blocked excepts YouTube links')
