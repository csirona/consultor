#!/bin/bash
export DISPLAY=:0
sleep 20  # Asegúrate de que haya suficiente tiempo para que el entorno gráfico esté listo
/usr/bin/chromium-browser --kiosk http://0.0.0.0:8080
