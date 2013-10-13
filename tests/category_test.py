#!/usr/bin/python

import sys
import smugpy
import unittest
import random
sys.path.append('../')

import smugmugglobals
import smugmugtests
from smugmugcategory import *

class SmugCategoryTests(unittest.TestCase):

  def setUp(self):  
    smugmugtests.prepare()

  def randomTitle(self):
    return "Title-%s" % random.randint(0,100)

  def test_create_and_delete_category(self):
    title = self.randomTitle()

    print "creating Category with Title %s" % title
    category = SmugMugCategory()
    self.assertTrue(category.create( title ))

    print "deleting Category with Title %s" % title
    self.assertTrue(category.delete())

  def test_initFromName(self):
    title = self.randomTitle()
    category = SmugMugCategory()
    
    print "creating Category with Title %s" % title
    category.create(title)

    testcategory = SmugMugCategory()
    self.assertTrue(testcategory.initFromName(title))

    self.assertEqual(testcategory.id, category.id)
    self.assertEqual(testcategory.name, category.name)

    category.delete()
    testcategory.delete()

  def test_get_all_categories(self):
    categories = SmugMugCategory.getAllCategories()

    for category in categories:
      print "name: %s, id: %s" %( category.name, category.id)

#    i = smugmugglobals.smugmughandle.subcategories_getAll()
#    print i

#    i = smugmugglobals.smugmughandle.subcategories_get( CategoryID = 252721040 )
#    print i


unittest.main()
