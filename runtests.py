#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname, join

app_name = 'inte_reports'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    SITE_ID=100,
    COUNTRY="uganda",
    APP_NAME=app_name,
    ETC_DIR=os.path.join(base_dir, app_name, "tests", "etc"),
    SUBJECT_CONSENT_MODEL="inte_consent.subjectconsent",
    SUBJECT_VISIT_MODEL="inte_subject.subjectvisit",
    SUBJECT_REQUISITION_MODEL="inte_subject.subjectrequisition",
    ADVERSE_EVENT_ADMIN_SITE="inte_ae_admin",
    ADVERSE_EVENT_APP_LABEL="inte_ae",
    EDC_BOOTSTRAP=3,
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    EMAIL_CONTACTS={
        "data_request": "someone@example.com",
        "data_manager": "someone@example.com",
        "tmg": "someone@example.com",
    },
    EMAIL_ENABLED=True,
    HOLIDAY_FILE=join(base_dir, app_name, "tests", "holidays.csv"),
    LIVE_SYSTEM=False,
    RANDOMIZATION_LIST_PATH=join(base_dir, app_name, "tests"),
    EDC_RANDOMIZATION_REGISTER_DEFAULT_RANDOMIZER=False,
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "django_celery_beat",
        "django_celery_results",
        "edc_action_item.apps.AppConfig",
        "edc_auth.apps.AppConfig",
        "edc_adverse_event.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_data_manager.apps.AppConfig",
        "edc_dashboard.apps.AppConfig",
        "edc_export.apps.AppConfig",
        # "edc_navbar.apps.AppConfig",
        "edc_pharmacy.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_facility.apps.AppConfig",
        "edc_offstudy.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        "edc_locator.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_list_data.apps.AppConfig",
        "edc_metadata.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_prn.apps.AppConfig",
        "edc_protocol.apps.AppConfig",
        "edc_randomization.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "edc_visit_tracking.apps.AppConfig",
        "inte_ae.apps.AppConfig",
        "inte_consent.apps.AppConfig",
        "inte_labs.apps.AppConfig",
        "inte_lists.apps.AppConfig",
        "inte_prn.apps.AppConfig",
        "inte_reports.apps.AppConfig",
        "inte_screening.apps.AppConfig",
        "inte_sites.apps.AppConfig",
        "inte_subject.apps.AppConfig",
        "inte_visit_schedule.apps.AppConfig",
    ],
    add_dashboard_middleware=True,
    use_test_urls=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split('=')[1] for t in sys.argv if t.startswith('--tag')]
    failures = DiscoverRunner(failfast=False, tags=tags).run_tests(
        [f'{app_name}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
