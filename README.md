# Integrantes
Abel Santiago Gómez López
Miguel Ángel Pérez Clavijo

# Endpoints 
## Ingresos
GET	/incomes --> Obtener todos los ingresos
GET	/incomes/{id} --> Obtener un ingreso por su id
POST /incomes --> Crear un ingreso
DELETE /incomes/{id} --> Eliminar un ingreso

## Egresos
GET	/egress --> Obtener todos los egresos
GET	/egress/{id} --> Obtener un egreso por su id
POST /egress --> Crear un egreso
DELETE /egress/{id} --> Eliminar un egreso

## Categorías
GET	/categories --> Obtener todas las categorías
POST /categories --> Crear una categoría
DELETE /categories/{id} --> Eliminar una categoría

##  Reportes
GET	/basic_report	Obtener un reporte básico (ingresos, egresos, dinero actual)
GET	/expanded_report	Obtener ingresos y egresos por categorías