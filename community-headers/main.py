from __palette__ import Palette, show_palette, Action
from ifred.util import register_action

import idaapi
import requests
import json

from functools import partial
from idc import ParseTypes

sess = requests.Session()
sess.trust_env = False

REPO_URL = 'https://api.github.com/repos/Jinmo/headers/git/trees/master'
REPO_RAW_URL = 'https://raw.githubusercontent.com/Jinmo/headers/master/'


def import_headers(name, item):
    r = sess.get(REPO_RAW_URL + name)
    ParseTypes(str(r.content))
    print 'loading', name, 'done'
    return True


def show_online_headers():
    headers = json.loads(sess.get(REPO_URL).content).get('tree')
    headers = map(lambda x: x['path'], headers)
    actions = list(Action(handler=partial(import_headers, x), id=x, description= x)
                   for x in headers)
    show_palette(Palette(myplugin_t.wanted_name, actions))


class myplugin_t(idaapi.plugin_t):
    flags = idaapi.PLUGIN_HIDE | idaapi.PLUGIN_FIX
    comment = "This is a comment"
    help = "Finds headers"
    wanted_name = "Community headers"
    wanted_hotkey = ""

    def init(self):
        register_action('Community Headers: Find headers online...')(show_online_headers)
        return idaapi.PLUGIN_OK

    def run(self, arg):
        pass

    def term(self):
        pass


def PLUGIN_ENTRY():
    return myplugin_t()
