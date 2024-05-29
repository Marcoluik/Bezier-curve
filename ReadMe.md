# How to use the script

Open your desired SSH of choice, whether it be Git bash, CMD or terminal.
Locate this directory, when typing ls you should se the bezier.py file.

Now you have three options

Brug: python script.py [linear|quadratic|cubic] x0 y0 x1 y1 [x2 y2] [x3 y3]

false or true?
True will add control lines and splines, false will only add the control points.
## For a linear Bézier-kurve
python bezier.py linear 0 0 1 1 true

## For a quadratic Bézier-kurve
python bezier.py quadratic 0 0 1 2 2 0 false

## For a qubic Bézier-kurve
python bezier.py cubic 0 0 1 3 3 3 4 0 true

# If youre on mac or python cmd dosent work- try python3
# For a linear Bézier-kurve
python3 bezier.py linear 0 0 1 1 true

# For a quadratic Bézier-kurve
python3 bezier.py quadratic 0 0 1 2 2 0 false

# For a qubic Bézier-kurve
python3 bezier.py cubic 0 0 1 3 3 3 4 0 true