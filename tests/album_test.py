#!/usr/bin/python

import sys
import smugpy
import unittest
import random
sys.path.append('../')

import smugmugglobals
import smugmugtests
from smugmugalbum import *



class SmugAlbumTests(unittest.TestCase):

  def setUp(self):  
    smugmugtests.prepare()

  def randomTitle(self):
    return "Title-%s" % random.randint(0,100)

  def test_create_and_delete_album(self):
    title = self.randomTitle()

    print "creating Album with Title %s" % title
    album = SmugMugAlbum()
    self.assertTrue(album.create( title ))

    print "deleting Album with Title %s" % title
    self.assertTrue(album.delete())

  def test_initFromName(self):
    title = self.randomTitle()
    album = SmugMugAlbum()
    
    print "creating Album with Title %s" % title
    album.create(title)

    testalbum = SmugMugAlbum()
    self.assertTrue(testalbum.initFromName(title))

    self.assertEqual(testalbum.id, album.id)
    self.assertEqual(testalbum.key, album.key)
    self.assertEqual(testalbum.category.id, album.category.id)
    self.assertEqual(testalbum.title, album.title)

    album.delete()
    testalbum.delete()



unittest.main()
  





