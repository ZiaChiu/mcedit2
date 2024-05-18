import functools
import os
from OpenGL import GL
from PySide6 import QtGui, QtOpenGL
import numpy as np
from mcedit2.util import glutils
from mcedit2.util.resources import resourcePath

__author__ = 'Rio'

def loadPNGTexture(filename, *a, **kw):
    try:
        w, h, ndata = loadPNGFile(filename)
        tex = glutils.Texture(name=os.path.basename(filename), image=ndata.ravel(),
                              width=w, height=h, *a, **kw)
        return tex
    except Exception as e:
        print("Exception loading ", filename, ": ", repr(e))
        return glutils.Texture()

def loadPNGImage(img):
    glImg = QtOpenGL.QGLWidget.convertToGLFormat(img)
    if glImg is None:
        raise ValueError(f"Loading png file {img}: Conversion to GL format failed.")

    ndata = np.frombuffer(glImg.bits(), dtype=np.uint8)
    w = glImg.width()
    h = glImg.height()
    b = glImg.depth() // 8

    assert len(ndata) == w * h * b
    return w, h, ndata.reshape((h, w, b))

def loadPNGData(data):
    img = QtGui.QImage.fromData(data)
    return loadPNGImage(img)

def loadPNGFile(filename):
    img = QtGui.QImage()
    if not os.path.isabs(filename):
        filename = resourcePath(f"mcedit2/assets/mcedit2/textures/{filename}")

    if not img.load(filename):
        raise IOError(f"Failed to read PNG file {filename}")
    return loadPNGImage(img)
