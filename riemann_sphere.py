from manim import *
import numpy as np
import math

def sphere_to_plane(x, y, z):
    return (x / (1 - z), y / (1 - z), 0)

class SurfacesAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Surface(
            lambda u, v: np.array([
                np.cos(u)*np.cos(v),
                np.cos(u)*np.sin(v),
                np.sin(u)
            ]),
            u_range=[-PI/2,PI/2 - 0.2], v_range=[0,TAU],
            fill_opacity=0,
            checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32))

        sphere_points = [Point(color='#DDDDDD', location=[np.cos(u)*np.cos(v),  np.cos(u)*np.sin(v), np.sin(u)])
                        for u in np.arange(-math.pi / 2, math.pi / 2 - 0.01, math.pi / 5)
                        for v in np.arange(0, math.pi * 2, math.pi / 4)]
        sphere_lines = [Line(color='#DD4444', stroke_width=0.9, 
                             start=[0, 0, 1],
                             end=(sphere_to_plane(*[np.cos(u)*np.cos(v),  np.cos(u)*np.sin(v), np.sin(u)]) if np.sin(u) > 0 
                                    else ([np.cos(u)*np.cos(v),  np.cos(u)*np.sin(v), np.sin(u)])))
                        for u in np.arange(-math.pi / 2, math.pi / 2 - 0.01, math.pi / 5)
                        for v in np.arange(0, math.pi * 2, math.pi / 4)]

        self.set_camera_orientation(phi = 75 * DEGREES)
        self.begin_ambient_camera_rotation(rate = 0.2)


        self.add(axes)
        for point in sphere_points:
            self.add(point)
        self.add(sphere)
        self.play(*[FadeIn(line) for line in sphere_lines])
        self.wait()
        self.play(*[Transform(point, Point(color='#DDDDDD', location=sphere_to_plane(*point.location))) for point in sphere_points] 
            + [ApplyPointwiseFunction(lambda point: np.asarray(sphere_to_plane(*point)), sphere)])