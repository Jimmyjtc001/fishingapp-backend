"""
foundation/drf/custom_authentication.py
"""
from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    https://stackoverflow.com/a/30875830
    """

    def enforce_csrf(self, request):
        return
