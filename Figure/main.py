import numpy as np
import matplotlib.pyplot as plt

def Hermite(x1, x2, x1p, x2p, theta):
    phi1 = 2 * theta**3 - 3 * theta**2 + 1
    phi2 = theta**3 - 2 * theta**2 + theta
    phi3 = -2 * theta**3 + 3 * theta**2
    phi4 = theta**3 - theta**2
    return (phi1 * x1 + phi2 * x1p + phi3 * x2 + phi4 * x2p)

def Interpolate(points, slopes, nb_points):
    interpolated_points = []
    n = len(points)
    
    # Pour chaque segment
    for i in range(n - 1):
        x1, x2 = points[i], points[i + 1]
        x1p, x2p = slopes[i], slopes[i + 1]
        
        # Calculer nb_points points entre x1 et x2
        for j in range(nb_points):
            t = j / (nb_points - 1)
            point = Hermite(x1, x2, x1p, x2p, t)
            interpolated_points.append(point)
        
    return np.array(interpolated_points)

def Plot_points(points, slopes, interpolated_points):
    fig, ax = plt.subplots()
    
    # Points
    ox, oy = zip(*points)
    ax.plot(ox, oy, 'o', label='Points', color='red')

    # Pentes
    for (x, y), (dx, dy) in zip(points, slopes):
        ax.arrow(x, y, dx, dy, head_width=0.1, head_length=0.2, fc='gray', ec='gray', length_includes_head=True)
    ax.plot(0, 0, '-', label='Tangentes', color='gray')

    # Interpolation
    ix, iy = zip(*interpolated_points)
    ax.plot(ix, iy, '-', label='Interpolation', color='blue', linewidth=2)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    
    # Grid
    ax.grid(which='both', linestyle='--', linewidth=0.5)
    ax.grid(which='minor', linestyle=':', linewidth=0.2)
    ax.set_xticks(np.arange(0, 11, 1))
    ax.set_yticks(np.arange(0, 11, 1))
    ax.set_xticks(np.arange(0, 10.2, 0.2), minor=True)
    ax.set_yticks(np.arange(0, 10.2, 0.2), minor=True)
    
    ax.set_title('DM de Mathématiques - Interpolation d\'Hermite')
    ax.legend()
    plt.show()


points = np.array([
    [4, 9.6],
    [8.6, 8],
    [8.2, 4.6],
    [9.4, 5.4],
    [8, 3.2],
    [6, 2],
    [2.5, 2],
    [2, 7],
    [6, 7],
    [4, 9.6] 
])

slopes = np.array([
    [3, -0.1],
    [-3, -3.5],
    [2.5, -0.5],
    [0.4, -3],
    [-5, 0], 
    [1, -3],
    [-2, 2],
    [2, 1.5],
    [-0.4, 1],
    [3, -0.1] 
])

precision_interpolation = 30

interpolated = Interpolate(points, slopes, precision_interpolation)
Plot_points(points, slopes, interpolated)