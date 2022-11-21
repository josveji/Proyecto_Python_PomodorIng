#!/usr/bin/python3
import threading
import customtkinter
from PIL import Image, ImageTk
import pygame
import os
import time

PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("blue")


class PomodorING(customtkinter.CTk):
  # ---------Variables globales--------------------------------
  global tiempo
  tiempo = "25:00"
  global time_text_split
  time_text_split = tiempo.split(":")
  global extraTime
  extraTime = 0

  # ---------Construccion de aplicacion------------------------
  def __init__(self):
    super().__init__()

    self.title("PomodorING")
    self.geometry("1280x720")

    # -----------------Frames principales--------------------------
    self.grid_columnconfigure(1, weight=1)
    self.grid_rowconfigure(0, weight=1)

    # ------------------------Open files---------------------------
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
    self.frame_timer = customtkinter.CTkFrame(master=self,
                                              corner_radius=15,
                                              fg_color="#FFFFFF")
    self.frame_timer.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
    # configurando columnas timer
    self.frame_timer.columnconfigure((0, 1, 2, 3, 4), weight=1)

    # configurando filas timer
    self.frame_timer.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

    # ---------------Frames Secundarios---------------------------
    # ========frame interior de to-do list======
    self.frame_to_do_container = customtkinter.CTkFrame(
      master=self.frame_tasks, corner_radius=15)

    self.frame_to_do_container.grid(row=1,
                                    column=0,
                                    ipady=10,
                                    rowspan=6,
                                    padx=20,
                                    sticky="nsew")

    # configurando columnas to-do list container
    self.frame_to_do_container.columnconfigure((0, 1, 2), weight=1)
    # configurando filas to-do list container
    self.frame_to_do_container.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    # ========frame interior para musica========
    self.frame_music = customtkinter.CTkFrame(master=self.frame_tasks,
                                              width=368,
                                              height=100,
                                              corner_radius=15)
    self.frame_music.grid(row=7, column=0, rowspan=2, padx=20)
    # configurando columnas musica
    self.frame_music.columnconfigure((0, 1), weight=1)
    # configurando filas musica
    self.frame_music.rowconfigure((0, 1), weight=1)

    # ===frame interior para botones start y repeat dentro de timer frame==
    self.frame_repstart = customtkinter.CTkFrame(master=self.frame_timer,
                                                 fg_color="#FFFFFF")
    self.frame_repstart.grid(row=4, column=2, sticky="N")
    # configurando columnas repstart buttons
    self.frame_repstart.columnconfigure((0, 1), weight=1)
    # configurando columnas repstart buttons
    self.frame_repstart.rowconfigure(0, weight=1)

    # ==========frame timer and +- 5==========
    self.frame_timer_5 = customtkinter.CTkFrame(master=self.frame_timer,
                                                fg_color="#FFFFFF")
    self.frame_timer_5.grid(row=3, column=2, sticky="S")
    # configurando columnas repstart buttons
    self.frame_timer_5.columnconfigure((0, 1, 2), weight=1)
    # configurando columnas repstart buttons
    self.frame_timer_5.rowconfigure(0, weight=1)

    # =========name update====================
    self.frame_upname = customtkinter.CTkFrame(master=self.frame_timer,
                                               fg_color="#FFFFFF")
    self.frame_upname.grid(row=5, column=2, sticky="S")
    # configurando columnas repstart buttons
    self.frame_upname.columnconfigure((0, 1, 2), weight=1)
    # configurando columnas repstart buttons
    self.frame_upname.rowconfigure(0, weight=1)

    # -------------Widgets-----------------------------
    # ==========To-do list====================
    # to-do list label
    self.label_tasks = customtkinter.CTkLabel(master=self.frame_tasks,
                                              text="TO-DO LIST",
                                              text_font=("pomodoring_font",
                                                         40))
    self.label_tasks.grid(row=0, column=0, padx=80)
    # to-do list entrys
    self.entry_task_1 = customtkinter.CTkEntry(
      master=self.frame_to_do_container,
      width=330,
      placeholder_text="...",
      text_font=("pomodoring_font", 15),
      border_width=0,
      corner_radius=15)
    self.entry_task_1.grid(row=1,
                           column=0,
                           columnspan=2,
                           pady=5,
                           padx=20,
                           sticky="W")

    self.entry_task_2 = customtkinter.CTkEntry(
      master=self.frame_to_do_container,
      width=330,
      placeholder_text="...",
      text_font=("pomodoring_font", 15),
      border_width=0,
      corner_radius=15)
    self.entry_task_2.grid(row=2,
                           column=0,
                           columnspan=2,
                           pady=5,
                           padx=20,
                           sticky="W")

    self.entry_task_3 = customtkinter.CTkEntry(
      master=self.frame_to_do_container,
      width=330,
      placeholder_text="...",
      text_font=("pomodoring_font", 15),
      border_width=0,
      corner_radius=15)
    self.entry_task_3.grid(row=3,
                           column=0,
                           columnspan=2,
                           pady=5,
                           padx=20,
                           sticky="W")

    self.entry_task_4 = customtkinter.CTkEntry(
      master=self.frame_to_do_container,
      width=330,
      placeholder_text="...",
      text_font=("pomodoring_font", 15),
      border_width=0,
      corner_radius=15)
    self.entry_task_4.grid(row=4,
                           column=0,
                           columnspan=2,
                           pady=5,
                           padx=20,
                           sticky="W")

    self.entry_task_5 = customtkinter.CTkEntry(
      master=self.frame_to_do_container,
      width=330,
      placeholder_text="...",
      text_font=("pomodoring_font", 15),
      border_width=0,
      corner_radius=15)
    self.entry_task_5.grid(row=5,
                           column=0,
                           columnspan=2,
                           pady=5,
                           padx=20,
                           sticky="W")

    self.entry_task_6 = customtkinter.CTkEntry(
      master=self.frame_to_do_container,
      width=330,
      placeholder_text="...",
      text_font=("pomodoring_font", 15),
      border_width=0,
      corner_radius=15)
    self.entry_task_6.grid(row=6,
                           column=0,
                           columnspan=2,
                           pady=5,
                           padx=20,
                           sticky="W")

    # to-do list checkbox
    self.check_box_1 = customtkinter.CTkCheckBox(
      master=self.frame_to_do_container,
      text="",
      corner_radius=15,
      border_width=2,
      fg_color="#53da1c",
      border_color="#939ba2",
      command=self.progressbar_increase)
    self.check_box_1.grid(row=1, column=2, sticky="W")

    self.check_box_2 = customtkinter.CTkCheckBox(
      master=self.frame_to_do_container,
      text="",
      corner_radius=15,
      border_width=2,
      fg_color="#53da1c",
      border_color="#939ba2",
      command=self.progressbar_increase)
    self.check_box_2.grid(row=2, column=2, sticky="W")

    self.check_box_3 = customtkinter.CTkCheckBox(
      master=self.frame_to_do_container,
      text="",
      corner_radius=15,
      border_width=2,
      fg_color="#53da1c",
      border_color="#939ba2",
      command=self.progressbar_increase)
    self.check_box_3.grid(row=3, column=2, sticky="W")

    self.check_box_4 = customtkinter.CTkCheckBox(
      master=self.frame_to_do_container,
      text="",
      corner_radius=15,
      border_width=2,
      fg_color="#53da1c",
      border_color="#939ba2",
      command=self.progressbar_increase)
    self.check_box_4.grid(row=4, column=2, sticky="W")

    self.check_box_5 = customtkinter.CTkCheckBox(
      master=self.frame_to_do_container,
      text="",
      corner_radius=15,
      border_width=2,
      fg_color="#53da1c",
      border_color="#939ba2",
      command=self.progressbar_increase)
    self.check_box_5.grid(row=5, column=2, sticky="W")

    self.check_box_6 = customtkinter.CTkCheckBox(
      master=self.frame_to_do_container,
      text="",
      corner_radius=15,
      border_width=2,
      fg_color="#53da1c",
      border_color="#939ba2",
      command=self.progressbar_increase)

    self.check_box_6.grid(row=6, column=2, sticky="W")

    # status bar tasks

    self.progressbar = customtkinter.CTkProgressBar(
      master=self.frame_to_do_container,
      width=330,
      height=30,
      progress_color="#53da1c")
    self.progressbar.grid(row=0, column=0, columnspan=3, padx=20, sticky="SW")
    self.progressbar.set(0)

    # =========Timer===================
    # welcomeback label
    self.welcome_label = customtkinter.CTkLabel(master=self.frame_timer,
                                                text=("WELCOMEBACK USERNAME!"),
                                                text_font=("pomodoring_font",
                                                           20))
    self.welcome_label.grid(row=0, column=1, columnspan=3, padx=1, pady=10)

    # label tiempo
    self.time_label = customtkinter.CTkLabel(master=self.frame_timer_5,
                                             text=tiempo,
                                             text_font=("pomodoring_font", 70))
    self.time_label.grid(row=0, column=1, padx=1, sticky="S")

    # label Pomo property
    self.pomo_pet_label = customtkinter.CTkLabel(master=self.frame_timer,
                                                 image=self.pomopet_image
                                                 )
    self.pomo_pet_label.grid(row=2, column=2, padx=1, sticky="S")

    # ----------------Timer buttons---------------

    # reset button
    self.button_reset = customtkinter.CTkButton(
      master=self.frame_repstart,
      width=5,
      height=5,
      border_width=0,
      corner_radius=8,
      image=self.reset_image,
      text="",
      text_font=("pomodoring_font", 50),
      fg_color="#FFFFFF",
      command=self.reset)
    self.button_reset.grid(row=0,
                           column=1,
                           columnspan=1,
                           pady=1,
                           padx=5,
                           sticky="NE")

    # start button
    self.button_start = customtkinter.CTkButton(
      master=self.frame_repstart,
      width=5,
      height=5,
      border_width=0,
      corner_radius=8,
      image=self.start_image,
      text="",
      text_font=("pomodoring_font", 50),
      fg_color="#FFFFFF",
      command=self.start)
    self.button_start.grid(row=0,
                           column=0,
                           columnspan=1,
                           pady=1,
                           padx=5,
                           sticky="NW")

    self.button_moremin = customtkinter.CTkButton(
      master=self.frame_timer_5,
      width=5,
      height=5,
      border_width=0,
      corner_radius=8,
      image=self.moremin_image,
      text="",
      text_font=("pomodoring_font", 50),
      fg_color="#FFFFFF",
      command=self.more_minutes)
    self.button_moremin.grid(row=0, column=2, pady=20, sticky="SW")

    self.button_lessmin = customtkinter.CTkButton(
      master=self.frame_timer_5,
      width=5,
      height=5,
      border_width=0,
      corner_radius=8,
      image=self.lessmin_image,
      text="",
      text_font=("pomodoring_font", 50),
      fg_color="#FFFFFF",
      command=self.less_minutes)
    self.button_lessmin.grid(row=0, column=0, pady=20, sticky="SE")

    self.entry_name = customtkinter.CTkEntry(master=self.frame_upname,
                                             width=280,
                                             justify="center",
                                             placeholder_text="WHAT IS YOU"
                                             "R NAME?",
                                             text_font=("pomodoring_font", 15),
                                             border_width=0,
                                             corner_radius=15,
                                             fg_color="#c0c2c5")
    self.entry_name.grid(row=0, column=0, columnspan=1, pady=15, sticky="S")

    self.update_name = customtkinter.CTkButton(master=self.frame_upname,
                                               width=50,
                                               text="SAVE",
                                               text_font=("pomodoring_font",
                                                          13),
                                               border_width=0,
                                               corner_radius=15,
                                               fg_color="#c0c2c5",
                                               command=self.save_name)
    self.update_name.grid(row=0,
                          column=1,
                          columnspan=1,
                          pady=15,
                          padx=10,
                          sticky="S")

    self.update_wlabel = customtkinter.CTkButton(master=self.frame_upname,
                                                 width=50,
                                                 text="APPLY",
                                                 text_font=("pomodoring_font",
                                                            13),
                                                 border_width=0,
                                                 corner_radius=15,
                                                 fg_color="#c0c2c5",
                                                 command=self.read_name)
    self.update_wlabel.grid(row=0,
                            column=2,
                            columnspan=1,
                            pady=15,
                            padx=1,
                            sticky="S")

    # =========Reproductor de musica===========
    # nombre de la cancion
    self.music_name_label = customtkinter.CTkLabel(
      master=self.frame_music,
      text="NOW YOU ARE LISTE"
      "NING TO LO-FI MUSIC",
      text_font=("pomodoring_font", 15))
    self.music_name_label.grid(row=0,
                               column=0,
                               columnspan=2,
                               ipady=10,
                               padx=50,
                               pady=1,
                               sticky="S")

    # botones reproductor de musica
    self.button_play = customtkinter.CTkButton(
      master=self.frame_music,
      width=5,
      height=5,
      border_width=0,
      corner_radius=8,
      image=self.resume_image,
      text="",
      text_font=("pomodoring_font", 35),
      fg_color="#d1d5d8",
      command=self.play_music)
    self.button_play.grid(row=1, column=0, padx=10, pady=10, sticky="NE")

    self.button_stop_song = customtkinter.CTkButton(
      master=self.frame_music,
      width=5,
      height=5,
      border_width=0,
      corner_radius=8,
      image=self.pause_image,
      text="",
      text_font=("pomodoring_font", 35),
      fg_color="#d1d5d8",
      command=self.stop_music)
    self.button_stop_song.grid(row=1, column=1, pady=10, sticky="NW")

    # conditions for Timer
    self.condicion = False
    self.contadorOneTimer = 0
    self.otroContador = 0
    self.positivo = 10
    self.time_text_split = tiempo.split(":")
    self.min = int(self.time_text_split[0])
    self.sec = int(self.time_text_split[1])


# ---------------Functions------------------------

  def start_timer(self):
    run_time = threading.Thread(target=self.start)
    run_time.start()

  # progress bar linked to checkbox
  def progressbar_increase(self):
    value = self.progressbar.get()
    value = value + 0.16666666667
    self.progressbar.set(value)

  # load rectangular image with path relative to PATH
  def load_image(self, path, image_size):
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size,
                                  image_size)))

  # path relative to PATH
  def complete_path(self, path):
    return (PATH + path)

  # save name in external file
  def save_name(self):
    # write txt

    savename_w = open(self.complete_path("/savename.txt"), "w")
    name = self.entry_name.get()
    name = str(name.upper())
    print(name)
    savename_w.write(name)
    savename_w.close()

  # read username in external file
  def read_name(self):
    savename_r = open(self.complete_path("/savename.txt"), "r")
    newname = savename_r.readline()
    print(newname)
    self.welcome_label.configure(text=("WELCOMEBACK {}!".format(newname)))
    self.welcome_label.update()

  # update welcome username label
  def show_name(self):
    readname = self.savename_r.readline()
    return readname
    self.welcome_label.update()

  # start timer button
  def start(self):
    self.contadorOneTimer = self.contadorOneTimer + 1
    self.condicion = True
    if self.condicion == True:
      self.reset_timer = False

      global min
      global sec
      min = int(time_text_split[0])
      sec = int(time_text_split[1])

      global full_sec
      full_sec = 60 * (min)

      if self.contadorOneTimer == 1:
        while full_sec > 0 and self.condicion == True:
          full_sec -= 1
          min, sec = divmod(full_sec, 60)

          self.time_label.config(text=f"{min + extraTime}:{sec}")
          self.update()
          time.sleep(1)

  # Stop Timer
  def reset(self):

    self.reset_timer = True
    self.condicion = False
    self.time_label.config(text=time_text_split)
    self.contadorOneTimer = 0
    global extraTime
    extraTime = 0
    self.positivo = 10

  # less minutes
  def less_minutes(self):

    if self.condicion == False and self.positivo > 10:

      min = int(time_text_split[0])
      global extraTime
      extraTime = extraTime - 5
      sec = int(time_text_split[1])
      self.time_label.config(text=f"{min+extraTime}:{sec}")
      self.positivo = self.positivo - 1
      self.update()

  # more minutes
  def more_minutes(self):

    if self.condicion == False:

      min = int(time_text_split[0])
      global extraTime
      extraTime = extraTime + 5
      sec = int(time_text_split[1])
      self.time_label.config(text=f"{min+extraTime}:{sec}")
      global positivo
      self.positivo = self.positivo + 1
      self.update()

  # play music
  def play_music(self):
    pygame.init()

    pygame.mixer.music.load(
      self.complete_path("/OnBourbonStreet"
                         "_GiorigioDiCampo.mp3"))
    pygame.mixer.music.play(10)
    return

  # stop music
  def stop_music(self):
    pygame.mixer.music.load(
      self.complete_path("/OnBourbonStreet"
                         "_GiorigioDiCampo.mp3"))
    pygame.mixer.music.stop()

if __name__ == "__main__":
  app = PomodorING()
  app.mainloop()
