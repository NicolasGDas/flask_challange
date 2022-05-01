# flask_challange
Cuando se clona o se copia el las carpetas deberian instalar los requerimientos
```
pip instal -r requirements.txt
```

una vez instalado correr 
```
$env:FLASK_APP = "src"       
$env:FLASK_ENV = "development"
```
luego en teoria tendrias que poder usar flask run para correr el servidor


Los endpoint son 
1- localhost:5000/api/cargar_registro metodo POST
2-localhost:5000/api/balance_empresa_usuario  metodo GET
3-localhost:5000/api/balance_empresa metodo GET

Para cargar registro desde postman usar en el body form-data con las variables 
  -idEmpresa
  -idUsuario
  -cantHA
 si no se ingresa alguna de las key tira error, si no pones valores tambien, te infroma que variable te falta o que valor falta.
 
Para balance_empresa_usuario se debe ingresar por params idUsuario e idEmpresa.
 
Para balance_empresa se debe ingresar por params idEmpresa.

Tema base de datos. Esta conectado, tiene los modelos y tiene un init, no se como funciona, supuestamente funciona pero yo hice todo el manejo inicial de db de crear tablas y todo por mysql workbench. Dentro de la carpeta DB tengo copiado el; DDL para crear las 3 tablas con sus propiedades
