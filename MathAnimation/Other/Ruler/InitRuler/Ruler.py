from manim import *
import numpy as np


def create_ruler( 
    width: float, 
    height: float,
    count_division: int,
    count_subdivision: int = 0,
    width_division_ident: float = .05,
    height_division: float = .45,
    height_subdivision: float = .25
):
    shape = np.array([
        [0, 0, 0],
        [width, 0, 0],
        [width, -height, 0],
        [0, -height, 0] 
    ])
    ruler_shape = Polygon(*shape, color=BLACK)

    step_division = (1 - width_division_ident)*width/(count_division-1)        
    div_x = np.arange(.5*width_division_ident*width, width, step_division)
    div_x = np.repeat(div_x, 2)
    div_y = np.full((count_division,2), [0,-height_division*height])
    division = np.vstack((div_x, div_y.reshape(-1))).transpose()

    ruler_division = VGroup(*[
        Line(
            np.append(division[i], 0), 
            np.append(division[i+1], 0), 
            color=BLACK
        ) for i in range(0, 2*count_division, 2)
    ])
    
    if count_subdivision > 0:
        step_subdivision = step_division/(count_subdivision + 1) 
        temp = np.arange(step_subdivision, step_division, step_subdivision)
        temp += .5*width_division_ident*width
        subdiv_x = np.array([temp + step_division*i for i in range(count_division - 1)])
        subdiv_x = np.repeat(subdiv_x.reshape(-1), 2)
        subdiv_y = np.full(
            ((count_division - 1)*count_subdivision, 2), 
            [0, -height_subdivision*height]
        )
        subdivision = np.vstack((subdiv_x, subdiv_y.reshape(-1))).transpose()
        ruler_subdivision = VGroup(*[
            Line(
                np.append(subdivision[i], 0), 
                np.append(subdivision[i+1], 0), 
                color=BLACK
            ) for i in range(0, 2*(count_division-1)*count_subdivision, 2)
        ])
        
        return VGroup(ruler_shape, ruler_division, ruler_subdivision).move_to(ORIGIN)
    
    return VGroup(ruler_shape, ruler_division).move_to(ORIGIN)