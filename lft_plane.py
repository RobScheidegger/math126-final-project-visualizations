from manimlib import *
from manimlib.scene.vector_space_scene import *

def LFT(a,b,c,d):
    return lambda z: float('inf') if (c * z + d) == 0 else (a * z + b) / (c * z + d)

def LFT_inv(a,b,c,d):
    return lambda z: float('inf') if (c * z - a) == 0 else (-d*z+b)/(c*z-a)

class ComplexTransformation(LinearTransformationScene):
    def construct(self):
        line = Square()
        moving_line = line.copy()

        c_grid = ComplexPlane()
        moving_c_grid = c_grid.copy()
        moving_c_grid.prepare_for_nonlinear_transform()
        c_grid.set_stroke(BLUE_E, 1)
        c_grid.add_coordinate_labels(font_size=24)


        self.play(
            Write(c_grid, run_time=1),
            FadeIn(moving_c_grid),
            #Write(line, run_time=1),
            FadeIn(moving_line),
        )
        self.wait()

        seq = [(1,0,0,1), (-2,2,1,2), (-4,8,-2,1), (1,0,0,1)]

        for i in range(len(seq) - 1):
            self.play(moving_c_grid.animate.apply_complex_function(lambda x: LFT(*seq[i+1])(LFT_inv(*seq[i])(x))),
                moving_line.animate.apply_complex_function(lambda x: LFT(*seq[i+1])(LFT_inv(*seq[i])(x))),
                run_time=4
            )