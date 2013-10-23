from __future__ import absolute_import

from django.core.management.base import BaseCommand
from django.conf import settings

from zerver.models import AppleDeviceToken

from zerver.lib.push_notifications import check_apns_feedback
import logging

class Command(BaseCommand):
    help = """Checks the Apple Push Notifications Service for any tokens that have been
              invalidated, and removes them from the database.

    Usage: ./manage.py check_apns_tokens"""

    def handle(self, *args, **options):
        check_apns_feedback()
