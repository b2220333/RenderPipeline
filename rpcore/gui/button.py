"""

RenderPipeline

Copyright (c) 2014-2016 tobspr <tobias.springer1@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

from panda3d.core import Vec3, Vec4
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectGui import DGG

from rpcore.globals import Globals
from rpcore.rpobject import RPObject


class Button(RPObject):

    """ Simple wrapper around DirectButton, providing a simpler interface """

    def __init__(self, text="", parent=None, x=0, y=0, width=80, callback=None, bg=(0, 0, 0, 1)):
        RPObject.__init__(self)
        color = Vec4(1)
        font = Globals.font
        self._width, self._height = width, 13
        self._initial_pos = self._translate_pos(x, y)

        self._node = DirectButton(
            text=text, parent=parent, pos=self._initial_pos, scale=(1, 1, 1),
            text_font=font, state=DGG.NORMAL, frameColor=bg, text_fg=color,
            text_scale=17, text_bg=(0, 0, 0, 0), pressEffect=1, relief=DGG.FLAT,
            frameSize=(-self._width // 2, self._width // 2, 10 + self._height, -self._height))

        if callback:
            self._node.bind(DGG.B1PRESS, callback)

    def _translate_pos(self, x, y):
        """ Converts 2d coordinates to pandas coordinate system """
        return Vec3(x + self._width / 2.0, 1, -y - self._height)

    def set_text(self, text):
        """ Changes the text, remember to pass may_change to the constructor,
        otherwise this method does not work. """
        self._node["text"] = text

    def get_initial_pos(self):
        """ Returns the initial position of the text. This can be used for
        animations """
        return self._initial_pos
