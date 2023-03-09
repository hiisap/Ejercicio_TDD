"""
Your module description
"""

from funcion import menor

def test_menor():
    assert menor([5,52,4,1,7]) == 1
    assert menor([10,7,2,0,3]) == 0
    assert menor([2,100,14,30,70]) == 2
    