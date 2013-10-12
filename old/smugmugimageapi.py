class SmugMugImage:
  def __init__(self, id, key=None):
    self.id = id
    self.key = key

class SmugMugImageAPI(object):
  def __init__(self, session_id=None):
    return

  def __stub__(self, returnlist):
    return returnlist

  def __to_object_list__(self, data):
    ret = []
    for d in data:
      ret.append(self.__to_object__(d))
    return ret
  
  def __to_object__(self, data):
    keys = data.keys()
    id = ""
    key = ""
    if 'id' in keys:
      id = data['id']
    if 'key' in keys:
      key = data['Key']

    return SmugMugImage( id, key )



  def get(self, album_id, album_key):
    stub_ret = {
      'stat' : 'ok', 
      'Album' : { 
        'id' : 1234, 
        'Key':'abc', 
        'ImageCount' : 2, 
        'Images' : [ 
          {'id' : 1234, 'key' : 'avsas'}, 
          {'id' : 5678, 'key':'asdd'} 
        ] 
      }
    }

    ret = self.__stub__( stub_ret )
    return ret['stat'], ret['Album'], ret['Album']['Images']

