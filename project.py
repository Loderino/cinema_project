class film:
    def __init__(self, n, reg, year, description = "",  photo ="аватарка.gif", actors = [], genre = [], rating = 0, category = "0+", country = []):
        self.name = n
        self.regiser = reg
        self.year = year
        self.description = description
        self.photo = photo
        self.actors = actors
        self.rating = rating
        self.genre = genre
        self.category = category
        self.country = country
    def add_actor(self, name, role):
        self.actors[role] = name

class actor:
    def __init__(self, name, photo = "аватарка.gif", films = [], description = ""):
        self.name = name
        self.photo = photo
        self.films = films
        self.description = description
    def add_film(self, film):
        self.films.append(film);

status = ""
films = [film("Любовь и голуби", "Хороший Г.А.", 1960, rating = 10), film("Иван Васильевич меняет профессию", "Гайдай Г.А.", 1973, rating = 9.9)]
actors = [actor("Сергей Безруков")]*10
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
    photo_group = Frame(work_area)
    photo = Label(photo_group, image = images[number], bg = "pink")
    rating = Label(photo_group, text = f"{films[number].rating}/10", font = "Arial 16 bold")
    photo.pack()
    rating.pack(pady = 20)
    photo_group.pack(side = RIGHT, anchor=NE, padx = 60, pady = 60)

    name = Label(work_area, text = f"{films[number].name}  ({films[number].year})", font = "Arial 30 bold", wraplength=1000)
    name.pack(pady = 60, padx = 20)
    desc = Label(work_area, text = films[number].description, font = "Arial 20", wraplength=1000)
    desc.pack(anchor = NW, padx=20, pady=60)

    about = Label(work_area, text = "О фильме",  font = "Arial 24 bold")
    about.pack(anchor = NW, padx=20, pady=30)

    countries = Label(work_area, text = "Производство: " + ", ".join(films[number].country), font = "Arial 18")
    genre = Label(work_area, text = "Жанр: " + ", ".join(films[number].genre), font = "Arial 18")
    reg = Label(work_area, text = "Режисёр: " + films[number].regiser, font = "Arial 18")
    age = Label(work_area, text = "Рейтинг: " + films[number].category, font = "Arial 18")

    countries.pack(anchor = NW, padx = 20, pady = 5)
    genre.pack(anchor = NW, padx = 20, pady = 5)
    reg.pack(anchor = NW, padx = 20, pady = 5)
    age.pack(anchor = NW, padx = 20, pady = 5)

    act = Label(work_area, text = "В ролях",  font = "Arial 24 bold")
    act.pack(anchor = NW, padx=20, pady=30)
    
    role = Label(work_area, text = ", ".join(films[number].actors), font = "Arial 14", wraplength=1500)    
    role.pack(anchor = NW, padx=20)

def open_actor(number):
    global status
    status = "actor"
    for widget in work_area.winfo_children():
            widget.destroy()

    photo = Label(work_area, image = images[number], bg = "pink")
    photo.pack(side = RIGHT, anchor=NE, padx = 60, pady = 60)

    name = Label(work_area, text = f"{actors[number].name}", font = "Arial 30 bold", wraplength=1000)
    name.pack(pady = 60, padx = 20)
    desc = Label(work_area, text = actors[number].description, font = "Arial 20", wraplength=1000)
    desc.pack(anchor = NW, padx=20, pady=60)

    act = Label(work_area, text = "Снимался в",  font = "Arial 24 bold")
    act.pack(anchor = NW, padx=20, pady=30)
    
    role = Label(work_area, text = ", ".join(actors[number].films), font = "Arial 14", wraplength=1500)    
    role.pack(anchor = NW, padx=20) 
    
def films_filling():
    global status
    if status == "films":
        return
    else:
        for widget in work_area.winfo_children():
            widget.destroy()
        images.clear()
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
                p = Label(f, image = images[4*i+j])
                n = Button(f, bg = "yellow", text = films[4*i+j].name)
                f.pack(side = LEFT, padx = 50)
                p.pack(side = TOP, pady = 20)
                n.configure(command = lambda x = 4*i+j: open_film(x))
                n.pack(side = TOP, pady = 20)
            work_area.create_window(0, 620*i, anchor=NW, window=group)
        #work_area.update_idletasks()
        print(len(images))

def on_resize(event):
    work_area.configure(scrollregion=work_area.bbox('all'))

def actors_filling():
    global status
    if status == "actors":
        return
    else:
        for widget in work_area.winfo_children():
            widget.destroy()
        images.clear()
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
                n.configure(command = lambda x = 4*i+j: open_actor(x))
                n.pack(side = TOP, pady = 20)
            work_area.create_window(0, 620*i, anchor=NW, window=group)

def new_film():
    global status
    if status == "new_film":
        return
    else:
        for widget in work_area.winfo_children():
            widget.destroy()
        images.clear()
        status = "actors"    
        films_button['bg'] = 'lightgray'
        actors_button['bg'] = 'lightgray'
        add_film_button['bg'] = 'darkgray'
        add_actor_button['bg'] = 'lightgray' 
        name_frame = Frame(work_area)
        name = Label(name_frame, text = "Название фильма")
        name_field = Entry(name_frame)
        name.pack(side = LEFT)
        name_field.pack(side = LEFT)
        name_frame.pack(pady=20)

        description_frame = Frame(work_area)
        description = Label(description_frame, text = "Описание")
        description_field = Text(description_frame, width = 50, height = 5)
        description.pack(side = LEFT)
        description_field.pack(side = LEFT)
        description_frame.pack(pady=20)

        reg_frame = Frame(work_area)
        reg = Label(reg_frame, text = "Режисёр")
        reg_field = Entry(reg_frame)
        reg.pack(side = LEFT)
        reg_field.pack(side = LEFT)
        reg_frame.pack(pady=20)

        year_frame = Frame(work_area)
        year = Label(year_frame, text = "Год")
        year_field = Entry(year_frame)
        year.pack(side = LEFT)
        year_field.pack(side = LEFT)
        year_frame.pack(pady=20)

        genre_frame = Frame(work_area)
        genre = Label(genre_frame, text = "Жанр")
        genre_field = Listbox(genre_frame, selectmode = MULTIPLE, height = 8)
        genre.pack(side = LEFT)
        genre_field.pack(side = LEFT)
        genre_frame.pack(pady=20)
        genres = ["Комедия", "Милодрама", "Детектив", "Фантастика", "Фентези", "Боевик", "Ужасы", "Историческое"]
        for i in range(len(genres)):
            genre_field.insert(i+1, genres[i])

        rating_frame = Frame(work_area)
        rating = Label(rating_frame, text = "Рейтинг")
        rating_field = Entry(rating_frame)
        rating.pack(side = LEFT)
        rating_field.pack(side = LEFT)
        rating_frame.pack(pady=20)

        age_frame = Frame(work_area)
        age = Label(age_frame, text = "Возрастная категория")
        age_field = Entry(age_frame)
        age.pack(side = LEFT)
        age_field.pack(side = LEFT)
        age_frame.pack(pady=20)

        actors_frame = Frame(work_area)
        actors = Label(actors_frame, text = "Актёры (перечислите через запятую)")
        actors_field = Text(actors_frame, width = 50, height = 5)
        actors.pack()
        actors_field.pack()
        actors_frame.pack(pady=20)

        countries_frame = Frame(work_area)
        countries = Label(countries_frame, text = "Страны (перечислите через запятую)")
        countries_field = Text(countries_frame, width = 50, height = 5)
        countries.pack()
        countries_field.pack()
        countries_frame.pack(pady=20)

        def apply():
            print()



        apply_button = Button(work_area, text = "Добавить фильм")
        apply_button.configure(command = apply)
        apply_button.pack(side=BOTTOM, pady=20)
        
films_button.configure(command = films_filling)
actors_button.configure(command = actors_filling)
add_film_button.configure(command = new_film)
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
