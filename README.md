# python-set-solver

This is a set solver for the card game Set, entirely written by me for Python 3.7

All rights for the underlying game 'Set' are reserved by Set Enterprises, Inc.

## usage

The file SetSolver.py can be run from the command line and takes a filename as an argument. Each card should be listed on a single line in filename, with number, color, fill, and shape listed separated by spaces. For example:

1 red hollow squiggle
2 green hatched ovals

Shapes can be singular or pluralized as desired. 

Custom fill options can be passed using the --fill option, if the standard group of 'filled', 'hatched', and 'hollow' are not desired. If --fill is raised, the first line of filename should list the three custom fill options. For example:

empty shaded solid
1 red empty squiggle
2 green shaded ovals