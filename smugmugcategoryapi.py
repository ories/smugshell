import smugmugglobals
import traceback

class SmugMugCategoryAPI(object):

  def __init__(self):
    self.handle = smugmugglobals.smugmughandle

    if self.handle == None:
      raise Exception("Handler not defined %s" % self.__module__)

  def check_response(self, response):
    if response['stat'] != 'ok':
      raise Warning("Server transaction failed!\n%s" % traceback.print_stack())

  def categories_get(self):
    response = self.handle.categories_get()
  
    try:
      self.check_response(response)
    except Warning as msg:
      print msg
      
    try:
      retlist = response['Categories']
    except:
      raise KeyError("Response is not formatted correctly, module %s, line %s" % (__module__, __line__) )

    return retlist
   
  def create(self, name):
    if name == "":
      raise ValueError("Category name required to create category, module %s, line %s" % (__module__, __line__) )

    try:
      response = self.handle.categories_create( Name=name, Unique=True)
    except Exception as msg:
      print "Error: %s" % msg
      return None

    try:
      self.check_response(response)
    except Warning as msg:
      print msg
      return None

    updated_categories = self.categories_get()

    iterator = iter( updated_categories )
    cat = iterator.next()
    while cat['id'] != response['Category']['id']:
      cat = iterator.next()

    return cat

  def delete(self, what):
    t = type(what)
    if t == str:
      return self.delete_by_name(what)
    elif t == int:
      return self.delete_by_id(what)
    else:
      raise Warning("Not a valid ID or Name for category: %s, module %s, line %s" % (what, __module__, __line__) )
      return False


  def delete_by_name(self, name):
    # expensive! use delete_by_id whenever you can
    categories = self.categories_get()
    iterator = iter( categories )
    category = iterator.next()

    while category['Name'] != name:
      category = iterator.next()

    return self.delete_by_id( category['id'] )
    
  def delete_by_id(self, id):

    try:
      response = self.handle.categories_delete( CategoryID = id)
    except Exception as msg:
      print "Error: %s" % msg
      return False

    return True


    
