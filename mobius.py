from manimlib import *
from manimlib.scene.vector_space_scene import *
import cmath

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
            Write(c_grid, run_time=0.3),
            FadeIn(moving_c_grid),
            #Write(line, run_time=1),
            FadeIn(moving_line),
        )
        self.wait()

        seq1 = [(1,0,0,1), (1,1+1j,0,1), (cmath.exp(math.pi/3*1j), 1+1j, 0, 1), (1.5*cmath.exp(math.pi/3*1j), 1+1j, 0, 1), (1,0,0,1), (0,1,1,0), (1,0,0,1)]
        seq2 = [(1,0,0,1), (-2,2,1,2), (-4,8,-2,1), (0,8,3,4), (1,0,0,1)]
        seq1text = [TexText('$f(z)=' + s + '$') for s in ['z', 'z+(1+1i)', 'e^{i\\pi/3}z+(1+1i)', '\\frac32e^{i\\pi/3}z+(1+1i)', 'z', '\\frac1z', 'z']]
        seq2text = [TexText('$f(z)=' + s + '$') for s in ['z', '\\frac{-2z+z}{z+2}', '\\frac{-4z+8}{-2z+1}', '\\frac{8}{3z+4}', 'z']]
        seq2text[0] = seq1text[-1]

        for t in seq1text:
            t.to_edge(UP)
            t.to_edge(RIGHT)
        for t in seq2text:
            t.to_edge(UP)
            t.to_edge(RIGHT)
        Write(seq1text[0])


        for i in range(len(seq1) - 1):
            self.play(moving_c_grid.animate.apply_complex_function(lambda x: LFT(*seq1[i+1])(LFT_inv(*seq1[i])(x))),
                moving_line.animate.apply_complex_function(lambda x: LFT(*seq1[i+1])(LFT_inv(*seq1[i])(x))),
                ReplacementTransform(seq1text[i], seq1text[i+1]),
                run_time=1.5
            )
        self.wait(2)

        for i in range(len(seq2) - 1):
            self.play(moving_c_grid.animate.apply_complex_function(lambda x: LFT(*seq2[i+1])(LFT_inv(*seq2[i])(x))),
                moving_line.animate.apply_complex_function(lambda x: LFT(*seq2[i+1])(LFT_inv(*seq2[i])(x))),
                ReplacementTransform(seq2text[i], seq2text[i+1]),
                run_time=3
            )