#!/usr/bin/env python

from dynamodb_mapper.model import DynamoDBModel


class DoomMap(DynamoDBModel):
    __table__ = u"doom_map"
    __hash_key__ = u"episode"
    __range_key__ = u"map"
    __schema__ = {
        u"episode": int,
        u"map": int,
        u"name": unicode,
        u"cheats": set,
    }
    __defaults__ = {
        u"cheats": set([u"Konami"]),
    }
