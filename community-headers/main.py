from __palette__ import Palette

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


def show_online_headers(item):
    headers = json.loads(sess.get(REPO_URL).content).get('tree')
    headers = map(lambda x: x['path'], headers)
    actions = list({'handler': partial(import_headers, x), 'name': x}
                   for x in headers)
    return Palette(actions)


class myplugin_t(idaapi.plugin_t):
    flags = idaapi.PLUGIN_UNL
    comment = "This is a comment"
    help = "Finds headers"
    wanted_name = "Community headers"
    wanted_hotkey = ""

    def init(self):
        return idaapi.PLUGIN_OK

    def run(self, arg):
        entries = [
            {
                'name': 'Find headers online...',
                'handler': show_online_headers
            }
        ]

        Palette(entries).show()

    def term(self):
        pass


def PLUGIN_ENTRY():
    return myplugin_t()
