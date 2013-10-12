#!/usr/bin/python

import smugpy
import getpass
import sys
import os
import getopt
import hashlib

SCRIPT_NAME = 'smugloader'
API_KEY = 'phxpe0OJVIHhcqYD5lTHnwI2AQGH5blI'
USER_NAME = "olli@olli-ries.com"
PASSWORD = "Penelope22"
NICK_NAME = "ries"

smugmug = smugpy.SmugMug(api_key=API_KEY, api_version="1.2.2", app_name=SCRIPT_NAME)

create_missing = False
create_local = False

# Public API

def upload_folder( FolderName, AlbumName, CategoryName = "", hidden=False ):
  #login
  login()

  category_id = -1

  # if CategoryName was given
  if CategoryName != "":
    # translate album name into id
    category_id = get_category_id( CategoryName )

  # Category not found, but --create 
  if category_id == -1:
    if not CategoryName == "" and create_missing == True:
      print "Category %s not found, creating it..." % (CategoryName)
      category_id = create_category( CategoryName )
    elif CategoryName == "":
      # this defaults to Category "Other" in my tests
      category_id = ""
    else:
      print "Error: Category not found please use --create to create a new category"
      sys.exit(2)

  # find an album for AlbumName
  album_id, foo = get_album_id( AlbumName, category_id )
  
  # no album found
  if album_id == -1:
    if create_missing == True:
      print "Album %s not found, creating it..." % (AlbumName)
      album_id = create_album( AlbumName, category_id, hidden )
    else:
      print "Error: Album not found, please use --create to create any missing albums"
      sys.exit(2)

  
  files = find_files_in_folder( FolderName )

  for file in files:
    if os.path.isfile(file):
      if file.rpartition('.')[2] in ("jpg", "png"):
        upload_file(file, album_id, hidden )
      else:
        print "Warning: not uploading unrecognized file type: %s" % file

def upload_file( file, albumID, hidden=False ):
  print "Uploading %s" % file
  ret = smugmug.images_upload( File=file, AlbumID=albumID )
  if ret['stat'] == "ok":
    print "\tUploaded picture %s to adress %s" % (file, ret['Image']['URL'])
  else:
    print "Error: There was an issue uploading %s\n\tErrorCode: %s" % (file, ret)
  return ret

def find_files_in_folder(folder):
  return [os.path.join(path, file) for (path, dirs, files) in os.walk(folder) for file in files]

def update_folder( FolderName, CategoryName, AlbumName, hidden=False ):
  return


def usage():
  print "usage:"
  return


def login():
  smugmug.login_withPassword(EmailAddress=USER_NAME, Password=PASSWORD)
  
def create_category( CategoryName ):
  ret = smugmug.categories_create( Name=CategoryName, Unique=True)
  return ret['Category']['id']

def create_album( AlbumName, CategoryID, hidden=False ):
  ret = smugmug.albums_create( Title=AlbumName, CategoryID=CategoryID, Public=not hidden, Heavy=True, Unique=True)
  URL = smugmug.albums_getInfo( AlbumID=ret['Album']['id'], AlbumKey=ret['Album']['Key'] )
  print "\tAlbum created at URL: %s" % URL['Album']['URL']
  return ret['Album']['id']


def get_album_id( AlbumName, CategoryId ):
  ret = []
  
  # query all albums
  albums = smugmug.albums_get( NickName = NICK_NAME)

  # find matching album entries
  if CategoryId == "":
    for album in albums['Albums']:
      if album['Title'] == AlbumName:
        ret.append( (album['id'], album['Key'], album['Title'] ))
  else:
    for album in albums['Albums']:
      if album['Title'] == AlbumName:
        if album['Category']['id'] == CategoryId:
          ret.append( (album['id'], album['Key'], album['Title'] ))

  # multiple albums matched, need to be unique
  if len( ret ) > 1:
    print "Error: could not uniquely identify an Album with the Title", AlbumName
    for t in ret:
      URL = smugmug.albums_getInfo( AlbumID=t[0], AlbumKey=t[1] )
      print "Album %s at URL: %s" % (t[2], URL['Album']['URL'])
    sys.exit(2)
  # no result found  
  elif len( ret ) == 0:  
    ret = (-1, -1)
  else:
    ret = (ret[0][0], ret[0][1])

  # return index of element of first of tupel in list
  return ret

def get_category_id( CategoryName ):
  
  categories = smugmug.categories_get( NickName = NICK_NAME )

  for category in categories['Categories']:
    if category['Name'] == CategoryName:
      return category['id']

  # Category doesn't exist
  return -1


def parse_args( opts, args, valid_args ):
  return -1

def name_is_valid(name, what):
  
  if not name[0].isupper() and not name[0].isdigit():
    print "Error: %s name %s must start with uppercase letter or be a number" % (what, name)
    sys.exit(2)

def update_md5sum( directory ):

  files = find_files_in_folder( directory )
  data = []

  for file in files:
    if file.rpartition('/')[2] == "MUGSUM":
      continue
    if os.path.isfile(file):
      data.append( (file, file_md5sum(file)) )
    else:
      print "Warning: Skipping %s" % (file)

  md5sum_file = directory + "/MUGSUM"

  with open( md5sum_file, 'w') as f:
    for name, md5 in data:
      s = "%s;%s\n" % (name.rpartition('/')[2], md5)
      f.write(s)

  return data
  
def file_md5sum(file):
  with open(file, 'rb') as fh:
    m = hashlib.md5()
    while True:
      data = fh.read(8192)
      if not data:
        break

      m.update(data)

  return m.hexdigest()

def album_md5sums( category, album ):
  category_id = -1
  album_id = -1

  ret = []

  if category != "":
    category_id = get_category_id( category )

  if album != "":
    album_id, album_key = get_album_id( album, category_id )

  images = smugmug.images_get( AlbumID = album_id, AlbumKey = album_key, Heavy = True)

  for image in images['Album']['Images']:
    ret.append( (image['FileName'], image['MD5Sum']) )

  return ret



def compare_md5sums( directory, category, album ):

  login()

  local_data = []
  remote_data = []

  compare = {}

  if not os.path.isfile(directory + "/MUGSUM"):
    local_data = update_md5sum( directory )
  else:
    content = open( directory + "/MUGSUM", "r")
    for line in content:
      name, md5 = line.split(";")
      local_data.append( (name, md5.replace('\n','') ) )

  remote_data = album_md5sums(category, album)

  for element in local_data:
    compare[ element[0] ] = [ -1, -1 ]
    compare[ element[0] ][0] = element[1]

  for element in remote_data:
    if element[0] in compare.keys():
      compare[ element[0] ][1] = element[1]
    else:
      compare[ element[0] ] = [-1, -1]
      compare[ element[0] ][1] = element[1] 

  for pic in compare:
    s = "picture %s " % pic

    if compare[pic][0] == compare[pic][1]:
      s += " is identical"
    elif compare[pic][0] == -1 and compare[pic][1] != -1:
      s += " does not exist locally"
    elif compare[pic][1] == -1 and compare[pic][0] != -1:
      s += " does not exist remotely"
    elif compare[pic][0] != compare[pic][1]:
      s += " are not identical"
    else:
      s = "Warning: unmatched case"

    print s

if __name__ == "__main__":

  # multi purpose executable
  base = os.path.basename( sys.argv[0] )

  # TODO - handle password/user

  # see how we were called
  if base == "smuguploader":
    directory =""
    category = ""
    album =""
    invisible = False
  # parse argv 
    try:
      opts, args = getopt.getopt( sys.argv[1:],"d:c:a:i",[ "directory=","category=", "album=", "invisible", "create" ])
    except getopt.GetoptError:
      usage()
      sys.exit(2)

    for o, a in opts:
      if o in ("-d", "--directory"):
        directory = a
      elif o in ("-c", "--category"):
        category = a
        name_is_valid(category, "Category")
      elif o in ("-a", "--album"):
        album = a
        name_is_valid(album, "Album")
      elif o in ("-i", "--invisible"):
        invisible = True
      elif o == "--create":
        create_missing = True
      else:
        assert False, "unhandled option"

    # sanity check
    if directory =="" or album == "":
        usage()
        sys.exit(2)

    upload_folder( directory, album, category, invisible )

  elif base == "smugupdater": 
    args = parse_args()

  elif base == "smugchecker":
    directory = ""
    category = ""
    album = ""
    try:
      opts, args = getopt.getopt( sys.argv[1:],"d:c:a:", ["directory", "category", "album", "create"])
    except getopt.GetoptError:
      usage()
      sys.exit(2)

    for o, a in opts:
      if o in ("-d", "--directory"):
        directory = a
      elif o in ("-c", "--category"):
        category = a
      elif o in ("-a", "--album"):
        album = a
      elif o == "--create":
        create_local = True
      else:
        assert False, "unhandled option"

    if directory =="":
      usage()
      sys.exit(2)

    if create_local:
      update_md5sum( directory )
    else:
      if category == "" or album == "":
        usage()
        sys.exit(2)
      else:  
        compare_md5sums( directory, category, album )

  else:
    usage()
  sys.exit()
