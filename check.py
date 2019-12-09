import random
from tkinter import *

movies = []
watched = []
watchlist = []
recommended_genre = set([])




def initialize_app():
	print("called")
	data = open("Data.csv","r")
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


	watched_data = open("watched.csv","r")
	for movie in watched_data.readlines():
		watched.append(movie.split(','))
	for movie in watched: #to bring all genres at one index
		temp = ""	
		for i in movie[4:]:			
			temp=temp + "," + str(i)
		for i in movie[4:]:
			movie.remove(i)
		movie.append(temp[1:])
	watched_data.close()

		
	watchlist_data = open("watchlist.csv","r")
	for movie in watchlist_data.readlines():
		watchlist.append(movie.split(','))
	for movie in watchlist: #to bring all genres at one index
		temp = ""	
		for i in movie[4:]:			
			temp=temp + "," + str(i)
		for i in movie[4:]:
			movie.remove(i)
		movie.append(temp[1:])
	watchlist_data.close()
	#print(watchlist)


	recommended_data = open("recommended_genre.txt","r")
	for i in recommended_data:
		recommended_genre.add(i)
	recommended_data.close()
	
	
	
		
def add_watchlist(r):
	for i in movies:
		if i[0]==r:
			watchlist.append(i)
			j = i[4].split(',')
			for k in j:
				recommended_genre.add(k)
			movies.remove(i)
			break




def add_watched(r,mode):
	if mode == 1:
		for i in watchlist:
			if i[0]==r:
				watched.append(i)
				j = i[4].split(',')
				print(j)
				for k in j:
					recommended_genre.add(k)
				watchlist.remove(i)
				break
	elif mode == 2:
		for i in movies:
			if i[0]==r:
				watched.append(i)
				j = i[4].split(',')
				for k in j:
					recommended_genre.add(k)
				movies.remove(i)
				break




recommended = []
def recommended_movies():
	j = set([])
	for i in range(random.randint(10,45)):
		random1 = random.randint(1,len(movies))
		l = movies[random1][4].split(',')
		for m in l:
			j.add(m)
		flag = 0
		for k in j:
			if k not in recommended_genre or k=='NaN' or k=='\n' or k=='Nan\n':
				flag += 1
		if flag == 0:
			recommended.append(movies[random1])
	#recommended1 = set(recommended)
	#print(recommended_genre)#print(recommended)
	display(recommended)



'''def display(list_given):
	print("{:15s}{:70s}{:15s}{:15s}{:15s}".format(movies[0][0],movies[0][1],movies[0][2],movies[0][3],movies[0][4]))
	for movie in list_given:
		print("{:15s}{:70s}{:15s}{:15s}{:15s}".format(movie[0],movie[1],movie[2],movie[3],movie[4]))
'''



def end_app():
	data = open("Data.csv","w")
	watched_data = open("watched.csv","w")
	watchlist_data = open("watchlist.csv","w")
	recommended_data = open("recommended_genre.txt","w")
	for i in movies:
		for j in i[:-1]:
			data.write(j)
			data.write(',')
		data.write(i[-1])
	data.close()
	for i in watched:
		for j in i[:-1]:
			watched_data.write(j)
			watched_data.write(',')
		watched_data.write(i[-1])
	watched_data.close()	
	for i in watchlist:
		for j in i[:-1]:
			watchlist_data.write(j)
			watchlist_data.write(',')
		watchlist_data.write(i[-1])	
	watchlist_data.close()		
	for i in list(recommended_genre):
		recommended_data.write(i)
		recommended_data.write('\n')		
	recommended_data.close()		
	



def display(my_list):
	window = Tk()
	if my_list == watchlist:
		i = "Watchlist"
	elif my_list == watched:
		i = "Watched"
	elif my_list == movies:
		i = "Movies"
	elif my_list == recommended:
		i = "Recommended"
	window.title(i)
	listbox1 = Listbox(window,height = 200,width = 200)
	listbox1.insert(END,"{:25}{:120}{:20}{:20}{:150}".format(movies[0][0],movies[0][1][:80],movies[0][2],movies[0][3],movies[0][4]))	
	for movie in my_list:
		listbox1.insert(END,"{:25}{:120}{:20}{:20}{:150}".format(movie[0],movie[1][:80],movie[2],movie[3],movie[4]))	
	listbox1.pack()
	window.mainloop()




#MAIN FUNTION
initialize_app()
print("1.Display Movies list\n2.Display Watchlist\n3.Display Watched\n4.Add to Watchlist\n5.Add to Watched\n6.Recommended\n7.Exit")
choice = 0
while choice != 7:
	choice = int(input("Enter your Choice: "))
	if choice == 1:
		display(movies)
	elif choice == 2:
		display(watchlist)
	elif choice == 3:
		display(watched)
	elif choice == 4:
		d = input("Enter the Id of the Movie: ")
		add_watchlist(d)
	elif choice == 5:
		mode = int(input("Where from(1.Watchlist or 2.Movies): "))
		d = input("Enter the Id of the Movie: ")
		add_watched(d,mode)
	elif choice == 6:
		recommended_movies()
	elif choice == 7:
		end_app()
		break

'''def createTable(self):
       # Create table
		self.tableWidget = QTableWidget()
		self.tableWidget.setColumnCount(5)
		self.tableWidget.setRowCount(len(movies))
		for i in range(len(movies)):
			for j in range(5):
				self.tableWidget.setItem(i,j,QTableWidgetItem(movies[i][j])


        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click) 


from tkinter import *
root = Tk()
cells = {}
for i in range(len(movies)):
	for j in range(len(movies[0])):
		b = Label(root,text = movies[i][j])
		b.grid(row = i,column = j)
	cells[i,j] = b
mainloop()

class table:
	def __init__(self,arr):
		root = Tk()
		for i in range(len(arr)):
			for j in range(len(arr[0])):
				lebel = Label(root,text = arr[i][j]
				label.grid(row = i,
		root.mainloop()
def window(my_list):
	root = Tk()
	
'''


