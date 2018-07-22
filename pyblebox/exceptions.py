"""
Copyright (c) 2018 Tomasz 'Zen' Napierala <tomasz@napierala.org>

Licensed under Apache 2 licence. All rights reserved.
"""


class wLightBoxSError(Exception):
    """General wLightBoxSError exception occurred."""

    pass


class wLightBoxSConnectionError(wLightBoxSError):
    """When a connection error is encountered."""

    pass
