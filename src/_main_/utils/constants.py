"""
This file contains Global constants used throughout the codebase.
"""

from _main_.settings import IS_PROD, IS_CANARY, BASE_DIR
from _main_.utils.utils import load_json


GLOBAL_SITE_SETTINGS = {"ADMIN_SITE_HEADER": "MassEnergize SuperAdmin Portal"}

CREATE_ERROR_MSG = "An error occurred during creation."

READ_ERROR_MSG = "An error occurred while fetching the requested resource(s)"

COMMUNITY_URL_ROOT = (
    "https://community.massenergize.org"
    if IS_PROD
    else "https://community-canary.massenergize.org"
    if IS_CANARY
    else "https://community.massenergize.dev"
)
#COMMUNITY_SANDBOX_URL_ROOT = (
#    "https://sandbox.community.massenergize.org"
#    if IS_PROD
#    else "https://sandbox.community-canary.massenergize.org"
#    if IS_CANARY
#    else "https://sandbox.community-dev.massenergize.org"
#)
ADMIN_URL_ROOT = (
    "https://admin.massenergize.org"
    if IS_PROD
    else "https://admin-canary.massenergize.org"
    if IS_CANARY
    else "https://admin.massenergize.dev"
)

SLACK_COMMUNITY_ADMINS_WEBHOOK_URL = "https://hooks.slack.com/workflows/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"


# TODO: @Add more words to this reserved list
RESERVED_SUBDOMAIN_LIST = load_json(
    BASE_DIR + "/_main_/utils/json_files/reserved_subdomains.json"
)
