import smugpy

SCRIPT_NAME = 'smugloader'
API_KEY = 'phxpe0OJVIHhcqYD5lTHnwI2AQGH5blI'
USER_NAME = "olli@olli-ries.com"
PASSWORD = "Penelope22"
NICK_NAME = "ries"


smugmughandle = None
runtime = "production"

def init(apikey=None, apiversion=None, app_name=None):
  smugmughandle = smugpy.SmugMug( api_key = API_KEY, api_version = "1.2.2", app_name = SCRIPT_NAME)


