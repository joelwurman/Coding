from pathlib import Path
from time import ctime
import shutil

source = Path("rosalind_lcsm.txt")
target = Path('sandbox_L/') / ""
path = Path('sandbox_L/rosalind_lcsm.txt')

shutil.copy(source, target)

path.write(str([p for p in range(4)]))


