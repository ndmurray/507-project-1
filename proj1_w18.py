import requests
import json
import sys
import webbrowser

########################
#     Classes
########################

#MEDIA PARENT CLASS
class Media:

	def __init__(self, title="No Title", author="No Author", release_year="No Release Year", json_dict = None):
		if json_dict == None:
			self.title = title
			self.author = author
			self.release_year = release_year
			self.url = None
		else:
			self.title = json_dict['trackName']
			self.author = json_dict['artistName']
			self.release_year = json_dict['releaseDate'][:4]
			self.url = json_dict['trackViewUrl']

	def __str__(self):
		return "{} by {} ({})".format(self.title,self.author,self.release_year)

	def __len__(self):
		return 0

print(Media())

#SONG SUBCLASS
class Song(Media):

	def __init__(self, title="No Title", author="No Author", release_year="No Release Year", album = "No Album", genre = "No Genre",
		track_length = 0, json_dict = None):

		super().__init__(title, author, release_year, json_dict)
		if json_dict == None:
			self.album = album
			self.genre = genre
			self.track_length = track_length
		else:
			self.album = json_dict['collectionName']
			self.genre = json_dict['primaryGenreName']
			self.track_length = json_dict['trackTimeMillis']


	def __str__(self):
		return super().__str__() + " [{}]".format(self.genre)

	def __len__(self):
		return int(int(self.track_length) / 1000) ##According to API docs track length returns in miliseconds - https://apple.co/2zHPSFZ

#MOVIE SUBCLASS

class Movie(Media):

	def __init__(self, title="No Title", author="No Author", release_year="No Release Year", rating = "No Rating", movie_length = 0, json_dict = None):

		super().__init__(title, author, release_year, json_dict)
		if json_dict == None:
			self.rating = rating
			self.movie_length = int(movie_length)
		else:
			self.rating = json_dict['contentAdvisoryRating']
			self.movie_length = int(json_dict['trackTimeMillis'])


	def __str__(self):
		return super().__str__() + " [{}]".format(self.rating)

	def __len__(self):
		return int(int(self.movie_length) / 60000) #Movie length also returned in miliseconds

## Other classes, functions, etc. should go here

if __name__ == "__main__":
	# your control code for Part 4 (interactive search) should go here
	pass

##########################################
#     API Requests and Data Formating
##########################################


#Caching system

#-Specify cache file

CACHE_FILE_NAME = "proj1_cache.json"

#-Load the cache file into a python dictionary

try:
	cache_file = open(CACHE_FILE_NAME, 'r')
	cache_str = cache_file.read()
	CACHE_DICT = json.loads(cache_str)
except:
	CACHE_DICT = {}

#-Define the unique identifer function

def unique_id(baseurl, params_dict):
	sorted_keys = sorted(params_dict.keys())
	result = []
	for item in sorted_keys:
		result.append("{}-{}".format(item,params_dict[item]))
	return baseurl + "_".join(result)

#Define the function for formatting API results

def format_data(unique_ident):
	results = []
	#print(CACHE_DICT[unique_ident]['results'][0]['kind'])
	#print(len(CACHE_DICT[unique_ident]['results']))
	item_list = CACHE_DICT[unique_ident]['results']
	# print(item_list[0].keys())
	for item in item_list:
		if 'kind' in item:
			if item['kind'] == 'song':
				results.append(Song(json_dict = item))
			elif item['kind'] == 'feature-movie':
				results.append(Movie(json_dict = item))
			else:
				results.append(Media(json_dict = item))
	return results

#Request data from iTunes API

#-Data request function

def get_itunes_data(term):

	#Data request components
	baseurl = "https://itunes.apple.com/search"
	params_dict = {
		'term': term
	}

	#Pull data from web or cache depending on unique request identifier
	unique_ident = unique_id(baseurl, params_dict)

	if unique_ident in CACHE_DICT:
		#Get Data from cache
		print("Getting cached iTunes data")
		return format_data(unique_ident)
	else:
		#Get data from iTunes API
		print("Requesting new data from iTunes API")
		resp = requests.get(baseurl,params_dict)
		print("iTunes request status:" + str(resp.status_code))
		#Add response to cache dictionary
		CACHE_DICT[unique_ident] = json.loads(resp.text)
		dumped_data = json.dumps(CACHE_DICT)
		cache_write_file = open(CACHE_FILE_NAME, 'w')
		cache_write_file.write(dumped_data)
		cache_write_file.close()
		print("New iTunes data written to cache")
		return format_data(unique_ident)

###############################
# User interface
###############################

# def user_query(search_term):
# 	print("Welcome to the iTunes data portal! Wubbba lubbba dub dubbb!\n")

# 	if search_term == "exit":
# 		print("Okay, peace.")
# 		exit()
# 	else:
# 		query_results = get_itunes_data(search_term)

# 		songs = []
# 		movies = []
# 		other = []

# 		for item in query_results:
# 			if isinstance(item,Song):
# 				songs.append(item)
# 			elif isinstance(item,Movie):
# 				movies.append(item)
# 			elif isinstance(item,Media):
# 				other.append(item)

# 		result_count = input("How many results you wanna preview from each category? ")


# 		print("Okay boss check out this preview:\n")
# 		print("SONGS:\n")
# 		if len(songs) == 0:
# 			print("No songs boss.")
# 		else:
# 			num = 1
# 			for song in songs[:int(result_count)]:
# 				print(str(num) + ". " + str(song))
# 				num += 1 
# 			print("\n")

# 		print("MOVIES:\n")
# 		if len(movies) == 0:
# 			print("No movies chief.")
# 		else:
# 			for movie in movies[:int(result_count)]:
# 				print(str(num) + ". " + str(movie))
# 				num += 1
# 			print("\n")

# 		print("OTHER MEDIA:\n")
# 		if len(other) == 0:
# 			print("No other media chief.\n")
# 		else:
# 			for other_item in other[:int(result_count)]:
# 				print(str(num) + ". " + str(other_item))
# 				num += 1
# 			print("\n")

# 		full_list = songs + movies + other
		
# 		output = {}

# 		for item in range(num):
# 			output[item] = full_list[item]

# 		return output

# search_term = input("What is the term you want to search biggity boss? If you don't want nothing, just write 'exit'\n")
# output = user_query(search_term)


# follow_up = input("Enter a number for more info, or another search term, or exit.\n")

# if int(follow_up) / int(follow_up) == 1:
# 	print("Launching item #" + follow_up + " in web browser.")
# 	webbrowser.open(output[int(follow_up)].url)

# else:
# 	user_query(follow_up)



