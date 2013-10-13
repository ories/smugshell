#!/usr/bin/python

import sys
import random
import smugpy
sys.path.append('../')

import smugmugglobals

SCRIPT_NAME = 'smugloader'
API_KEY = 'phxpe0OJVIHhcqYD5lTHnwI2AQGH5blI'
USER_NAME = "olli@olli-ries.com"
PASSWORD = "Penelope22"
NICK_NAME = "ries"

def prepare():
  smugmugglobals.smugmughandle = smugpy.SmugMug(api_key=API_KEY, api_version="1.2.2", app_name=SCRIPT_NAME)
  smugmugglobals.smugmughandle.login_withPassword(EmailAddress=USER_NAME, Password=PASSWORD)
