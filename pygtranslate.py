#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 
# Copyright © 2013 Victor Aurélio <victoraur.santos@gmail.com>
#
# This file is part of PyGTranslate.
#
# PyGTranslate is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyGTranslate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import gtranslatelib
import gui
from gi.repository import Gtk


class Main(object):
    def __init__(self):
        self.tro = gtranslatelib.Translate()
        self.gui = gui.MainWindow(self.cbtranslate)
        self._filllangs()

    def cbtranslate(self, button, data):
        lfrom = data.lslangs[data.wcbfrom.get_active_iter()][1]
        lto = data.lslangs[data.wcbto.get_active_iter()][1]
        bfrom = data.wfrom.get_buffer()
        bto = data.wto.get_buffer()
        start, end = bfrom.get_start_iter(), bfrom.get_end_iter()
        tfrom = bfrom.get_text(start, end, True)

        trr = self.tro.translate(lfrom, lto, tfrom)
        translated = str()
        for t in trr.get_sentence():
            translated += t['trans']
        bto.set_text(translated)

    def _filllangs(self):
        for lc in self.tro.get_lang_codes():
            self.gui.lslangs.append([self.tro.get_lang_name(lc), lc])    

    def run(self):
        self.gui.show_all()
        Gtk.main()

if __name__ == "__main__":
    main = Main()
    main.run()
