import numpy as np
import matplotlib.pyplot as plt
import sys


def linear_bezier(p0, p1, t):
    return (1 - t) * p0 + t * p1


def quadratic_bezier(p0, p1, p2, t):
    return (1 - t) ** 2 * p0 + 2 * (1 - t) * t * p1 + t ** 2 * p2


def cubic_bezier(p0, p1, p2, p3, t):
    return (1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t ** 2 * p2 + t ** 3 * p3


def plot_intermediate_splines(points, t):
    n = len(points)
    while n > 1:
        new_points = []
        for i in range(n - 1):
            new_point = (1 - t) * points[i] + t * points[i + 1]
            new_points.append(new_point)
            plt.plot([points[i][0], points[i + 1][0]], [points[i][1], points[i + 1][1]], 'b--')
        points = new_points
        n = len(points)


def plot_curve(curve_type, points, show_control):
    t_values = np.linspace(0, 1, 100)

    if curve_type == "linear":
        p0, p1 = points
        curve_points = [linear_bezier(p0, p1, t) for t in t_values]
        curve_points = np.array(curve_points)
        plt.plot(curve_points[:, 0], curve_points[:, 1], label="Linear Bézier Curve")
        plt.scatter([p0[0], p1[0]], [p0[1], p1[1]], color='red')
        if show_control:
            plt.plot([p0[0], p1[0]], [p0[1], p1[1]], 'k--', label="Control Polygon")
            plot_intermediate_splines([p0, p1], 0.5)  # Show intermediate splines at t=0.5

    elif curve_type == "quadratic":
        p0, p1, p2 = points
        curve_points = [quadratic_bezier(p0, p1, p2, t) for t in t_values]
        curve_points = np.array(curve_points)
        plt.plot(curve_points[:, 0], curve_points[:, 1], label="Quadratic Bézier Curve")
        plt.scatter([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]], color='red')
        if show_control:
            plt.plot([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]], 'k--', label="Control Polygon")
            plot_intermediate_splines([p0, p1, p2], 0.5)  # Show intermediate splines at t=0.5

    elif curve_type == "cubic":
        p0, p1, p2, p3 = points
        curve_points = [cubic_bezier(p0, p1, p2, p3, t) for t in t_values]
        curve_points = np.array(curve_points)
        plt.plot(curve_points[:, 0], curve_points[:, 1], label="Cubic Bézier Curve")
        plt.scatter([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], color='red')
        if show_control:
            plt.plot([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], 'k--', label="Control Polygon")
            plot_intermediate_splines([p0, p1, p2, p3], 0.5)  # Show intermediate splines at t=0.5

    else:
        print("Invalid curve type! Use 'linear', 'quadratic', or 'cubic'.")
        return

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{curve_type.capitalize()} Bézier Curve')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py [linear|quadratic|cubic] x0 y0 x1 y1 [x2 y2] [x3 y3] [show_control]")
    else:
        curve_type = sys.argv[1].lower()
        points = list(map(float, sys.argv[2:-1]))
        show_control = sys.argv[-1].lower() == "true"

        if curve_type == "linear" and len(points) == 4:
            p0 = np.array([points[0], points[1]])
            p1 = np.array([points[2], points[3]])
            plot_curve(curve_type, [p0, p1], show_control)

        elif curve_type == "quadratic" and len(points) == 6:
            p0 = np.array([points[0], points[1]])
            p1 = np.array([points[2], points[3]])
            p2 = np.array([points[4], points[5]])
            plot_curve(curve_type, [p0, p1, p2], show_control)

        elif curve_type == "cubic" and len(points) == 8:
            p0 = np.array([points[0], points[1]])
            p1 = np.array([points[2], points[3]])
            p2 = np.array([points[4], points[5]])
            p3 = np.array([points[6], points[7]])
            plot_curve(curve_type, [p0, p1, p2, p3], show_control)

        else:
            print("Invalid number of control points for the selected curve type!")