import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import json
import time

# Configuración inicial
box_size = 1e-6  # Tamaño de la caja
dt = 1e-10  # Paso de tiempo

# Leer archivo JSON
with open('molecules.json', 'r') as file:
    data = json.load(file)

# Procesar moléculas desde el JSON
molecules = data['molecules']
num_particles = sum(molecule['numero'] for molecule in molecules)

# Inicializar posiciones, velocidades y parámetros específicos
positions = np.random.uniform(0, box_size, (num_particles, 3))
velocities = np.zeros((num_particles, 3))
sigmas = []
epsilons = []
colors = []

# Crear partículas para cada molécula
index = 0
for molecule in molecules:
    num = molecule['numero']
    positions[index:index+num] = np.random.uniform(0, box_size, (num, 3))
    color = tuple(int(c) / 255 for c in molecule['color'].split(','))
    colors.extend([color] * num)
    sigmas.extend([molecule['sigma']] * num)
    epsilons.extend([molecule['epsilon']] * num)
    index += num

sigmas = np.array(sigmas)
epsilons = np.array(epsilons)

# Configuración de la figura 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, box_size)
ax.set_ylim(0, box_size)
ax.set_zlim(0, box_size)
ax.set_box_aspect([1, 1, 1])  # Proporción cúbica
# Etiquetas para los ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Crear los puntos
scatter = ax.scatter(
    positions[:, 0], positions[:, 1], positions[:, 2], c=colors, s=100
)

# Texto para mostrar el tiempo
time_text = ax.text2D(0.05, 0.95, f'Tiempo: 0.0', transform=ax.transAxes, fontsize=12, color='black')

# Variables para zoom
zoom_factor = 1.0
zoom_step = 0.5  # Incremento/decremento del zoom

# Función para manejar el zoom con el scroll del mouse
def on_scroll(event):
    global zoom_factor
    if event.button == 'up':  # Scroll hacia arriba
        zoom_factor = max(0.1, zoom_factor - zoom_step)
    elif event.button == 'down':  # Scroll hacia abajo
        zoom_factor += zoom_step

    # Ajustar los límites del eje
    mid = box_size / 2
    range_size = box_size * zoom_factor / 2
    ax.set_xlim(mid - range_size, mid + range_size)
    ax.set_ylim(mid - range_size, mid + range_size)
    ax.set_zlim(mid - range_size, mid + range_size)
    fig.canvas.draw_idle()

# Conectar el evento de scroll
fig.canvas.mpl_connect('scroll_event', on_scroll)

def LennardJones(positions, sigmas, epsilons):
    forces = np.zeros_like(positions)
    for i in range(num_particles):
        for j in range(num_particles):
            if not j == i:
                r_vec = positions[j] - positions[i]
                r = np.linalg.norm(r_vec)
                sigma_ij = (sigmas[i] + sigmas[j]) / 2  # Regla de mezcla para sigma
                epsilon_ij = (epsilons[i] * epsilons[j]) ** 0.5  # Regla de mezcla para epsilon
                force_magnitude = -24 * epsilon_ij * (2 * (sigma_ij**12 / r**13) - (sigma_ij**6 / r**7))
                force_vec = force_magnitude * r_vec / r
                forces[i] += force_vec
    return forces

# Función de actualización para la animación
def update(frame):
    global positions, velocities
    # Calcular fuerzas y actualizar velocidades
    forces = LennardJones(positions, sigmas, epsilons)
    velocities += forces * dt
    # Actualizar posiciones
    positions += velocities * dt

    # Verificar colisiones con las paredes y revertir velocidad si hay colisión
    for i in range(3):  # x, y, z
        # Implementar la regla de aparición por el otro lado
        pass

    # Actualizar datos de los puntos
    scatter._offsets3d = (positions[:, 0], positions[:, 1], positions[:, 2])

    # Actualizar el tiempo transcurrido en el texto
    time_text.set_text(f'Tiempo: {frame * dt:.2e} s')

    return scatter, time_text

# Animar la simulación
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=False)

# Mostrar la simulación
plt.show()
