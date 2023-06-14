class film:
    def __init__(self, n, reg, year, description = "",  photo ="img//noimg.jpg", actors = [], genre = [], rating = 0, category = "0+", country = []):
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

class actor:
    def __init__(self, name, photo = "img//noimg.jpg", films = [], description = ""):
        self.name = name
        self.photo = photo
        self.films = films
        self.description = description

status = ""
full_films =  []
films = full_films
actors = []
images = []
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog as fd
import math
window = Tk() 
window.title("КиноПрятки")
menu = Frame(window, bg="green")
work_area = Canvas(window, bg = "#505050")
scroll = Scrollbar(window, orient = VERTICAL, command =work_area.yview)

films_button = Button(menu, width = 20, height = 2, bg = "lightgray" , fg ="black", text = "Фильмы", font = "Arial 16") 
actors_button = Button(menu, width = 20, height = 2, bg = "lightgray" , fg ="black", text = "Актёры", font = "Arial 16")
add_film_button = Button(menu, width = 20, height = 2, bg = "lightgray" , fg ="black", text = "Добавить фильм", font = "Arial 16") 
add_actor_button = Button(menu, width = 20, height = 2, bg = "lightgray" , fg ="black", text = "Добавить актёра", font = "Arial 16")
save_data_button = Button(menu, width = 20, height = 2, bg = "lightgray" , fg ="black", text = "Сохранить", font = "Arial 16")
load_data_button = Button(menu, width = 20, height = 2, bg = "lightgray" , fg ="black", text = "Открыть", font = "Arial 16")
def on_resize(event):
    work_area.configure(scrollregion=work_area.bbox('all'))

def select_file(number, tp):
        status = "select"
        name = fd.askopenfilename(filetypes=(("Images","*.gif *.png *.jpeg *.jpg"),  ("All files", "*.*")))
        if name == "":
            return
        if not name.endswith(".gif") and not name.endswith(".png") and not name.endswith(".jpeg") and not name.endswith(".jpg"):
            messagebox.showinfo("Ошибка", "Формат выбранного файла не поддерживается")
            return
        if tp==1:
            films[number].photo = name
            films_filling()
        else:
            actors[number].photo = name
            actors_filling()
        return

def open_film(number):
    global status, films
    if status == "films":
        scroll.pack_forget()
    status = "film"
    for widget in work_area.winfo_children():
            widget.destroy()
    photo_group = Frame(work_area, width = 300, height = 450, bg = "darkgrey")
    photo = Label(photo_group, image = images[number], bg = "white", highlightthickness=4, highlightbackground="#000000")
    rating = Label(photo_group, text = f"{films[number].rating}/10", font = "Arial 32 bold", bg = "darkgrey")
    photo.pack()
    rating.pack(pady = 20)
    change_photo_button = Button(photo_group, text = "Выбрать другое фото")
    change_photo_button.pack()
    change_photo_button.configure(command = lambda : select_file(number, 1))
    photo_group.pack(side = RIGHT, anchor=NE, padx = 60, pady = 60)

    name = Label(work_area, text = f"{films[number].name}  ({films[number].year})", font = "Arial 30 bold", wraplength=1000, bg = "#505050")
    name.pack(pady = 60, padx = 20)
    
    desc = Label(work_area, text = films[number].description, font = "Arial 20", wraplength=1000, bg = "#505050")
    desc.pack(anchor = NW, padx=20, pady=60)

    about = Label(work_area, text = "О фильме",  font = "Arial 24 bold", bg = "#505050")
    about.pack(anchor = NW, padx=20, pady=30)

    countries = Label(work_area, text = "Производство: " + ", ".join(films[number].country), font = "Arial 18", bg = "#505050")
    countries.pack(anchor = NW, padx = 20, pady = 5)
    
    genre = Label(work_area, text = "Жанр: " + ", ".join(films[number].genre), font = "Arial 18", bg = "#505050")
    genre.pack(anchor = NW, padx = 20, pady = 5)
    
    reg = Label(work_area, text = "Режисёр: " + films[number].regiser, font = "Arial 18", bg = "#505050")
    reg.pack(anchor = NW, padx = 20, pady = 5)
    
    age = Label(work_area, text = "Рейтинг: " + films[number].category, font = "Arial 18", bg = "#505050")
    age.pack(anchor = NW, padx = 20, pady = 5)

    act = Label(work_area, text = "В ролях:",  font = "Arial 24 bold", bg = "#505050")
    act.pack(anchor = NW, padx=20, pady=30)
    
    role = Label(work_area, text = ", ".join(films[number].actors), font = "Arial 14", wraplength=1000, bg = "#505050")    
    role.pack(anchor = NW, padx=20)
    films = full_films

def open_actor(number):
    global status, films
    if status == "actors":
        scroll.pack_forget()
    films = full_films
    status = "actor"
    for widget in work_area.winfo_children():
            widget.destroy()
    photo_group = Frame(work_area, bg = "darkgrey")
    photo = Label(photo_group, image = images[number], bg = "white", highlightthickness=4, highlightbackground="#000000" )
    photo.pack()
    change_photo_button = Button(photo_group, text = "Выбрать другое фото")
    change_photo_button.pack(pady=20)
    change_photo_button.configure(command = lambda : select_file(number, 2))
    photo_group.pack(side = RIGHT, anchor=NE, padx = 60, pady = 60)
    
    name = Label(work_area, text = f"{actors[number].name}", font = "Arial 30 bold", wraplength=1000, bg = "#505050")
    name.pack(pady = 60, padx = 20)
    
    desc = Label(work_area, text = actors[number].description, font = "Arial 20", wraplength=1000, bg = "#505050")
    desc.pack(anchor = NW, padx=20, pady=60)

    fil = Label(work_area, text = "Снимался в",  font = "Arial 24 bold", bg = "#505050")
    fil.pack(anchor = NW, padx=20, pady=30)
    
    role = Label(work_area, text = ", ".join(actors[number].films), font = "Arial 14", wraplength=1500, bg = "#505050")    
    role.pack(anchor = NW, padx=20)

    work_area.config(yscrollcommand = scroll.set)

    
    
def films_filling(f_text = ""):
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

        def find_films(text):
            global status, films
            films = full_films
            status = ""
            if text == "":
                films = full_films
            else:
                films = list(filter(lambda x: x.name.lower().find(text.lower().strip())+1, films))
            films_filling(f_text = text)

        scroll.pack(side=RIGHT, fill=Y)
        find_frame = Frame(work_area, bg = "#505050")
        find_field = Entry(find_frame, font = "Arial 24", highlightthickness = 4, highlightbackground = "#000000", width = 50)
        find_field.pack(side = LEFT)
        find_field.insert(0, f_text)
        find_button = Button(find_frame, text = "Найти",  font = "Arial 16")
        find_button.configure(command = lambda : find_films(find_field.get()))
        find_button.pack(side = LEFT, expand  = 1, fill = X)
        work_area.create_window(800, 0, window=find_frame, height=50)
        
        for i in range(math.ceil(len(films)/4)):
            group = Canvas(work_area, bg = "#505050", highlightthickness=0)
            group.pack()
            if (i*4) >= len(films):
                break
            for j in range(4):
                if (i*4+j)>= len(films):
                    break
                f = Frame(group, bg = "#505050")
                img = ImageTk.PhotoImage(Image.open(films[4*i+j].photo).crop((0, 0, 300, 450)), width = 300, height = 450, )
                images.append(img);
                p = Label(f, image = images[4*i+j], highlightthickness=4, highlightbackground="#000000")
                n = Button(f, bg = "yellow", text = films[4*i+j].name)
                f.pack(side = LEFT, padx = 50)
                p.pack(side = TOP, pady = 20)
                n.configure(command = lambda x = 4*i+j: open_film(x))
                n.pack(side = TOP, pady = 20)
            work_area.create_window(0, 620*i + 100, anchor=NW, window=group)
        work_area.config(yscrollcommand = scroll.set)

def actors_filling():
    global status, films
    films = full_films
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

        scroll.pack(side=RIGHT, fill=Y)
        for i in range(math.ceil(len(actors)/4)):
            group = Canvas(work_area, bg = "#505050", highlightthickness = 0)
            group.pack()
            if (i*4) >= len(actors):
                break
            for j in range(4):
                if (i*4+j)>= len(actors):
                    break
                f = Frame(group, bg = "#505050")
                img = ImageTk.PhotoImage(Image.open(actors[4*i+j].photo).crop((0, 0, 300, 450)), width = 300, height = 450 )
                images.append(img);
                p = Label(f, image = images[-1], highlightthickness=4, highlightbackground="#000000")
                n = Button(f, bg = "yellow", text = actors[4*i+j].name)
                f.pack(side = LEFT, padx = 50)
                p.pack(side = TOP, pady = 20)
                n.configure(command = lambda x = 4*i+j: open_actor(x))
                n.pack(side = TOP, pady = 20)
            work_area.create_window(0, 620*i, anchor=NW, window=group)
        work_area.config(yscrollcommand = scroll.set)

def new_film():
    global status, films
    if status == "films" or status == "actors":
        scroll.pack_forget()
    films = full_films
    if status == "new_film":
        return
    else:
        for widget in work_area.winfo_children():
            widget.destroy()
        images.clear()
        status = "new_film"    
        films_button['bg'] = 'lightgray'
        actors_button['bg'] = 'lightgray'
        add_film_button['bg'] = 'darkgray'
        add_actor_button['bg'] = 'lightgray'
        left_form = Frame(work_area, bg = "#505050", width = work_area.winfo_reqwidth()/2)
        left_form.pack(side = LEFT, expand=1, fill=BOTH)
        right_form = Frame(work_area, bg = "#505050", width = work_area.winfo_reqwidth()/2)
        right_form.pack(side = RIGHT, expand=1, fill=BOTH)

        name_frame = Frame(left_form)
        name = Label(name_frame, text = "Название фильма")
        name_field = Entry(name_frame)
        name.pack()
        name_field.pack()
        name_frame.pack(pady=20, padx = 50, anchor = NW)

        description_frame = Frame(right_form)
        description = Label(description_frame, text = "Описание")
        description_field = Text(description_frame, width = 50, height = 5)
        description.pack()
        description_field.pack()
        description_frame.pack(pady=20, padx = 50, anchor = NW)

        reg_frame = Frame(left_form)
        reg = Label(reg_frame, text = "Режисёр")
        reg_field = Entry(reg_frame)
        reg.pack()
        reg_field.pack()
        reg_frame.pack(pady=20, padx = 50, anchor = NW)

        year_frame = Frame(left_form)
        year = Label(year_frame, text = "Год")
        year_field = Entry(year_frame)
        year.pack()
        year_field.pack()
        year_frame.pack(pady=20, padx = 50, anchor = NW)

        genre_frame = Frame(right_form)
        genre = Label(genre_frame, text = "Жанр")
        genre_field = Listbox(genre_frame,  selectmode = MULTIPLE, height = 8)
        genre.pack()
        genre_field.pack()
        genre_frame.pack(pady=20, padx = 50, anchor = NW)
        genres = ["Боевик","Детектив", "Драма", "Историческое", "Комедия", "Криминал", "Мелодрама", "Трагикомедия", "Ужасы", "Фантастика", "Фентези" ]
        for i in range(len(genres)):
            genre_field.insert(i+1, genres[i])

        rating_frame = Frame(left_form)
        rating = Label(rating_frame, text = "Рейтинг")
        rating_field = Entry(rating_frame)
        rating.pack()
        rating_field.pack()
        rating_frame.pack(pady=20, padx = 50, anchor = NW)

        age_frame = Frame(left_form)
        age = Label(age_frame, text = "Возрастная категория")
        age_field = Entry(age_frame)
        age.pack()
        age_field.pack()
        age_frame.pack(pady=20, padx = 50, anchor = NW)

        actors_frame = Frame(right_form)
        actors = Label(actors_frame, text = "Актёры (перечислите через запятую)")
        actors_field = Text(actors_frame, width = 50, height = 5)
        actors.pack()
        actors_field.pack()
        actors_frame.pack(pady=20, padx = 50, anchor = NW)

        countries_frame = Frame(right_form)
        countries = Label(countries_frame, text = "Страны (перечислите через запятую)")
        countries_field = Text(countries_frame, width = 50, height = 5)
        countries.pack()
        countries_field.pack()
        countries_frame.pack(pady=20, padx = 50, anchor = NW)

        def apply():
            NAME = name_field.get()
            if len(NAME)==0:
                messagebox.showinfo("Ошибка", "Введите название фильма")
                return
            DESC = description_field.get("1.0", "end-1c")
            if len(DESC)==0:
                messagebox.showinfo("Ошибка", "Введите описание к фильму")
                return
            REG = reg_field.get()
            if len(REG)==0:
                messagebox.showinfo("Ошибка", "Введите имя режиссёра")
                return
            YEAR = year_field.get()
            if len(YEAR) == 0:
                messagebox.showinfo("Ошибка", "Введите год выхода фильма")
                return
            if not YEAR.isdigit():
                messagebox.showinfo("Ошибка", "Неверное значение для года")
                return
            GENRES = [genre_field.get(idx) for idx in genre_field.curselection()]
            if len(GENRES) == 0:
                messagebox.showinfo("Ошибка", "Должен быть выбран хотя бы один жанр")
                return
            RATING = rating_field.get()
            if len(RATING)==0:
                RATING = 0
            else:
                try:
                    RATING = float(RATING.replace(",", "."))
                except(ValueError):
                    messagebox.showinfo("Ошибка", "Рейтинг должен быть в диапазоне от 0 до 10")
                    return
                if RATING <0 or RATING > 10:
                    messagebox.showinfo("Ошибка", "Рейтинг должен быть в диапазоне от 0 до 10")
                    return
            AGE = age_field.get()
            if len(AGE) == 0:
                AGE = "0+"
            ACTORS = actors_field.get("1.0", "end-1c").split(", ")
            if len(ACTORS) == 0:
                messagebox.showinfo("Ошибка", "Введите хотя бы одного актёра")
                return
            COUNTRIES = countries_field.get("1.0", "end-1c").split(", ")
            if len(COUNTRIES) == 0:
                messagebox.showinfo("Ошибка", "Введите хотя бы одну страну")
                return
            full_films.append(film(NAME, REG, YEAR, description = DESC, actors = ACTORS, genre = GENRES, rating = RATING, category = AGE, country = COUNTRIES))
            messagebox.showinfo("Успех", "Фильм успешно добавлен")

        bot = Frame(work_area, bg = "#505050")
        bot.pack( anchor = S, expand=1, fill=BOTH)
        apply_button = Button(bot, text = "Добавить фильм")
        apply_button.configure(command = apply)
        apply_button.pack(pady=50, side = BOTTOM)

def new_actor():
    global status, films
    if status == "films" or status == "actors":
        scroll.pack_forget()
    films = full_films
    if status == "new_actor":
        return
    else:
        for widget in work_area.winfo_children():
            widget.destroy()
        images.clear()
        status = "new_actor"    
        films_button['bg'] = 'lightgray'
        actors_button['bg'] = 'lightgray'
        add_film_button['bg'] = 'lightgray'
        add_actor_button['bg'] = 'darkgray'

        name_frame = Frame(work_area)
        name = Label(name_frame, text = "Имя актёра")
        name_field = Entry(name_frame)
        name.pack()
        name_field.pack()
        name_frame.pack(pady=20, padx = 50, anchor = NW)

        description_frame = Frame(work_area)
        description = Label(description_frame, text = "Описание")
        description_field = Text(description_frame, width = 50, height = 5)
        description.pack()
        description_field.pack()
        description_frame.pack(pady=20, padx = 50, anchor = NW)

        films_frame = Frame(work_area)
        films = Label(films_frame, text = "Фильмография (перечислите через запятую)")
        films_field = Text(films_frame, width = 50, height = 5)
        films.pack()
        films_field.pack()
        films_frame.pack(pady=20, padx = 50, anchor = NW)

        def apply_actor():
            NAME = name_field.get()
            if len(NAME)==0:
                messagebox.showinfo("Ошибка", "Введите имя актёрв")
                return
            DESC = description_field.get("1.0", "end-1c")
            if len(DESC)==0:
                messagebox.showinfo("Ошибка", "Введите характеристику актёра")
                return
            FILMS = films_field.get("1.0", "end-1c").split(", ")
            if len(FILMS) == 0:
                messagebox.showinfo("Ошибка", "Введите хотя бы один фильм/сериал")
                return
            actors.append(actor(NAME, films = FILMS, description = DESC))
            messagebox.showinfo("Успех", "Актёр успешно добавлен")

        apply_button = Button(work_area, text = "Добавить актёра")
        apply_button.configure(command = apply_actor)
        apply_button.pack(pady=50, side = BOTTOM)


def save_data():
    import pickle
    global status
    status = "save"
    with open ("saves//films.flm", "wb") as file:
        pickle.dump(full_films, file)
    with open ("saves//actors.act", "wb") as file:
        pickle.dump(actors, file)
    messagebox.showinfo("Успех", "Данные успешно сохранены")

def load_data():
    import pickle
    global full_films, films, actors, status
    status = "load"
    try:
        with open ("saves//films.flm", "rb") as file:
            full_films = pickle.load(file)
        with open ("saves//actors.act", "rb") as file:
            actors = pickle.load(file)
    except EnvironmentError:
        messagebox.showinfo("Ошибка", "Отсутствует(ют) файл(ы) сохранения")
        return
    films = full_films
    messagebox.showinfo("Успех", "Данные успешно считаны")
        
films_button.configure(command = films_filling)
actors_button.configure(command = actors_filling)
add_film_button.configure(command = new_film)
add_actor_button.configure(command = new_actor)
save_data_button.configure(command = save_data)
load_data_button.configure(command = load_data)
films_button.pack()
actors_button.pack()
add_film_button.pack()
add_actor_button.pack()
save_data_button.pack()
load_data_button.pack()
menu.pack(side = LEFT, expand = 0, fill = Y)

work_area.pack(side=LEFT, fill=BOTH, expand=True)

window.bind('<Configure>', on_resize)

window.mainloop()
