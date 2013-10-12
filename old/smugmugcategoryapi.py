class SmugMugCategory(object):
  def __init__(self, id, name, nicename, type):
    self.id = id
    self.name = name
    self.nicename = nicename
    self.type = type



class SmugMugCategoryAPI(object):
  def __init__(self, session_id=None):
    return

  def __stub__(self, returnlist):
    return returnlist

  def get(self):
    stub_ret = {
        'stat' : 'ok',
        'categories' : (
          )
      }
    
    ret = self.__stub__( stub_ret )
    return ret['stat'], ret['categories']


