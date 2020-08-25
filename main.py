# Kelompok 5
# Referensi yang digunakan untuk mempelajari Bresenham's Line Algorithm:
# http://www.uobabylon.edu.iq/eprints/publication_2_22893_6215.pdf

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-100.0, 100.0, -100.0, 100.0)

# Untuk menentukan apakah pixel harus naik, turun atau tetap


def sign(x):
    if (x < 0):
        return -1
    elif (x == 0):
        return 0
    else:
        return 1


def call_bresenham(x0, y0, x1, y1):

    x = x0
    y = y0

    delta_x = abs(x1 - x0)
    delta_y = abs(y1 - y0)

    sign_1 = sign(x1 - x0)
    sign_2 = sign(y1 - y0)

    if delta_y > delta_x:
        temp_delta_x = delta_x
        delta_x = delta_y
        delta_y = temp_delta_x
        interchange = 1
    else:
        interchange = 0

    e = (2 * delta_y) - delta_x
    a = 2 * delta_y
    b = (2 * delta_y) - (2 * delta_x)

    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

    for i in range(1, (delta_x + 1)):
        if (e < 0):
            if (interchange == 1):
                y += sign_2
            else:
                x += sign_1
                e += a
        else:
            x += sign_1
            y += sign_2
            e += b

        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()


def plotpoints():

    # Test case 1
    x0 = 0
    y0 = 0
    x1 = 50
    y1 = 50

    # Test case 2
    # x0 = 0
    # y0 = 0
    # x1 = 50
    # y1 = -50

    # Test case 3
    # x0 = 0
    # y0 = 0
    # x1 = -50
    # y1 = -50

    # Test case 4
    # x0 = 0
    # y0 = 0
    # x1 = -50
    # y1 = 50

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1.0, 1.0)
    glPointSize(5)

    glBegin(GL_LINES)

    glVertex2f(-100, 0)
    glVertex2f(100, 0)

    glVertex2f(0, -100)
    glVertex2f(0, 100)

    glEnd()

    call_bresenham(x0, y0, x1, y1)

    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Bresenham Algoritm")
    glutDisplayFunc(plotpoints)

    init()
    glutMainLoop()


main()
