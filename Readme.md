# Proyecto Urban Routes
Proyecto de pruebas automatizadas para la aplicación **Urban Routes** utilizando el método Page Object Model (POM) con `pytest` y `selenium`.

---

## 📋 Contenido

- [Descripción](#descripción)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Lista de Comprobación](#lista-de-comprobación)
- [Recursos](#recursos)
- [Instrucciones de Uso](#instrucciones-de-uso)

---

## 📌 Descripción

Este proyecto tiene como objetivo automatizar el flujo de uso de la app **Urban Routes**, validando su comportamiento en distintas etapas mediante pruebas automatizadas con el enfoque **POM** (Page Object Model).

---

## 📁 Estructura del Proyecto

- `data.py`: Contiene la URL y los cuerpos necesarios para las solicitudes.
- `utilidades.py`: Función para obtener el código de confirmación del teléfono.
- `selector.py`: Selectores de la app y funciones relacionadas.
- `main.py`: Contiene funciones principales y una clase con todas las pruebas.
- `README.md`: Este archivo que estás leyendo 😊
- `.gitignore`: Archivos que no deben incluirse en el repositorio.

---

## ✅ Lista de Comprobación

1. ✅ Configurar la dirección.
2. ✅ Seleccionar la tarifa **Comfort**.
3. ✅ Rellenar el número de teléfono.
4. ✅ Agregar una tarjeta de crédito.
5. ⚠️ Escribir un mensaje para el conductor *(máx. 24 caracteres, pero es opcional)*.
6. ✅ Pedir una manta y pañuelos.
7. ✅ Pedir 2 helados 🍦.
8. ✅ Aparece el modal de búsqueda de taxi.
9. ✅ Mostrar información del conductor en el modal.

---

## 📦 Recursos

Paquetes necesarios:
- `python`    Ver.- 3.13.12
- `pytest`    Ver.- 8.3.5
- `selenium`  Ver.- 4.31.0


## 📦 Instrucciones
- Ejecuta todas las pruebas del proyecto a través de la terminal de PyCharm: escribe pytest main.py en la terminal.
- Ejecuta la pruebas a través de la interfaz de PyCharm haciendo clic en el botón con un triángulo verde en la parte superior.
  - Asegúrate de ejecutarlas en el archivo correcto.
- Otra forma de ejecutar la prueba es haciendo clic en la flecha verde junto a las pruebas en el código.
- Las pruebas están dentro de una sola clase, separadas en partes.
