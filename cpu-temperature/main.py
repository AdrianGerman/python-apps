import tkinter as tk
import psutil


def get_temperature():
    sensors = psutil.sensors_temperatures()
    if 'k10temp' in sensors:
        # Obtenemos la primera lectura de 'k10temp'
        return sensors['k10temp'][0].current
    return None


def update_temperature():
    temp = get_temperature()
    if temp is not None:
        label.config(text=f'Temperatura: {temp:.2f}°C')
    else:
        label.config(text='Temperatura: N/A')
    root.after(1000, update_temperature)  # Actualiza cada segundo


root = tk.Tk()
root.title('Monitoreo de temperatura del CPU')

label = tk.Label(root, text="Temperatura: N/A", font=('Fira code', 16))
label.pack(pady=20)

update_temperature()  # Llamada inicial

root.mainloop()
