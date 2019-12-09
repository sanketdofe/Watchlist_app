import tkinter as tk
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
	
watched_data = open("watched.csv","r")
watched = []
for movie in watched_data.readlines():
	watched.append(movie)



#based_on_interest = []




watchlist_data = open("watchlist.csv","r")
watchlist = []
for movie in watchlist_data.readlines():
	watchlist.append(movie)




def add_watchlist(index):
	temp=movies[index]
	watchlist.append(temp)
	movies.remove(temp)




def add_watched(movie,mode):
	watched.append(movie)
	if mode==1:
		watched.remove()
	elif mode == 2:
		watchlist.remove()




def display(list_given):
	for movie in list_given:
		print("{:15s}{:60s}{:10s}{:10s}{:10s}".format(movie[0],movie[1],movie[2],movie[3],movie[4]))



def display_movies():
	display(movies)
root = tk.Tk()
root.title("Watchlist ")
def movies_window():
	window2 = tk.Toplevel(root)
	listbox1 = tk.Listbox(window2,height = 200,width = 200,command = tk.yview)
	for movie in movies:
		listbox1.insert(tk.END,"{:15}{:120}{:20}{:20}{:150}".format(movie[0],movie[1][:80],movie[2],movie[3],movie[4]))	
	listbox1.pack()
	v1 = tk.Button(window2,text = "Add to Watchlist",width = 15)#,command = add_watchlist(listbox1.curselection()))
	v1.pack(justify=tk.LEFT)
	v2 = tk.Button(window2,text = "Add to Watched",width = 15)
	v2.pack(justify=tk.LEFT)	
	
	
w1 = tk.Button(root,text='Movies list',width = 10,command = movies_window)
w2 = tk.Button(root,text='Watchlist',width=10)
w3 = tk.Button(root,text='Recommended',width=10)
w4 = tk.Button(root,text='Watched',width=10)
w5 = tk.Button(root,text='Favourites',width=10)
w6 = tk.Button(root,text='Exit',width=10,command=root.destroy)
w1.pack()
w2.pack()
w3.pack()
w4.pack()
w5.pack()
w6.pack()
root.mainloop()
