import pytest


def test_calculate_triangle_type():
	from triangle import calculate_triangle_type

	assert calculate_triangle_type([1.1, 1.1, 1.1]) == "equilateral"
	assert calculate_triangle_type([1.1, 1.2, 1.1]) == "isosceles"
	assert calculate_triangle_type([1.1, 1.2, 1.3]) == "scalene"


def test_triangle_equilateral():
	from triangle import is_triangle_equilateral

	assert is_triangle_equilateral([1.1, 1.2, 1.3]) is False
	assert is_triangle_equilateral([1.1, 1.1, 1.1]) is True


def test_triangle_is_triangle_isosceles():
	from triangle import is_triangle_isosceles

	assert is_triangle_isosceles([1.1, 1.2, 1.3]) is False
	assert is_triangle_isosceles([1, 1.1, 1.1]) is True
	assert is_triangle_isosceles([1.1, 1.9, 1.5]) is False


def test_triangle_is_triangle_scalene():
	from triangle import is_triangle_scalene

	assert is_triangle_scalene([1.1, 1.2, 1.3]) is True
	assert is_triangle_scalene([1.1, 1.1, 1.1]) is False
	assert is_triangle_scalene([1.1, 1.11, 1.11]) is False
