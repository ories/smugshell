class SmugMugAlbumAPI(object):
  def albums_get(self, data=None):
    if data != None:
      return data
   
    ret = [
            { "id": 1234, 
              "Key": "xCXXu", 
              "Category": 
              { 
                "id": 0,
                "Name": "Other"
              }, 
              "Title": "My Birthday 2008" 
            }
          ] 

    return ret

  def create(self, name, category_id=None, subcategory_id=None, data=None):
    if data != None:
      return data
    
    ret = { 
          "id": 1234,
          "Key": "xCXXu" 
      }
    
    return ret

  def delete(self, what, data=None):
    if data != None:
      return data

    ret = { 
        #"stat": "ok", 
        #"method": "smugmug.albums.delete"
      }

    return True

class SmugMugCategoryAPI(object):
  def categories_get(self, data=None):
    if data != None:
      return data

    ret = {
          #"stat": "ok", 
          #"method": "smugmug.categories.get",
          "Categories": [ 
            { 
              "id": 0,
              "Name": "Other",
              "NiceName": "Other",
              "Type": "SmugMug" 
            },
            {
              "id": 1,
              "Name": "Animals",
              "NiceName": "Animals",
              "Type": "SmugMug"
            } 
          ]
        }

    return ret

  def create(self, data=None):
    if data != None:
      return data

    ret = {
        #"stat": "ok",
        #"method": "smugmug.categories.create",
        "Category": 
          { 
            "id": 1234 
          } 
        }

    return ret

  def delete(self, what, data=None):
    if data != None:
      return data

    ret = {
         # "stat": "ok",
          #"method": "smugmug.categories.delete" 
        }

    return True

class SmugMugImageAPI(object):
  def delete(self, what, data=None):
    if data != None:
      return data

    ret = {
            #"stat": "ok",
            #"method": "smugmug.images.delete"
          }
    return True

