from smugmugcategory import *
from smugmugsubcategory import *

class SmugMugAlbum(object):
  def __init__(self, session_id=None):
    return

  def __stub__(self, returnlist):
    return returnlist

  def create(self, title, extra_args=None):
    stub_ret = { 
      'stat' : 'ok', 
      'Album' : {
        'id' : 1234, 
        'Key' : "abcd"
      } 
    }
    ret = self.__stub__( stub_ret )
    return ret['stat'], ret['Album']

  def delete(self, album_id, extra_args=None):
    stub_ret = { 'stat' : 'ok' }
    ret = self.__stub__( stub_ret )
    return ret['stat']


    ret = self.__stub__( stub_ret )
    return ret['stat'], ret['Albums']

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

  
