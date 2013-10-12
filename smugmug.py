from smugmugalbum import *

class SmugMug(object):
  def __init__(self):
    return

  def login(self):
    return

  def get_albums(self):
    stub_ret = { 
      'stat' : 'ok', 
      'Albums' : [ 
        { 
          'id' : 1234, 
          'Key':'abc', 
          'Category' : { 
            'id' : 0, 
            'Name' : 'name'
          }, 
          'Title' : 'foo' 
        },
        {
          'id' : 5678, 
          'Key':'fooabc', 
          'Category' : { 
            'id' : 1, 
            'Name' : 'name'
          }, 
          'Title' : 'bar' 
        }
      ]
    }

    ret = self.__stub__( stub_ret )

    ret_list = []

    for album in ret['Albums']:
      ret_list.append( SmugMugAlbum(album) )

    return ret_list
  
  def __stub__(self, returnlist):
    return returnlist

  def get_categories(self):
    return

