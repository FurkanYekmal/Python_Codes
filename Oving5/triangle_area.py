# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 00:36:06 2021

@author: Furkan Kaya
@email: furkakay@nmbu.no
"""
import numpy as np
import math

#v1 = [x1,y1]
#v2 = [x2,y2]
#v3 = [x3,y3]

def triangle_area(vertices):
        x1,y1 = vertices[0]
        x2,y2 = vertices[1]
        x3,y3 = vertices[2]
    
        return abs(0.5*((x2*y3)-(x3*y2)-(x1*y3)+(x3*y1)+(x1*y2)-(y1*x2)))
            
def test_triangle_area():
    """
    Verify the area of a triangle with vertices
    (0,0), (1,0), and (0,2).
    """
    v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg
    print(computed)

test_triangle_area()