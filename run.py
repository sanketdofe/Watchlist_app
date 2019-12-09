
data = open("Data.csv","r")
movies = []
for movie in data.readlines():
	movies.append(movie.split(","))
for movie in movies: #to bring all genres at one index
	temp = ""	
	for i in movie[4:]:			
		temp=temp + "," + str(i)
	for i in movie[4:]:
		movie.remove(i)
	movie.append(temp[1:])
data.close()


print(movies[3:8])
