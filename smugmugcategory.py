from smugmugglobals import runtime

if runtime == "testing":
    import smugmugmockapi as impl
else:
    import smugmugapi as impl

class SmugMugCategory(object):
  def __pre_init__(self):
    # members
    self.id = -1 # integer
    self.name = ""
    self.nicename = ""
    self.type = ""

  def __init__(self, data):
    
    self.__pre_init__()

    try: 
      self.id = data['id']
      self.name = data['Name']
    except:
      raise TypeError("Data does not represent a valid Category:\n\t%s" % data)

    keys = data.keys()

    if 'NiceName' in keys:
      self.nicename = data['NiceName']

    if 'Type' in keys:
      self.type = data['Type']


  def __stub__(self, returnlist):
    return returnlist

  @classmethod
  # returns instance but can also be called from instance - use with care
  # TODO
  def create(cls, name, extra_args=None):
    category = impl.SmugMugCategoryAPI().create(name)

    if category == None:
      return None
    else:
      try:
        ret = cls(category)
      except Exception as msg:
        print msg
        return None

    return ret

  @classmethod
  def getAllCategories(self):
    categories = impl.SmugMugCategoryAPI().categories_get()
    ret_list = []
    
    if len(categories) == 0:
      return ret_list

    for category in categories:
      ret_list.append(SmugMugCategory(category))

    return ret_list  
  
  def delete(self):
    return impl.SmugMugCategoryAPI().delete(self.id)

  def rename(self, newname):
    return


