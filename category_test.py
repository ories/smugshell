#!/usr/bin/python

import smugpy
import smugmugglobals
from smugmugcategory import *
import smugmugcategoryapi

from smugmugalbum import *
import smugmugalbumapi
import sys
import random

sys.path.append('../')

SCRIPT_NAME = 'smugloader'
API_KEY = 'phxpe0OJVIHhcqYD5lTHnwI2AQGH5blI'
USER_NAME = "olli@olli-ries.com"
PASSWORD = "Penelope22"
NICK_NAME = "ries"

def prepare():
  smugmugglobals.smugmughandle = smugpy.SmugMug(api_key=API_KEY, api_version="1.2.2", app_name=SCRIPT_NAME)
  smugmugglobals.smugmughandle.login_withPassword(EmailAddress=USER_NAME, Password=PASSWORD)

def test_get_all_categories():
  a=SmugMugCategory.getAllCategories()
  for e in a:
    print "name: %s, id: %s" %( e.name, e.id)

  i = smugmugglobals.smugmughandle.subcategories_getAll()
  print i

  i = smugmugglobals.smugmughandle.subcategories_get( CategoryID = 252721040 )
  print i

def test_get_all_albums():
  a=SmugMugAlbum.getAllAlbums()
  for e in a:
    print "name: %s, id: %s\n\tcategory name: %s category id: %s\n" %( e.title, e.id, e.category.name, e.category.id)



def test_create_category():
  n = "Test-%s" % random.randint(0,100)
  a=SmugMugCategory.create( n )
  print n


def test_delete_category():
  a=SmugMugCategory.create("DeleteTest")
  a.delete()

def test_create_album():
  name = "TestAlbum-%s" % random.randint(0,100)
  print name
  album1 = SmugMugAlbum.create(name, 251743812)
  print album1.id
  print album1.category.name

  album2 = SmugMugAlbum.create(name, -1)
  print album2.id
  print album2.category.name
  
  album3 = SmugMugAlbum.create(name)
  print album3.id
  print album3.category.name

prepare()
#test_create_category()
#test_delete_category()
#test_create_album()
test_get_all_categories()
test_get_all_albums()
