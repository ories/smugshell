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

  def __init__(self, data = None):
    
    self.__pre_init__()

    if data != None:
      try: 
        self.id = data['id']
        self.name = data['Name']
      except Exception as msg:
        print msg
        raise TypeError("Data does not represent a valid Category:\n\t%s" % data)

      keys = data.keys()

      if 'NiceName' in keys:
        self.nicename = data['NiceName']

      if 'Type' in keys:
        self.type = data['Type']

  def initFromName(self, name):
    ret = False

    categories = impl.SmugMugCategoryAPI().categories_get()

    for category in categories:
      if category['Name'] == name:
        self.initFromData( category )
        ret = True
        break

    return ret  

  def initFromData( self, data ):
    self.__init__(data)


  def __stub__(self, returnlist):
    return returnlist

  def create(self, name, extra_args=None):
    ret = False
    category = impl.SmugMugCategoryAPI().create(name)

    if category == None:
      ret = False
    else:
      try:
        self.initFromData(category)
        ret = True
      except Exception as msg:
        print msg
        ret = False

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


