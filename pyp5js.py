import js

pyp5js = js.window

# can't import directly: import js.window as py5js because a setter doesn't
# seem to be implemented in the Pyodide side?
# core/pyproxy.ts
def setup(width = 400, height = 400):
    pyp5js.createCanvas(width, height)

