# Repo para EIEC - DevOps - UNIR

Este repositorio incluye un proyecto sencillo para demostrar los conceptos de pruebas unitarias, pruebas de servicio o de API y pruebas E2E o de GUI. El objetivo es que el alumno entienda estos conceptos, por lo que el código y la estructura del proyecto son especialmente sencillos.

El Makefile ofrece comandos para facilitar la creación de imágenes de Docker y la ejecución de las pruebas. El único requisito es tener Docker instalado. Los comandos funcionarán en MacOS y Linux. En caso de usar Windows, será necesario adaptarlos o ejecutarlos en una máquina virtual Linux con Docker instalado.

## 1 Revision de respositorio original

### funciones existentes

- add(x, y)
- substract(x, y)
- multiply(x, y)
- divide(x, y)
- power(x, y)
- check_types(x, y)

### agregar archivos

- requirements.txt
- main.py

### Ejecute

- python3 -m venv venv
- source venv/bin/activate
- en el entorno ejecute en la carperta raiz
  - pip install -r requirements.txt
  - python main.py
  nos dio resultado * Running on http://172.27.168.62:5000
  se hizo prueba funciono

  - http://127.0.0.1:5000/
  - http://127.0.0.1:5000/calc/add/3/3

### agrego otras funcionalidades agregando la libreria math

- sqrt(x)
- log10(x)
- mod(x, y) (resto)
- abs_value(x)
- avg(numbers) (promedio)
- max_value(numbers)
- min_value(numbers)
- factorial(x)
- percent(x, y) (porcentaje de x respecto a y)
- inverse(x) (1/x)

## creacion de puebas unitarias y utilidades

- tests/unit/test_calc.py
- tests/unit/test_util.py
   
## Creacion de api rest (simulado)

- tests/rest/test_api.py
- 
### instalar pytest

- sudo apt install python-pytest

## ejecutamos prueba

pytest

- Esto creará un archivo results.xml dentro de una carpeta reports/ con el resumen de ejecución.

- Ese test usa la librería de OWASP ZAP API (una herramienta de pentesting).
  
pip install python-owasp-zap-v2.4

## instalar selenium 
pip install selenium webdriver-manager


### EJECUTAR PRUEBAS

- UNITARIAS
*** tener instaladas owas y ejecutar el entorno
-- source venv/bin/activate
-- python3 -m venv venv       ** construir entorno
-- python -m pytest -m unit -v     ** ejecutar
-- deactivate   ** salir del entorno
-- pip install -r requirements.txt   *** instalar requerimientos
-- pip install flask pytest selenium webdriver-manager  ** instalar flask
-- pip install python-owasp-zap-v2.4

***ejecutar***

-- python -m pytest -m unit -v

- pruebas de API
  
***tener otro servidor corriendo con:***

--python main.py

***en otro terminal y luego***

-- export BASE_URL="http://127.0.0.1:5000"
-- python -m pytest -m api -v


### REPORTES

- python -m pytest -m unit --junitxml=reports/unit-results.xml -v
- python -m pytest -m api --junitxml=reports/api-results.xml -v

