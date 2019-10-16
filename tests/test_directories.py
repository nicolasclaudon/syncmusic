import unittest
import os
import fs.directories

class Test_Directories(unittest.TestCase):
    
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))

    def setUp(self):
        self.artist = os.path.join(self.THIS_DIR, os.pardir, 'data/Adele')
        self.album = os.path.join(self.THIS_DIR, os.pardir, 'data/Adele/21')
        self.emptyalbum = os.path.join(self.THIS_DIR, os.pardir, 'data/Adele/19')

    def test_is_there_a_subdir(self):
        # Adele contains two subdirs, they shoumd be detected
        self.assertTrue(fs.directories.there_is_a_subdirectory(self.artist))
        self.assertFalse(fs.directories.there_is_a_subdirectory(self.album))

    def test_Adele_is_an_artist(self):
        self.assertTrue(fs.directories.this_is_an_artist(self.artist))
        self.assertFalse(fs.directories.this_is_an_artist(self.album))

    def test_21_is_an_album(self):
        self.assertTrue(fs.directories.this_is_an_album(self.album))
        self.assertFalse(fs.directories.this_is_an_album(self.artist))
        self.assertFalse(fs.directories.this_is_an_album(self.emptyalbum))

    def test_albums_list_should_contains_21_19(self):
        albums_list = fs.directories.get_album_list(self.artist)
        album_present = False
        if "21" in albums_list:
            album_present = True
        self.assertTrue(album_present)

    def test_there_is_a_flac(self):
        self.assertTrue(fs.directories.there_is_a_flac(self.album))

if __name__ == '__main__':
    unittest.main()