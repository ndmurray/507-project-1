import unittest
import proj1_w18 as proj1
import test_data #sample json for part 2 tests

############################
#     Part 1 
############################

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
		with self.assertRaises(AttributeError):
			TestMedia.m1.genre
		with self.assertRaises(AttributeError):
			TestMedia.m1.album
		with self.assertRaises(AttributeError):
			TestMedia.m1.track_length
		with self.assertRaises(AttributeError):
			TestMedia.m1.rating
		with self.assertRaises(AttributeError):
			TestMedia.m1.movie_length

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

	def testConstructor(self):

		#s1
		self.assertEqual(TestSong.s1.album, "No Album")
		self.assertEqual(TestSong.s1.genre, "No Genre")
		self.assertEqual(TestSong.s1.track_length, 0)
		#Testing class doesn't have movie attributes
		with self.assertRaises(AttributeError):
			TestMedia.m1.rating
		with self.assertRaises(AttributeError):
			TestMedia.m1.movie_length

		#s2
		self.assertEqual(TestSong.s2.album, "Comfort Eagle")
		self.assertEqual(TestSong.s2.genre, "Alt Rock")
		self.assertEqual(int(TestSong.s2.track_length), 204000)


	def testString(self):

		#s1
		self.assertEqual(str(TestSong.s1),"No Title by No Author (No Release Year) [No Genre]")
		#s2
		self.assertEqual(str(TestSong.s2),"Short Skirt Long Jacket by Cake (2001) [Alt Rock]")
	
	def testLen(self):

		#s1
		self.assertEqual(len(TestSong.s1),0)
		#s2
		self.assertEqual(len(TestSong.s2),204)

class TestMovie(unittest.TestCase):

	mov1 = proj1.Movie()
	mov2 = proj1.Movie("Full Metal Jacket", "Stanley Kubrick", "1987", "R","7020000")

	def testConstructor(self):

		#s1
		self.assertEqual(TestMovie.mov1.rating, "No Rating")
		self.assertEqual(TestMovie.mov1.movie_length, 0)
		#Testing class doesn't have movsongie attributes
		with self.assertRaises(AttributeError):
			TestMovie.mov1.genre
		with self.assertRaises(AttributeError):
			TestMovie.mov1.track_length
		with self.assertRaises(AttributeError):
			TestMovie.mov1.album

		#s2
		self.assertEqual(TestMovie.mov2.rating, "R")
		self.assertEqual(int(TestMovie.mov2.movie_length), 7020000)


	def testString(self):

		#s1
		self.assertEqual(str(TestMovie.mov1),"No Title by No Author (No Release Year) [No Rating]")
		#s2
		self.assertEqual(str(TestMovie.mov2),"Full Metal Jacket by Stanley Kubrick (1987) [R]")
	
	def testLen(self):

		#s1
		self.assertEqual(len(TestMovie.mov1),0)
		#s2
		self.assertEqual(len(TestMovie.mov2),117)

############################
#     Part 2
############################

test_media = test_data.test_other
test_song = test_data.test_song
test_movie = test_data.test_movie

class TestClasses (unittest.TestCase):

	media = proj1.Media(json_dict = test_media)
	song = proj1.Song(json_dict = test_song)
	movie = proj1.Movie(json_dict = test_movie)

	def testMediaAttributes(self):
		self.assertEqual(TestClasses.media.title,"WTF with Marc Maron Podcast")
		self.assertEqual(TestClasses.media.author,"Marc Maron")
		self.assertEqual(TestClasses.media.release_year,"2018")
		self.assertEqual(TestClasses.media.url,"https://itunes.apple.com/us/podcast/wtf-with-marc-maron-podcast/id329875043?mt=2&uo=4")

	def testMediaStr(self):
		self.assertEqual(str(TestClasses.media),"WTF with Marc Maron Podcast by Marc Maron (2018)")

	def testMediaLen(self):
		self.assertEqual(len(TestClasses.media),0)

	def testSongAttributes(self):
		self.assertEqual(TestClasses.song.title,"At Last")
		self.assertEqual(TestClasses.song.author,"Etta James")
		self.assertEqual(TestClasses.song.release_year,"1960")
		self.assertEqual(TestClasses.song.url,"https://itunes.apple.com/us/album/at-last/1115802590?i=1115802822&uo=4")
		self.assertEqual(TestClasses.song.album,"At Last!")
		self.assertEqual(TestClasses.song.genre,"Blues")
		self.assertEqual(TestClasses.song.track_length,181373)

	def testSongStr(self):
		self.assertEqual(str(TestClasses.song),"At Last by Etta James (1960) [Blues]")

	def testSongLen(self):
		self.assertEqual(len(TestClasses.song),181)

	def testMovieAttributes(self):
		self.assertEqual(TestClasses.movie.title,"Harry Potter and the Sorcerer's Stone")
		self.assertEqual(TestClasses.movie.author,"Chris Columbus")
		self.assertEqual(TestClasses.movie.release_year,"2001")
		self.assertEqual(TestClasses.movie.url,"https://itunes.apple.com/us/movie/harry-potter-and-the-sorcerers-stone/id271469503?uo=4")
		self.assertEqual(TestClasses.movie.movie_length,9141663)
		self.assertEqual(TestClasses.movie.rating,"PG")

	def testMovieStr(self):
		self.assertEqual(str(TestClasses.movie),"Harry Potter and the Sorcerer's Stone by Chris Columbus (2001) [PG]")

	def testMovieLen(self):
		self.assertEqual(len(TestClasses.movie),152)
		
############################
#     Part 3
############################


class TestResults(unittest.TestCase):

	wide_query1 = proj1.get_itunes_data("baby")
	wide_query2 = proj1.get_itunes_data("love")

	narrow_query1 = proj1.get_itunes_data("Frequenzfett")
	narrow_query2 = proj1.get_itunes_data("Minor Swag")

	trash_query1 = proj1.get_itunes_data("sad;lkew;ilasoi")
	trash_query2 = proj1.get_itunes_data("776s9s99")

	def testWide(self):
		self.assertEqual(len(TestResults.wide_query1),50)
		self.assertEqual(len(TestResults.wide_query2),50)

	def testNarrow(self):
		self.assertLessEqual(len(TestResults.narrow_query1),5)
		self.assertLessEqual(len(TestResults.narrow_query2),5)

	def testTrash(self):
		self.assertEqual(len(TestResults.trash_query1),0)
		self.assertEqual(len(TestResults.trash_query2),0)

unittest.main(verbosity=2)
