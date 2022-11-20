#!/usr/bin/python3

import tkinter
import customtkinter
from PIL import Image, ImageTk
import os

PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("blue")

class PomodorING(customtkinter.CTk):
# ---------Variables globales---------------------------------
    global tiempo
    tiempo = "25:00"
    global time_text_split
    global extra
    extra = 0

# ---------Construccion de aplicacion------------------------
    def __init__(self):
        super().__init__()

        self.title("PomodorING")
        self.geometry("1280x720")

# -----------------Frames principales--------------------------
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

# -------------Abrir archivos externos-------------------------------

        self.start_image = self.load_image("/app_buttons/start.png", 50)
        self.reset_image = self.load_image("/app_buttons/reset.png", 50)
        self.moremin_image = self.load_image("/app_buttons/moremin.png", 50)
        self.lessmin_image = self.load_image("/app_buttons/lessmin.png", 50)
        self.pause_image = self.load_image("/app_buttons/pause.png", 50)
        self.resume_image = self.load_image("/app_buttons/start_music.png", 50)
        self.pomopet_image = self.load_image("/app_buttons/pomo_pet.jpg", 400)

        # =========tasks frame configuracion================
        self.frame_tasks = customtkinter.CTkFrame(master=self,
                                                 width=448,
                                                 corner_radius=0,
                                                 fg_color="#FFFFFF")
        self.frame_tasks.grid(row=0, column=0, sticky="nswe")
        # configurando columnas tasks
        self.frame_tasks.columnconfigure(0, weight=1)

        # configurando filas tasks
        self.frame_tasks.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)

        # =========Timer frame configuracion==================
        self.frame_timer = customtkinter.CTkFrame(master=self, corner_radius=15,
                                                  fg_color="#FFFFFF")
        self.frame_timer.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        # configurando columnas timer
        self.frame_timer.columnconfigure((0, 1, 2, 3, 4), weight=1)

        # configurando filas timer
        self.frame_timer.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

# ---------------Frames Secundarios---------------------------
        # ========frame interior de to-do list======
        self.frame_to_do_container = customtkinter.CTkFrame(master=self.frame_tasks,
                                                            corner_radius=15)

        self.frame_to_do_container.grid(row=1, column=0, ipady=10, rowspan=6, padx=20, sticky="nsew")

        # configurando columnas to-do list container
        self.frame_to_do_container.columnconfigure((0, 1, 2), weight=1)
        # configurando filas to-do list container
        self.frame_to_do_container.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)


        # ========frame interior para musica========
        self.frame_music = customtkinter.CTkFrame(master=self.frame_tasks, width=368,
                                                  height=100, corner_radius=15)
        self.frame_music.grid(row=7, column=0, rowspan=2, padx=20)
        # configurando columnas musica
        self.frame_music.columnconfigure((0, 1), weight=1)
        # configurando filas musica
        self.frame_music.rowconfigure((0, 1), weight=1)

        # ===frame interior para botones start y repeat dentro de timer frame===
        self.frame_repstart = customtkinter.CTkFrame(master=self.frame_timer, fg_color="#FFFFFF")
        self.frame_repstart.grid(row=4, column=2, sticky="N")
        # configurando columnas repstart buttons
        self.frame_repstart.columnconfigure((0, 1), weight=1)
        # configurando columnas repstart buttons
        self.frame_repstart.rowconfigure(0, weight=1)

        # ==========frame timer and +- 5==========
        self.frame_timer_5 = customtkinter.CTkFrame(master=self.frame_timer, fg_color="#FFFFFF")
        self.frame_timer_5.grid(row=3, column=2, sticky="S")
        # configurando columnas repstart buttons
        self.frame_timer_5.columnconfigure((0, 1, 2), weight=1)
        # configurando columnas repstart buttons
        self.frame_timer_5.rowconfigure(0, weight=1)



# -------------Widgets-----------------------------
        # ==========To-do list====================
        # to-do list label
        self.label_tasks = customtkinter.CTkLabel(master=self.frame_tasks,
                                              text="TO-DO LIST",
                                              text_font=("pomodoring_font", 40))
        self.label_tasks.grid(row=0, column=0, padx=80)
        # to-do list entrys
        self.entry_task_1 = customtkinter.CTkEntry(master=self.frame_to_do_container,
                                            width=330,
                                            placeholder_text="...",
                                            text_font=("pomodoring_font", 15),
                                            border_width=0,
                                            corner_radius=15)
        self.entry_task_1.grid(row=1, column=0, columnspan=2, pady=5, padx=20, sticky="W")

        self.entry_task_2 = customtkinter.CTkEntry(master=self.frame_to_do_container,
                                            width=330,
                                            placeholder_text="...",
                                            text_font=("pomodoring_font", 15),
                                            border_width=0,
                                            corner_radius=15)
        self.entry_task_2.grid(row=2, column=0, columnspan=2, pady=5, padx=20, sticky="W")

        self.entry_task_3 = customtkinter.CTkEntry(master=self.frame_to_do_container,
                                            width=330,
                                            placeholder_text="...",
                                            text_font=("pomodoring_font", 15),
                                            border_width=0,
                                            corner_radius=15)
        self.entry_task_3.grid(row=3, column=0, columnspan=2, pady=5, padx=20, sticky="W")

        self.entry_task_4 = customtkinter.CTkEntry(master=self.frame_to_do_container,
                                            width=330,
                                            placeholder_text="...",
                                            text_font=("pomodoring_font", 15),
                                            border_width=0,
                                            corner_radius=15)
        self.entry_task_4.grid(row=4, column=0, columnspan=2, pady=5, padx=20, sticky="W")

        self.entry_task_5 = customtkinter.CTkEntry(master=self.frame_to_do_container,
                                            width=330,
                                            placeholder_text="...",
                                            text_font=("pomodoring_font", 15),
                                            border_width=0,
                                            corner_radius=15)
        self.entry_task_5.grid(row=5, column=0, columnspan=2, pady=5, padx=20, sticky="W")

        self.entry_task_6 = customtkinter.CTkEntry(master=self.frame_to_do_container,
                                            width=330,
                                            placeholder_text="...",
                                            text_font=("pomodoring_font", 15),
                                            border_width=0,
                                            corner_radius=15)
        self.entry_task_6.grid(row=6, column=0, columnspan=2, pady=5, padx=20, sticky="W")

        # to-do list checkbox
        self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_to_do_container,
                                                     text="",corner_radius=15,
                                                     border_width=2,
                                                     fg_color="#53da1c",
                                                     command=self.progressbar_increase)
        self.check_box_1.grid(row=1, column=2, sticky="W")

        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_to_do_container,
                                                     text="",corner_radius=15,
                                                     border_width=2,
                                                     fg_color="#53da1c",
                                                     command=self.progressbar_increase)
        self.check_box_2.grid(row=2, column=2, sticky="W")

        self.check_box_3 = customtkinter.CTkCheckBox(master=self.frame_to_do_container,
                                                     text="",corner_radius=15,
                                                     border_width=2,
                                                     fg_color="#53da1c",
                                                     command=self.progressbar_increase)
        self.check_box_3.grid(row=3, column=2, sticky="W")

        self.check_box_4 = customtkinter.CTkCheckBox(master=self.frame_to_do_container,
                                                     text="",corner_radius=15,
                                                     border_width=2,
                                                     fg_color="#53da1c",
                                                     command=self.progressbar_increase)
        self.check_box_4.grid(row=4, column=2, sticky="W")

        self.check_box_5 = customtkinter.CTkCheckBox(master=self.frame_to_do_container,
                                                     text="",corner_radius=15,
                                                     border_width=2,
                                                     fg_color="#53da1c",
                                                     command=self.progressbar_increase)
        self.check_box_5.grid(row=5, column=2, sticky="W")

        self.check_box_6 = customtkinter.CTkCheckBox(master=self.frame_to_do_container,
                                                     text="",corner_radius=15,
                                                     border_width=2,
                                                     fg_color="#53da1c",
                                                     command=self.progressbar_increase)

        self.check_box_6.grid(row=6, column=2, sticky="W")

        # status bar tasks

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_to_do_container,
                                                   width=330, height=30,
                                                   progress_color="#53da1c")
        self.progressbar.grid(row=0, column=0, columnspan=3, padx=20, sticky="SW")
        self.progressbar.set(0)

        # =========Temporizador===================
        # welcomeback label
        self.welcome_label = customtkinter.CTkLabel(master=self.frame_timer,
                                                 text="WELCOMEBACK USERNAME!",
                                                 text_font=("pomodoring_font", 20))
        self.welcome_label.grid(row=0, column=1, columnspan=3, padx=1, pady=10)

        # label tiempo
        self.time_label = customtkinter.CTkLabel(master=self.frame_timer_5,
                                                 text=tiempo,
                                                 text_font=("pomodoring_font", 70))
        self.time_label.grid(row=0, column=1, padx=1, sticky="S")

        # label Pomo property
        self.pomo_pet_label = customtkinter.CTkLabel(master=self.frame_timer,
                                                     image=self.pomopet_image)
        self.pomo_pet_label.grid(row=2, column=2, padx=1, sticky="S")

        # botones de temporizador

        self.button_reset = customtkinter.CTkButton(master=self.frame_repstart,
                                                    width=5,
                                                    height=5,
                                                    border_width=0,
                                                    corner_radius=8,
                                                    image=self.reset_image,
                                                    text="",
                                                    text_font=("pomodoring_font", 50),
                                                    fg_color="#FFFFFF")
        self.button_reset.grid(row=0, column=1, columnspan=1, pady=1,padx=5, sticky="NE")

        self.button_start = customtkinter.CTkButton(master=self.frame_repstart,
                                                    width=5,
                                                    height=5,
                                                    border_width=0,
                                                    corner_radius=8,
                                                    image=self.start_image,
                                                    text="",
                                                    text_font=("pomodoring_font", 50),
                                                    fg_color="#FFFFFF")
        self.button_start.grid(row=0, column=0, columnspan=1, pady=1, padx=5, sticky="NW")

        self.button_moremin = customtkinter.CTkButton(master=self.frame_timer_5,
                                                    width=5,
                                                    height=5,
                                                    border_width=0,
                                                    corner_radius=8,
                                                    image=self.moremin_image,
                                                    text="",
                                                    text_font=("pomodoring_font", 50),
                                                    fg_color="#FFFFFF")
        self.button_moremin.grid(row=0, column=2, pady=20, sticky="SW")

        self.button_lessmin = customtkinter.CTkButton(master=self.frame_timer_5,
                                                    width=5,
                                                    height=5,
                                                    border_width=0,
                                                    corner_radius=8,
                                                    image=self.lessmin_image,
                                                    text="",
                                                    text_font=("pomodoring_font", 50),
                                                    fg_color="#FFFFFF")
        self.button_lessmin.grid(row=0, column=0, pady=20, sticky="SE")

        self.entry_name = customtkinter.CTkEntry(master=self.frame_timer,
                                                 width=330,
                                                 placeholder_text="WHAT IS YOUR NAME?",
                                                 text_font=("pomodoring_font", 15),
                                                 border_width=0,
                                                 corner_radius=15,
                                                 fg_color="#c0c2c5")
        self.entry_name.grid(row=5, column=1, columnspan=3, pady=15, sticky="S")

        # =========Reproductor de musica===========
        # nombre de la cancion
        self.music_name_label = customtkinter.CTkLabel(master=self.frame_music,
                                                 text="NOW YOU ARE LISTENING TO LO-FI MUSIC",
                                                 text_font=("pomodoring_font", 15))
        self.music_name_label.grid(row=0, column=0, columnspan=2, ipady=10, padx=50, pady=1, sticky="S") # sticky="S")

        # botones reproductor de musica
        self.button_play = customtkinter.CTkButton(master=self.frame_music,
                                                    width=5,
                                                    height=5,
                                                    border_width=0,
                                                    corner_radius=8,
                                                    image=self.resume_image,
                                                    text="",
                                                    text_font=("pomodoring_font", 35),
                                                    fg_color="#d1d5d8")
        self.button_play.grid(row=1, column=0, padx=10, pady=10, sticky="NE")

        self.button_last_song = customtkinter.CTkButton(master=self.frame_music,
                                                    width=5,
                                                    height=5,
                                                    border_width=0,
                                                    corner_radius=8,
                                                    image=self.pause_image,
                                                    text="",
                                                    text_font=("pomodoring_font", 35),
                                                    fg_color="#d1d5d8")
        self.button_last_song.grid(row=1, column=1, pady=10, sticky="NW")
 # ---------------Funciones------------------------
    def progressbar_increase(self):
        value = self.progressbar.get()
        value = value + 0.16666666667
        self.progressbar.set(value)

    def load_image(self, path, image_size):
       """ load rectangular image with path relative to PATH """
       return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))

if __name__ == "__main__":
    app = PomodorING()
    app.mainloop()
