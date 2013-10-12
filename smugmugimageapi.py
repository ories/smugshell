import smugmugglobals
import traceback

class SmugMugImageAPI(object):

  def __init__(self):
    self.handle = smugmugglobals.smugmughandle

    if self.handle == None:
      raise Exception("Handler not defined %s" % self.__module__)

  def check_response(self, response):
    if response['stat'] != 'ok':
      raise Warning("Server transaction failed!\n%s" % traceback.print_stack())
  
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


    
