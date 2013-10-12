from smugmugglobals import runtime

if runtime == "testing":
  import smugmugmockapi as impl
else:
  import smugmugapi as impl

from smugmugcategory import *

class SmugMugAlbum(object):
  def __pre_init__(self):
    # members
    self.id = -1 # integer
    self.key = "" # string
    self.category = None # class category
    self.subcategory = None # class subcategory
    self.title = ""

  def __init__(self, data):
    # expecting:
    # { 'id' : 1234, 'Key':'abc', 'Category' : {'id' : 0, 'Name' : 'name'}, 'SubCategory' : {'id' : 0, 'Name' : 'name'}', Title' : 'foo'} 
    self.__pre_init__()

    try: 
      self.id = data['id']
      self.key = data['Key']
      self.category = SmugMugCategory(data['Category'])
      self.title = data['Title']
    except Exception as msg:
      print msg
      raise TypeError("data does not represent a valid album:\n\t%s" % data)

  def __stub__(self, returnlist):
    return returnlist

  @classmethod
  # returns instance but can also be called from instance - use with care
  # TODO
  def create( cls, title, category_id = None, subcategory_id = None ):
    album = impl.SmugMugAlbumAPI().create( title, category_id, subcategory_id )

    if album == None:
      return None
    else:
      try:
        ret = cls(album)
      except Exception as msg:
        print msg
        return None

    return ret

  @classmethod
  def getAllAlbums(self):
    albums = impl.SmugMugAlbumAPI().albums_get()
    ret_list = []

    if len(albums) == 0:
      return ret_list

    for album in albums:
      ret_list.append( SmugMugAlbum(album) )

    return ret_list
    
  def delete(self, album_id, extra_args=None):
    return impl.SmugMugAlbumAPI().delete(self.id)

  def getImages(self):
    images = impl.SmugMugImageAPI().images_get(self.id, self.key) 
    ret_list = []

    if len(images) == 0:
      return ret_list

    for image in images:
      ret_list.append(SmugMugImage(image))

    return ret_list

  def getInfo(self, album_id, album_key, extra_args=None):
    stub_ret = { 
      "stat": "ok", 
      "method": "smugmug.albums.getInfo", 
      "Album": { 
        "id": 1234, 
        "Key": "xCXXu", 
        "Backprinting": "", 
        "CanRank": "true", 
        "Category": { 
          "id": 0, 
          "Name": "Other" 
        }, 
        "Clean": "false", 
        "ColorCorrection": 0, 
        "Comments": "true", 
        "Description": "Photos from my party.", 
        "EXIF": "true", 
        "External": "false", 
        "FamilyEdit": "true", 
        "FriendEdit": "true", 
        "Geography": "false", 
        "Header": "true", 
        "HideOwner": "false", 
        "ImageCount": 20, 
        "Larges": "true", 
        "LastUpdated": "", 
        "NiceName": "My-Birthday-2008", 
        "Originals": "false", 
        "Password": "1973", 
        "PasswordHint": "What year was I born ?", 
        "Position": 1, 
        "Printable": "true", 
        "ProofDays": 1, 
        "Protected": "false", 
        "Public": "false", 
        "Share": "true", 
        "SmugSearchable": "true", 
        "SortDirection": "false", 
        "SortMethod": "Position", 
        "SquareThumbs": "true", 
        "Template": { "id": 0 }, 
        "Title": "My Birthday 2008", 
        "Type": "Album", 
        "URL": "http://fred.smugmug.com/Other/My-Birthday-2008/1234_xCXXu", 
        "UnsharpAmount": 0.2, 
        "UnsharpRadius": 1, 
        "UnsharpSigma": 1, 
        "UnsharpThreshold": 0.05, 
        "UploadKey": "", 
        "Watermark": { 
          "id": 0, 
          "Name": "SmugMug" 
        }, 
        "Watermarking": "false",
        "WorldSearchable": "true", 
        "XLarges": "true", 
        "X2Larges": "true", 
        "X3Larges": "true" 
      } 
    }
    ret = self.__stub__( stub_ret )
    return ret

  def changeSettings(self, album_id, extra_args=None):
    stub_ret = { 
      'stat' : 'ok', 
      'Album' : {
        'id' : 1234, 
        'Key' : "abcd"
      } 
    }
    
    ret = self.__stub__( stub_ret )
    return ret['stat'], ret['Album']

  def comments_add(self):
    return

  def comments_get(self):
    return

  
