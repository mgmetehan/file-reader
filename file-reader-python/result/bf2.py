from pathlib import Path
from functools import partial
from io import DEFAULT_BUFFER_SIZE

path = Path("/Users/mgmetehan/Desktop/chomar/c-port.txt")
with path.open('rb') as file:
    reader = partial(file.read1, DEFAULT_BUFFER_SIZE)
    file_iterator = iter(reader, bytes())
    for chunk in file_iterator:
        print(chunk)
        print(chunk.decode('utf-8'))
