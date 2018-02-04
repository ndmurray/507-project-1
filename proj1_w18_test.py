import unittest
import proj1_w18 as proj1


#Part 1 - Test classes

#Test Media (Class admins started it)
class TestMedia(unittest.TestCase):

	m1 = proj1.Media()
	m2 = proj1.Media("1999", "Prince", "1982")

	def testConstructor(self):

		#m1
		self.assertEqual(TestMedia.m1.title, "No Title")
		self.assertEqual(TestMedia.m1.author, "No Author")
		self.assertEqual(TestMedia.m1.release_year, "No Release Year")
		#Making sure song and movie classes aren't present
		with self.assertRasies(AttributeError):
			Testmedia.m1.album
		with self.assertRasies(AttributeError):
			Testmedia.m1.genre

		#m2
		self.assertEqual(TestMedia.m2.title, "1999")
		self.assertEqual(TestMedia.m2.author, "Prince")
		self.assertEqual(TestMedia.m2.release_year, "1982")

	def testString(self):

		#m1
		self.assertEqual(str(TestMedia.m1),"No Title by No Author (No Release Year)")

		#m2
		self.assertEqual(str(TestMedia.m2),"1999 by Prince (1982)")
		
	def testLen(self):

		#m1
		self.assertEqual(len(TestMedia.m1),0)

		#m2
		self.assertEqual(len(TestMedia.m2),0)

#Test Song
class TestSong(unittest.TestCase):

	s1 = proj1.Song()
	s2 = proj1.Song("Short Skirt Long Jacket", "Cake", "2001", "Comfort Eagle", "Alt Rock", "204000")

	def TestConstructor(self):

		#s1
		self.assertEqual(TestSong.s1.album, "No Album")
		self.assertEqual(TestSong.s1.genre, "No Genre")
		self.assertEqual(TestSong.s1.track_length, 0)
		#Test class doesn't have instance variable HOW???

		#s2
		self.assertEqual(TestSong.s2.album, "Comfort Eagle")
		self.assertEqual(TestSong.s2.genre, "Alt Rock")
		self.assertEqual(TestSong.s2.track_length, 204)


	def TestString(self):

		#s1
		self.assertEqual(str(TestSong.s1),)

		pass

	def TestLen(self):

		pass








unittest.main()
