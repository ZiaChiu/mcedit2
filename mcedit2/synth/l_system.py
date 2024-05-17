"""
    l_system
"""
import logging
from OpenGL import GL

from mcedit2.rendering.scenegraph.vertex_array import VertexNode
from mcedit2.rendering.selection import SelectionBoxNode
from mcedit2.rendering.vertexarraybuffer import VertexArrayBuffer
from mcedit2.util import bresenham
from mceditlib.selection import BoundingBox

log = logging.getLogger(__name__)


def applyReplacements(symbol_list):
    """
    Apply the rules associated with each symbol to the symbols in
    `symbol_list`. Symbols with no defined rule are returned as-is.

    The elements of `symbol_list` must be subclasses of Symbol.

    Returns a tuple of (`replaced`, `new_symbol_list`) where `replaced` is
    True if any symbols had triggered a replacement rule, and
    `new_symbol_list` is the new list after applying all replacement rules.
    If `replaced` is False, `new_symbol_list` should be identical to
    `symbol_list`
    """
    replaced = False
    new_list = []
    for symbol in symbol_list:
        if hasattr(symbol, 'replace'):
            replaced = True
            new_symbols = symbol.replace()
            new_list.extend(new_symbols)
        else:
            new_list.append(symbol)

    return replaced, new_list


def applyReplacementsIterated(symbol_list, repeats):
    """
    Repeatedly apply replacement rules to `symbol_list` up to `repeats` times or until no replacements are applied.

    This is a generator function. For each iteration, yields the iteration count and the intermediate list as a tuple.
    """
    for i in range(repeats):
        replaced, symbol_list = applyReplacements(symbol_list)
        if not replaced:
            break
        yield i, symbol_list


def renderBlocks(symbol_list):
    rendering = []
    for symbol in symbol_list:
        rendering.extend(symbol.renderBlocks())
    return rendering


def renderSceneNodes(symbol_list):
    rendering = []
    for symbol in symbol_list:
        rendering.extend(symbol.renderSceneNodes())
    return rendering


class Symbol:
    def __init__(self, **kw):
        self.parameters = kw

    def __getattr__(self, key):
        return self.parameters[key]

    def renderBlocks(self):
        """
        Implement this function to render this symbol as a list of Minecraft block
        placement commands, in the form of (x, y, z, blockType) tuples. Return an empty
        list if there is nothing to render.
        """
        return []

    def renderSceneNodes(self):
        """
        Implement this function to render this symbol as an OpenGL scene node. Typically only
        one Node is required. Return an empty list if there is nothing to render.
        """
        return []

    def __repr__(self):
        return f"{self.__class__.__name__}({self.parameters})"


class Geometric(Symbol, BoundingBox):
    """
    A symbol that can represent a region of 3D space as an axis-aligned
    bounding box.

    Inherits from mceditlib's BoundingBox and provides all derived
    properties such as center, volume, maximum, positions, the chunk
    coordinates [min,max][cx,cy,cz] and so on.

    Parameters:
    minx
    miny
    minz
    width
    height
    length
    """

    def __init__(self, box=None, **kw):
        Symbol.__init__(self, **kw)
        if box is None:
            origin = kw['minx'], kw['miny'], kw['minz']
            size = kw['width'], kw['height'], kw['length']
        else:
            origin = box.origin
            size = box.size
        BoundingBox.__init__(self, origin, size)

    def renderSceneNodes(self):
        node = SelectionBoxNode()  # xxx BoundingBoxNode
        node.selectionBox = self
        node.filled = False
        node.color = 1.0, 1.0, 1.0, 0.7
        return [node]


class Fill(Geometric):
    """
    Fills a 3D box with a chosen blocktype.

    Parameters:

    blocktype

    + parameters inherited from Geometric
    """

    def __init__(self, box=None, blocktype=None, **kw):
        super(Fill, self).__init__(box, **kw)
        if blocktype:
            self.parameters["blocktype"] = blocktype

    def renderBlocks(self):
        return [(x, y, z, self.blocktype) for x, y, z in self.positions]


class Line(Symbol):
    """
    Draws a line between the chosen points with a chosen blocktype.

    Parameters:

    blocktype: BlockType | str | int | (int, int)
    p1: Vector
    p2: Vector
    """

    def __init__(self, p1, p2, **kw):
        kw.setdefault("glColor", (255, 64, 64, 128))
        super(Line, self).__init__(**kw)
        self.p1 = p1
        self.p2 = p2

    def renderBlocks(self):
        for x, y, z in bresenham.bresenham(self.p1, self.p2):
            yield x, y, z, self.blocktype

    def renderSceneNodes(self):
        vertexArray = VertexArrayBuffer(2, GL.GL_LINES, False, False)
        vertexArray.vertex[:] = [self.p1, self.p2]
        vertexArray.vertex[:] += 0.5  # draw using box centers
        vertexArray.rgba[:] = self.glColor
        node = VertexNode([vertexArray])  # xxx LineNode
        return [node]
