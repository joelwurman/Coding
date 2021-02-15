from pathlib import Path
#pathlib module... path class

path = Path()
for file in path.glob('*'):
    print(file)
