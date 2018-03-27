import json

with open('movies.json', 'r') as data_file:
    json_data = data_file.read()

data = json.loads(json_data)

movies_by_title = {}
movies_by_actor = {}
actor_movie_pairs = []
checked_actors = []
all_matches = []

for movie in data:
	if(movie["cast"]):
		cast = movie["cast"].split(", ")
		
		movies_by_title[movie["title"]] = cast
		
		for actor in cast:
			actor_movie_pairs.append((actor,movie["title"],False))
			if actor in movies_by_actor:
				movies_by_actor[actor].append(movie["title"])
			else:
				movies_by_actor[actor] = [movie["title"]]



def get_actors_in_movie(movie):
	return movies_by_title[movie]

def get_movies_actor_in(actor):
	return movies_by_actor[actor]

def get_all_actors_in_movies_actor_in(actor):
	movies_in = get_movies_actor_in(actor)
	all_actors = []
	for movie in movies_in:
		actors_in_movie = get_actors_in_movie(movie)
		for actor_in_movie in actors_in_movie:
			if actor_in_movie not in all_actors:
				all_actors.append((actor_in_movie,movie))
	return all_actors


def find_bacon(actor,chain):
	if(chain == ""):
		chain += actor + " -> "
	actors_in_movie_actor_in = get_all_actors_in_movies_actor_in(actor)
	# print actors_in_movie_actor_in
	# return
	for bacon_check in actors_in_movie_actor_in:
		if bacon_check[0] == "Kevin Bacon":
			chain += " Kevin Bacon(" + bacon_check[1]+")"
			return "FOUND HIM " + chain
			# all_matches.append(chain)
	for actor_in in actors_in_movie_actor_in:
		if(actor_in[0] not in checked_actors):
			checked_actors.append(actor_in[0])
			chain  += actor_in[0] + "("+actor_in[1]+") -> "
			# find_bacon(actor_in[0],chain)
			return find_bacon(actor_in[0],chain)
	

# print actor_movie_pairs
print find_bacon("Simon Pegg","")
all_matches.sort(key = lambda x: x.split("->"))
# for match in all_matches:
# 	print match
# 	print "\n"

# print all_matches[0]
# print find_bacon("Fred Ward")
# print get_all_actors_in_movies_actor_in("Simon Pegg")
# print checked_actors
# print len(checked_actors)
# print find_bacon("Kevin Bacon")