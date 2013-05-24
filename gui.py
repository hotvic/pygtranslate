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

from gi.repository import Gtk
import gtranslatelib

class MainWindow(Gtk.Window):
    def __init__(self, cbtranslate):
        super(Gtk.Window, self).__init__()
        # Some Variables
        self.cbtranslate = cbtranslate
        # Add main widgets
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.vbox)
        self.set_vbox()
        # Connect main events
        self.connect('destroy', Gtk.main_quit)

    def set_vbox(self):
        # Widgets
        self.swfrom = Gtk.ScrolledWindow()
        self.swto = Gtk.ScrolledWindow()
        self.wfrom = Gtk.TextView()
        self.wto = Gtk.TextView()
        self.lslangs = Gtk.ListStore(str, str)
        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.wbtnr = Gtk.Button()
        self.wbtnimg = Gtk.Image()
        self.wcbfrom = Gtk.ComboBox.new_with_model(self.lslangs)
        self.wcbto = Gtk.ComboBox.new_with_model(self.lslangs)
        self.wbtntr = Gtk.Button()
        renderer_text = Gtk.CellRendererText()
        # Add then
        self.wbtnr.add(self.wbtnimg)
        self.swfrom.add(self.wfrom)
        self.swto.add(self.wto)
        self.hbox.pack_start(self.wcbfrom, True, True, 0)
        self.hbox.pack_start(self.wbtnr, False, False, 0)
        self.hbox.pack_start(self.wcbto, True, True, 0)
        self.hbox.pack_start(self.wbtntr, False, False, 0)
        self.vbox.pack_start(self.swfrom, True, True, 0)
        self.vbox.pack_start(self.hbox, False, False, 6)
        self.vbox.pack_end(self.swto, True, True, 0)
        self.wcbfrom.pack_start(renderer_text, False)
        self.wcbto.pack_start(renderer_text, False)
        # Properties
        self.swfrom.set_vexpand(True)
        self.swfrom.set_hexpand(True)
        self.swto.set_vexpand(True)
        self.swto.set_hexpand(True)
        self.wbtnimg.set_from_stock(Gtk.STOCK_GO_FORWARD, Gtk.IconSize.BUTTON)
        self.wcbfrom.set_wrap_width(3)
        self.wcbto.set_wrap_width(3)
        self.wcbfrom.add_attribute(renderer_text, "text", 0)
        self.wcbto.add_attribute(renderer_text, "text", 0)
        self.wbtntr.set_label("Translate")
        # Connect events
        self.wbtnr.connect('clicked', self._invert_ft)
        self.wbtntr.connect('clicked', self.cbtranslate, self)

    def _invert_ft(self, button):
        old = self.wcbfrom.get_active_iter()
        self.wcbfrom.set_active_iter(self.wcbto.get_active_iter())
        self.wcbto.set_active_iter(old)
