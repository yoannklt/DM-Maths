import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicHermiteSpline
from matplotlib.patches import Circle
import tkinter as tk
from tkinter import messagebox

class InterpolationApp:
    def __init__(self, master):
        self.master = master
        master.title("Interpolation Hermite")

        self.points = []
        self.derivatives = []

        self.label = tk.Label(master, text="Entrez un point au format (x, y) ou 'fin' pour terminer:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.label2 = tk.Label(master, text="Entrez la dérivée en ce point:")
        self.label2.pack()

        self.entry2 = tk.Entry(master)
        self.entry2.pack()

        self.add_button = tk.Button(master, text="Ajouter point", command=self.add_point)
        self.add_button.pack()

        self.label3 = tk.Label(master, text="Entrez la borne minimale pour x:")
        self.label3.pack()

        self.entry3 = tk.Entry(master)
        self.entry3.pack()

        self.label4 = tk.Label(master, text="Entrez la borne maximale pour x:")
        self.label4.pack()

        self.entry4 = tk.Entry(master)
        self.entry4.pack()

        self.label5 = tk.Label(master, text="Entrez la borne minimale pour y:")
        self.label5.pack()

        self.entry5 = tk.Entry(master)
        self.entry5.pack()

        self.label6 = tk.Label(master, text="Entrez la borne maximale pour y:")
        self.label6.pack()

        self.entry6 = tk.Entry(master)
        self.entry6.pack()

        self.label7 = tk.Label(master, text="Centre du cercle (x, y):")
        self.label7.pack()

        self.entry7 = tk.Entry(master)
        self.entry7.pack()

        self.label8 = tk.Label(master, text="Rayon du cercle:")
        self.label8.pack()

        self.entry8 = tk.Entry(master)
        self.entry8.pack()

        self.plot_button = tk.Button(master, text="Tracer", command=self.plot)
        self.plot_button.pack()

        self.plot_circle_button = tk.Button(master, text="Tracer cercle", command=self.plot_circle)
        self.plot_circle_button.pack()

    def add_point(self):
        try:
            point_input = self.entry.get()
            if point_input.lower() == 'fin':
                return
            x, y = map(float, point_input.split(','))
            derivative_input = float(self.entry2.get())
            self.points.append((x, y))
            self.derivatives.append(derivative_input)
            self.entry.delete(0, tk.END)
            self.entry2.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erreur", "Format invalide. Veuillez entrer des nombres décimaux.")

    def plot(self):
        try:
            xmin = float(self.entry3.get())
            xmax = float(self.entry4.get())
            ymin = float(self.entry5.get())
            ymax = float(self.entry6.get())

            if len(self.points) < 2:
                messagebox.showerror("Erreur", "Au moins deux points sont nécessaires pour l'interpolation.")
                return

            x_data, y_data = zip(*self.points)
            spline = CubicHermiteSpline(x_data, y_data, self.derivatives)

            x_values = np.linspace(xmin, xmax, 1000)
            y_values = spline(x_values)

            plt.plot(x_values, y_values, label="Courbe interpolée")
            plt.scatter(x_data, y_data, color='red', label="Points")
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Interpolation Hermite')
            plt.legend()
            plt.grid(True)
            plt.ylim(ymin, ymax)  # Limite des bornes Y
            plt.show()
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres décimaux pour les bornes.")

    def plot_circle(self):
        try:
            center_input = self.entry7.get()
            x_center, y_center = map(float, center_input.split(','))
            radius = float(self.entry8.get())

            circle = Circle((x_center, y_center), radius, edgecolor='purple', facecolor='none')
            plt.gca().add_patch(circle)
            plt.axis('equal')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Cercle')
            plt.grid(True)
            plt.show()
        except ValueError:
            messagebox.showerror("Erreur", "Format invalide. Veuillez entrer des nombres décimaux pour le centre et le rayon.")

def main():
    root = tk.Tk()
    app = InterpolationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
