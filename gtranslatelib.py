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

import os
import urllib.request
import urllib.parse
import json

class UrlHandler(object):
    def __init__(self, url):
        ua = "Mozilla/5.0 (X11; Linux x86_64; rv:20.0) Gecko/20100101 Firefox/20.0"
        self._request = urllib.request.Request(url, headers={'User-Agent': ua})

    def getcontent(self):
        f = urllib.request.urlopen(self._request)
        return f.read().decode('utf-8')

class TranslateResponse(object):
    def __init__(self):
        self._sentence = []
        self._dict = []

    def get_sentence(self):
        return self._sentence

    def set_sentence(self, value):
        self._sentence = value

#class Dictionary(object):
#    def __init__(self, value):
#        self._value = value
#        self.words = dict()
#        self._cterm = 0
#        self._fill() 
#
#    def __iter__(self):
#        return self
#
#    def __next__(self):
#        print(self.words)
#        if self._cterm > len(self.terms):
#            raise StopIteration
#        self._cterm += 1
#        return self.words[self.terms[self._cterm]]
#
#    def _fill(self):
#        self.terms = self._value[0]['terms']
#        for t in self.terms:
#            for i in self._value[0]['entry']:
#                if i['word'] == t:
#                    self.words.update({t: i['reverse_translation']})


class Translate(object):
    def __init__(self):
        self.baseurl = "http://translate.google.com/translate_a/t?"
        ## Load languages
        f = open(os.path.dirname(os.path.abspath(__file__)) + "/languages.json")
        self.langs = json.load(f)
        f.close()

    def get_lang_codes(self):
        return self.langs['codes']

    def get_lang_name(self, lcode):
        return self.langs['names'][lcode]
       
    def translate(self, lcfrom, lcto, text):
        url = urllib.parse.urlencode({'sl': lcfrom, 'tl': lcto, 'text': text,
                                     'client': 'j', 'ie': 'UTF-8', 'oe': 'UTF-8'})
        self._resp = UrlHandler(self.baseurl + url)
        t = json.loads(self._resp.getcontent())
        ## Create a new TranslateResponse object and return it
        tr = TranslateResponse()
        tr.set_sentence(t['sentences'])
        return tr

#    def getdict(self, lcfrom, lcto, word):
#        url = urllib.parse.urlencode({'sl': lcfrom, 'tl': lcto, 'text': word,
#                                     'client': 'j', 'ie': 'UTF-8', 'oe': 'UTF-8'})
#        self._resp = UrlHandler(self.baseurl + url)
#        t = json.loads(self._resp.getcontent())
#        ## Create a new Dictionary object and return it
#        #print(t)
#        return Dictionary(t['dict'])

