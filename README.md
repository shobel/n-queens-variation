# n-queens-variation

Problem story:
People are riding around on scooters in a city. Policemen must be placed around the city so that the maximum number of scooters cross their paths collectively. Whenever a scooter runs into a policman, the policemen gain an "activity point". Policemen placement rules follow the same rules as queens on a chessboard, i.e. If the city is represented as a 2D matrix, there cannot be 2 policeman in the same row column or diagonal path.

Input file format:
A file called input.txt must be created. It will contain several lines of information about the city. 
First line: strictly positive 32-bit integer n, the width and height of the nx ncity area, n<= 15.
Second line: strictly positive 32-bit integer p, the number of police officers
Third line: strictly positive 32-bit integer s, the number of scooters
Next s*12lines: the list of scooter x,y coordinatesover time, separated with the End-of-line character LF.  With sscooters and 12 timestepsin a day, this results in 12 coordinatesper scooter.

Output file:
The program will output a file called output.txt that will contain the max activity points collected by the policemen.   

How to run:
Requires python 2.7+
`python n-queens-solver.py`
