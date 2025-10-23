# Parte_03

## Uso de Recursos de Sistema en Linux

### 

> **~$** top
##### _Ver procesos y uso de CPU en tiempo real_

> **~$** top -u usuario
##### _Ver procesos y uso de CPU en tiempo real filtrado por usuario_

> **~$** top -d 2
##### _Ver procesos y uso de CPU en tiempo real cada 2 segundos_

> **~$** htop
##### _Monitor de recursos mas moderno._

Ejercicio:

Detener un contador por medio del comando kill
```bash
#!/bin/bash
```bash
for i in {1..1000}
do
    echo "$i
    sleep 0.1
done
```
[Bucles en Bash](https://atareao.es/tutorial/scripts-en-bash/bucles-en-bash/)


> **~$** mpstat 2 5 
##### _Ver estadísticas de todas las CPUs cada 2 segundos, 5 iteraciones_

> **~$** mpstat -P ALL 1 3
##### _Ver porcentaje de uso por CPU_

> **~$** iostat -dx 2 5 
##### _E/S de Disco_
```bash
# %util: Porcentaje de utilización
# r/s w/s: Lecturas/escrituras por segundo
# rkB/s wkB/s: KB leídos/escritos por segundo
# await: Tiempo promedio de E/S
```
```bash
# Información del sistema en /proc
cat /proc/cpuinfo     # Información de CPU
cat /proc/meminfo     # Información detallada de memoria
cat /proc/loadavg     # Promedio de carga del sistema
cat /proc/diskstats   # Estadísticas de 
```

Acerca de la RED:

```bash
# Ver interfaces de red
ifconfig
# ademas tenenos otro...
ip addr show
# e
ip a
# con estadísticas específicas
ip -s link show eth0
```