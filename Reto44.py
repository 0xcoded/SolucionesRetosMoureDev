from datetime import datetime
import pytz, os
from time import sleep

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def change_utc(fecha):
    timezone = pytz.timezone("Europe/Madrid")
    fecha_local = timezone.localize(fecha, is_dst=None)
    fecha_utc = fecha_local.astimezone(pytz.utc)
    return fecha_utc

start_month = input("Introduce el mes: ")
start_day = input("Introduce el día: ")
start_hour = input("Introduce la hora: ")
start_minute = input("Introduce el minuto: ")
start_second = input("Introduce el segundo: ")

while True:
    project_date = change_utc(datetime.strptime(f"2024-{start_month}-{start_day} {start_hour}:{start_minute}:{start_second}", "%Y-%m-%d %H:%M:%S"))
    now_date = change_utc(datetime.now())
    if(project_date <= now_date):
        print("¡MoureDev.pro lanzado!")
        exit(0)
    print(f"Faltan {project_date.day - now_date.day} días {project_date.hour - now_date.hour} horas, {59 - now_date.minute - project_date.minute} minutos y {59 - now_date.second - project_date.second} segundos")

    sleep(1)
    clear()
