class film:
    def __init__(self, n, reg, year, photo ="аватарка.gif", actors = {}, genre = [], rating = 0, category = "0+"):
        self.name = n
        self.regiser = reg
        self.year = year
        self.photo = photo
        self.actors = actors
        self.rating = rating
        self.genre = genre
        self.category = category
    def add_actor(self, name, role):
        self.actors[role] = name

class actor:
    def __init__(self, name, photo = "аватарка.gif", films = []):
        self.name = name
        self.photo = photo
        self.films = films
    def add_film(self, film):
        self.films.append(film);

status = ""

films = [film("Любовь и голуби", "Хороший Г.А.", 1960)]*10
actors = [actor("Сергей Безруков")]*5
images = []
from tkinter import *
window = Tk() 
window.title("КиноПрятки")
menu = Frame(window, bg="green")
work_area = Canvas(window)




films_button = Button(menu, width = 20, height = 2, bg = "lightgray" , fg ="black", text = "Фильмы", font = "Arial 16") 
actors_button = Button(menu, width = 20, height = 2, bg = "lightgray" , fg ="black", text = "Актёры", font = "Arial 16")
add_film_button = Button(menu, width = 20, height = 2, bg = "lightgray" , fg ="black", text = "Добавить фильм", font = "Arial 16") 
add_actor_button = Button(menu, width = 20, height = 2, bg = "lightgray" , fg ="black", text = "Добавить актёра", font = "Arial 16")

def open_film(number):
    global status
    status = "film"
    for widget in work_area.winfo_children():
            widget.destroy()

def films_filling():
    global status
    if status == "films":
        return
    else:
        for widget in work_area.winfo_children():
            widget.destroy()
        status = "films"    
        films_button['bg'] = 'darkgray'
        actors_button['bg'] = 'lightgray'
        add_film_button['bg'] = 'lightgray'
        add_actor_button['bg'] = 'lightgray' 
       
        for i in range(len(films)//4 + 1):
            group = Canvas(work_area)
            group.pack()
            if (i*4) >= len(films):
                break
            for j in range(4):
                if (i*4+j)>= len(films):
                    break
                f = Frame(group)
                img = PhotoImage( file = films[4*i+j].photo , width = 300, height = 500)
                images.append(img);
                p = Label(f, image = images[-1])
                n = Button(f, bg = "yellow", text = films[4*i+j].name)
                f.pack(side = LEFT, padx = 50)
                p.pack(side = TOP, pady = 20)
                n.pack(side = TOP, pady = 20)
                n.configure(command = lambda: open_film(i*4+j))
            work_area.create_window(0, 150+620*i, anchor=NW, window=group)
        #work_area.update_idletasks()

def on_resize(event):
    work_area.configure(scrollregion=work_area.bbox('all'))

def actors_filling():
    global status
    if status == "actors":
        return
    else:
        for widget in work_area.winfo_children():
            widget.destroy()
        status = "actors"    
        films_button['bg'] = 'lightgray'
        actors_button['bg'] = 'darkgray'
        add_film_button['bg'] = 'lightgray'
        add_actor_button['bg'] = 'lightgray' 
        
        for i in range(len(actors)//4 + 1):
            group = Canvas(work_area)
            group.pack()
            if (i*4) >= len(actors):
                break
            for j in range(4):
                if (i*4+j)>= len(actors):
                    break
                f = Frame(group)
                img = PhotoImage( file = actors[4*i+j].photo , width = 300, height = 500)
                images.append(img);
                p = Label(f, image = images[-1])
                n = Button(f, bg = "yellow", text = actors[4*i+j].name)
                f.pack(side = LEFT, padx = 50)
                p.pack(side = TOP, pady = 20)
                n.pack(side = TOP, pady = 20)
            work_area.create_window(0, 150+620*i, anchor=NW, window=group)
        #work_area.update_idletasks()



films_button.configure(command = films_filling)
actors_button.configure(command = actors_filling)
films_button.pack()
actors_button.pack()
add_film_button.pack()
add_actor_button.pack()
menu.pack(side = LEFT, expand = 0, fill = Y)


work_area.pack(side=LEFT, fill=BOTH, expand=True)
scroll = Scrollbar(window, orient = VERTICAL, command =work_area.yview)
scroll.pack(side=RIGHT, fill=Y)
work_area.config(yscrollcommand = scroll.set)

window.bind('<Configure>', on_resize)

window.mainloop()
