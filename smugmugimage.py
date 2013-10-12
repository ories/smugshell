from smugmugglobals import runtime

if runtime == "testing":
    import smugmugmockapi as impl
else:
    import smugmugapi as impl

from smugmugcategory import *


class SmugMugImage(object):

  def __pre_init__(self)
    # members
    self.id = -1 # integer
    key = "" # string

  def __init__(self, data, session_id):
    # expecting:
    # { 'id' : 1234, 'Key':'abc' }
    self.__pre_init__()

    try: 
      self.id = data['id']
      self.key = data['Key']
    except:
      raise TypeError("data does not represent a valid image:\n\t%s" % data)

  def delete(self):
    return impl.SmugMugImageAPI().delete(self.id)

  def getInfo(self, album_id, album_key, extra_args=None):
    return

  def changeSettings(self, album_id, extra_args=None):
    return 

  def comments_add(self):
    return

  def comments_get(self):
    return

  
