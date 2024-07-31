from datetime import datetime

fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('/workspaces/exercise-terminal-challenge/revisar_elisa_felix/scripts_python/test.txt', "a") as archivo:
	archivo.write(f'Tarea Finalizada a las {fecha_hora_actual}.')


print('Ejecutado')
