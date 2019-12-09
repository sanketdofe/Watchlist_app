
data = open("Data.csv","r")
movies = [[]]
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



recommended_genre = set([])
recommended_data = open("recommended_genre.txt","r")
for i in recommended_data:
	recommended_genre.add(i)
recommended_data.close()
	
	

watched=[]
watchlist=[]


for i in movies[40:54]:
	watched.append(i)
	j = i[4].split(',')
	for k in j:
		recommended_genre.add(k)
	movies.remove(i)


for i in movies[476:498]:
	watchlist.append(i)
	j = i[4].split(',')
	for k in j:
		recommended_genre.add(k)
	movies.remove(i)


watched_data = open("watched.csv","w")
for i in watched:
	for j in i[:-1]:
		watched_data.write(j)
		watched_data.write(',')
	watched_data.write(i[-1])
watched_data.close()	
	


watchlist_data = open("watchlist.csv","w")
for i in watchlist:
	for j in i[:-1]:
		watchlist_data.write(j)
		watchlist_data.write(',')
	watchlist_data.write(i[-1])	
watchlist_data.close()



data1 = open("Data.csv","w")
for i in movies:
	for j in i[:-1]:
		data1.write(j)
		data1.write(',')
	data1.write(i[-1])
data1.close()


recommended_data = open("recommended_genre.txt","w")
for i in list(recommended_genre):
	recommended_data.write(i)
	recommended_data.write('\n')		
recommended_data.close()
