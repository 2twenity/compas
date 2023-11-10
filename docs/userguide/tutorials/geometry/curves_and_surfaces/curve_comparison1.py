from compas.geometry import Point
from compas.geometry import Polyline, Bezier
from compas.geometry import NurbsCurve
from compas.scene import SceneObject
from compas.colors import Color


points = [Point(0, 0, 0), Point(1, 3, 0), Point(2, 0, 0)]
bezier = Bezier(points)

points = [Point(3, 0, 0), Point(4, 3, 0), Point(5, 0, 0)]

curve1 = NurbsCurve.from_parameters(
    points=points,
    weights=[1.0, 1.0, 1.0],
    knots=[0.0, 1.0],
    multiplicities=[3, 3],
    degree=2,
)

curve2 = NurbsCurve.from_parameters(
    points=points,
    weights=[1.0, 2.0, 1.0],
    knots=[0.0, 1.0],
    multiplicities=[3, 3],
    degree=2,
)

curve3 = NurbsCurve.from_parameters(
    points=points,
    weights=[1.0, 1.0, 1.0],
    knots=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
    multiplicities=[1, 1, 1, 1, 1, 1],
    degree=2,
)

# ==============================================================================
# Visualisation
# ==============================================================================

SceneObject.clear()

SceneObject(Polyline(bezier.points)).draw()
SceneObject(Polyline(bezier.locus())).draw(show_points=True)

SceneObject(Polyline(curve1.points)).draw(show_points=True)

SceneObject(curve1).draw(color=Color.black())
SceneObject(curve2).draw(color=Color.pink())
SceneObject(curve3).draw(color=Color.azure())

SceneObject.redraw()
