import numpy as np
import matplotlib
import matplotlib.pyplot as plt


class Particle:
    """A particle is defined by its position (x, y) and its charge q."""
    def __init__(self, x: float, y: float, q: float):
        self.x = x
        self.y = y
        self.q = q

    def plot_particle(self):
        if self.q > 0:
            color = "red"
        else:
            color = "blue"
        plt.plot(self.x, self.y, color=color, marker="o")

class Simu_E:
    def __init__(self, rangeX, rangeY):
        X, Y = np.meshgrid(rangeX, rangeY)
        self.gridX = X
        self.gridY = Y
        self.particles = []
        self.N = 0
        self.field = []

    def add_particle(self, x, y, q):
        self.particles.append(Particle(x, y, q))  # List of Particles
        self.N += 1

    def compute_electric_field(self):
        E = []
        # Iterate over all points in the grid
        for ii in range(len(self.gridY[:, 1])):  # Rows are Y
            E_row = []  # Store each row separately
            for jj in range(len(self.gridX[1, :])):  # Columns are X
                # Superposition principle
                Ex = 0
                Ey = 0
                for part in self.particles:
                    delx = self.gridX[1, jj] - part.x
                    dely = self.gridY[ii, 1] - part.y
                    den = delx**2 + dely**2
                    if den < 0.01:  # Avoid dividing by very small values
                        E_aux = 0
                    else:
                        E_aux = part.q / (pow(den, 1.5))  # Coulomb law in reduced units
                    Ex += E_aux * delx
                    Ey += E_aux * dely

                E_row.append((Ex, Ey))  # Append field as a TUPLE
            E.append(E_row)

        self.field = np.array(E)

    def plot_field(self, ax):
        plt.streamplot(self.gridX, self.gridY, self.field[:, :, 0], self.field[:, :, 1],
                       arrowsize=1, linewidth=0.4, color="grey")
        norm = np.sqrt(np.square(self.field[:, :, 0]) + np.square(self.field[:, :, 1]))

        factor = 500
        plt.quiver(self.gridX, self.gridY, factor*np.divide(self.field[:, :, 0], norm),
                   factor*np.divide(self.field[:, :, 1], norm), np.log(norm), angles="uv", cmap="turbo")

        plt.colorbar(label="log(|E*|)")

        for part in self.particles:
            part.plot_particle()

        plt.xlabel("x")
        plt.ylabel("y")


def onclick(event, fig, ax, E):
    """Event when clicking on plot."""
    plt.clf()
    q = np.random.choice([1, -1])
    E.add_particle(event.xdata, event.ydata, q)
    E.compute_electric_field()
    E.plot_field(ax)
    plt.title("Click to add point charge (random sign)")
    fig.canvas.draw()


# ----------------------------------------------------------------------------------------
# ------------------------------------- MAIN ---------------------------------------------
def main():
    rangex = np.linspace(-10, 10, 30)
    E = Simu_E(rangex, rangex)

    # Start plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.set_title("Click to add point charge (of random sign)")

    # Read input clicks
    fig.canvas.mpl_connect('button_press_event', lambda event: onclick(event, fig, ax, E))
    plt.show()

if __name__ == "__main__":
    main()
