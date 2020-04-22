# differential-geometry
Практикумы по курсу Дифференциальной геометрии

## Практикум №1
Цель: научиться сглаживать замкнутую плоскую кривую с помощью потока кривизны.

Класс `curve_transform` в приложенном файле curvature_flow.py. 
Конструктор класса принимает на вход кривую в виде массива двумерных векторов (т.е. пар чисел).
В комментариях к методам указано, что они должны делать. Их можно условно разбить на три группы:
  - previous_edge, next_edge, turning_angle, curvature, N, kN - возвращают соответствующие свойства кривой в данной вершине
  - flow считает поток кривизны, transform преобразует кривую
  - is_round, mass_center, total_curvature возвращают соответствующие свойства кривой.

## Практикум №2

Мы задаём ориентируемое симплициальное многообразие X без края с помощью класса Variety. Оно обладает X.V вершинами, пронумерованными числами от 0 до V-1. Рёбра задаются парами вершин, ориентированные рёбра - парами вершин с учётом их порядка, а грани задаются тройками вершин с учётом ориентации, то есть направления обхода вершин. Основным полем объекта X является X.faces - массив ориентированных граней. Предполагается, что каждая вершина входит в какую-то грань.

Методы:
-  is_surface(), проверяющий, является ли комплекс X симплициальной поверхностью без края, и возвращающий соответствующее булево значение.
-  is_connected(), проверяющий, является ли поверхность X связной, и возвращающий соответствующее булево значение.
-  is_oriented(), проверяющий, является ли поверхность X ориентированной (то есть является ли данная ориентация граней согласованной), и возвращающий соответствующее булево значение.
-  is_orientable(), проверяющий, является ли поверхность X ориентируемой (то есть можно ли выбрать согласованную ориентацию граней), и возвращающий соответствующее булево значение.
-  Euler(), возвращающий эйлерову характеристику симплициального многообразия.
