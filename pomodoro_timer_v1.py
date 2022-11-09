import threading 
import time 
import tkinter as tk 

class Temporizador: 
    global tiempo 
    tiempo = "25:00"

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("420x150")
        self.root.title("PomodorING prueba")

        self.time_label = tk.Label(self.root, font=("Arial", 30), text=tiempo)
        self.time_label.grid(row=0, column=2, columnspan=2)
        
        self.lessmin = tk.Button(self.root, font=("Arial", 30), text="-5", command=self.less_minutes)
        self.lessmin.grid(row=1, column=1)

        self.start_button = tk.Button(self.root, font=("Arial", 30), text="Start", command=self.start_timer)
        self.start_button.grid(row=1, column=2)

        self.reset_button = tk.Button(self.root, font=("Arial", 30), text="Reset", command=self.reset)
        self.reset_button.grid(row=1, column=3)

        self.moremin_button = tk.Button(self.root, font=("Arial", 30), text="+5", command=self.more_minutes)
        self.moremin_button.grid(row=1, column=4)

        self.reset_timer = False
        
        self.root.mainloop()
    
    def start_timer(self):
        run_time = threading.Thread(target=self.start)
        run_time.start()

    def start(self): #Revisar porque si se pulsa de nuevo el botón no se pausa. Se se apreta se bugea y combina varios temporizadores
                     #de cantidad equivalente a la que uno haya apretado el botón
        self.reset_timer = False
        time_text_split = tiempo.split(":")
        min = int(time_text_split[0])
        sec = int(time_text_split[1])
        
        full_sec = 60 * min
        
        while full_sec > 0:
            full_sec -= 1
            min, sec = divmod(full_sec, 60)
            
            self.time_label.config(text=f"{min}:{sec}")
            self.root.update()
            time.sleep(1)
                          

    def reset(self): #Revisar, porque si se apreta el botón de reiniciar se reincia por un segundo y vuelve al tiempo anterior 
        self.reset_timer = True
        self.time_label.config(text=tiempo)

    def less_minutes(self): #Hacer esta función 
        pass

    def more_minutes(self): #Hacer esta función
        pass

Temporizador()