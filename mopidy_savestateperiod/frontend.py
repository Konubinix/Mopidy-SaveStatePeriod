#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pykka
from pykka.messages import ProxyCall

from mopidy import core
from mopidy.internal.gi import GLib


class SaveStatePeriodFrontend(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super().__init__()
        self.core = core
        self.config = config

    def on_start(self):
        GLib.timeout_add_seconds(self.config["savestateperiod"]["period"], self.periodic_save_state)

    def periodic_save_state(self):
        call = ProxyCall(attr_path=["_save_state"], args=[], kwargs={})
        self.core.actor_ref.ask(call, block=True)
        GLib.timeout_add_seconds(self.config["savestateperiod"]["period"], self.periodic_save_state)
