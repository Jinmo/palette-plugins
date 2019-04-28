from __palette__ import Palette, show_palette, Action

import idaapi
import requests
import json
import threading

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
    def handler():
        headers = json.loads(sess.get(REPO_URL).content).get('tree')
        headers = map(lambda x: x['path'], headers)
        actions = list(Action(handler=partial(import_headers, x), id=x, description= x)
                       for x in headers)
        show_palette(Palette(myplugin_t.wanted_name, "Enter header path...", actions))
    t = threading.Thread(target=handler)
    t.start()


# Helper for registering actions
def register_action(name, shortcut=''):
    def handler(f):
        # 1) Create the handler class
        class MyHandler(idaapi.action_handler_t):
            def __init__(self):
                idaapi.action_handler_t.__init__(self)

            # Say hello when invoked.
            def activate(self, ctx):
                t = threading.Thread(target=f)
                t.start()
                return 1

            # This action is always available.
            def update(self, ctx):
                return idaapi.AST_ENABLE_ALWAYS

        # 2) Describe the action
        action_desc = idaapi.action_desc_t(
            name,  # The action name. This acts like an ID and must be unique
            name,  # The action text.
            MyHandler(),  # The action handler.
            shortcut,  # Optional: the action shortcut
            name,  # Optional: the action tooltip (available in menus/toolbar)
            0)  # Optional: the action icon (shows when in menus/toolbars)

        # 3) Register the action
        idaapi.register_action(action_desc)

    return handler


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
