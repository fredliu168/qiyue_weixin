#!/usr/bin/env python

import os


class Config(object):
    DEBUG = True
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = os.path.join(BASE_DIR, 'tmp')
    SESSION_USE_SIGNER = True

    WEIXIN_TOKEN = 'vunIxPzCptjTRj'
    WEIXIN_AESKEY = 'Gn7gwr9cqRuHD0esqBKPTLSZtSgsEdB6GIMligMeR1g'
    WEIXIN_CORPID = 'wxc8b8bbdb9e35e224'
    WEIXIN_AGTID = '1000006'
    WEIXIN_SECRET = '3BG9Res4XvmKPZxut0MUPB27imrLY492ZVkdgIs_B60'
