angle = None
branches = None

def setup():
    size(400, 400)
    global angle, branches
    angle = PI / 4
    branches = 8

def draw():
    background(0)
    translate(width / 2, height)
    global angle
    angle = map(mouseX, 0, width, 0, PI)
    branch(100)

def branch(len):
    stroke(255)
    strokeWeight(2)
    line(0, 0, 0, -len)
    translate(0, -len)

    if len > 4:
        pushMatrix()
        rotate(angle)
        branch(len * 0.67)
        popMatrix()
        pushMatrix()
        rotate(-angle)
        branch(len * 0.67)
        popMatrix()
    else:
        fill(0, 255, 0)
        noStroke()
        triangle(0, 0, -5, 10, 5, 10) # draw a triangle to represent the leaf

run_sketch()