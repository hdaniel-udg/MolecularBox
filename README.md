# MolecularBox
Este proyecto implementa una simulación de dinámica molecular en 3D utilizando el potencial de Lennard-Jones. Permite modelar y visualizar el comportamiento de partículas interactuantes dentro de una caja cúbica, con un enfoque en la personalización y adaptabilidad.
=======
# Simulación de Dinámica Molecular en 3D

Este proyecto implementa una simulación de dinámica molecular en 3D utilizando el potencial de Lennard-Jones. Es ideal para visualizar y analizar la interacción de partículas dentro de un espacio cúbico definido, con un enfoque en la adaptabilidad para incluir nuevos potenciales.

## 🚀 Características
- **Simulación en tiempo real:** Visualización interactiva en 3D de partículas en movimiento.
- **Potencial de Lennard-Jones:** Interacciones calculadas con reglas de mezcla personalizables.
- **Configuración flexible:** Propiedades de moléculas definidas mediante un archivo JSON.
- **Zoom interactivo:** Ajusta la escala para explorar diferentes áreas de la simulación.
- **Fácil expansión:** Diseñado para incluir nuevos potenciales interatómicos en el futuro.

---

## 📋 Estructura del Proyecto

- **`main.py`:** Archivo principal que ejecuta la simulación.
- **`molecules.json`:** Archivo de configuración para definir las moléculas, incluyendo:
  - `nombre`: Nombre de la molécula.
  - `numero`: Cantidad de partículas.
  - `sigma`: Parámetro del potencial Lennard-Jones.
  - `epsilon`: Profundidad del potencial Lennard-Jones.
  - `color`: Color en formato RGB.

---

## 📂 Ejemplo de Archivo `molecules.json`

```json
{
  "molecules": [
    {
      "nombre": "Molécula A",
      "numero": 100,
      "sigma": 3.4e-10,
      "epsilon": 1.65e-21,
      "color": "255,0,0"
    },
    {
      "nombre": "Molécula B",
      "numero": 50,
      "sigma": 3.2e-10,
      "epsilon": 1.50e-21,
      "color": "0,255,0"
    }
  ]
}