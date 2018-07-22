"""
Copyright (c) 2018 Tomasz 'Zen' Napierala <tomasz@napierala.org>

Licensed under Apache 2 licence. All rights reserved.
"""

import time

import requests

from . import exceptions
from . import config


class wLightBoxS(object):
    """A class for a wLightBoxS LED controller."""

    def __init__(self, host):
        """Initialize the controller."""
        self.resource = 'http://{}'.format(host)
        self.timeout = 5
        self.data = None

        # Basic device information
        self.device_name = None
        self.type = None
        self.fv = None
        self.hv = None
        self.id = None
        self.ip = None

        # Network related information
        self.net_scanning = None
        self.net_ssid = None
        self.net_station_status = None
        self.net_ap_enable = None
        self.net_ap_ssid = None
        self.net_ap_passw = None

        # Light related information
        self.light_desired_color = 0
        self.light_current_color = 0
        self.light_fade_speed = 0

        self.on = None
        self.brightness = 0

    def get_status(self):
        """Get the detailed state from the controller."""
        try:
            request = requests.get(
                '{}/{}/{}'.format(self.resource, wLightBoxSAPIdevice, 'state'), timeout=self.timeout)
            raw_data_json = request.json()
            self.data = raw_data_json[self._mac]
            return self.data
        except (requests.exceptions.ConnectionError, ValueError):
            raise exceptions.wLightBoxSConnectionError()

    def _get_light_current_color(self):
        """Get current color, which is in fact brightness level in hex"""
        self.get_status()
        try:
            self.light_current_color = self.data['light']['currentColor']
        except TypeError:
            self.light_current_color = 'Unknown'

        return self.light_current_color

    def get_device_name(self):
        """Get device name"""
        self.get_status()
        try:
            self.device_name = self.data(['device']['deviceName'])
        except TypeError:
            self.device_name = 'Unknown'

        return self.device_name

    def get_brightness(self):
        """Get current brightness."""
        self._get_light_current_color()

        try:
            self.brightness = int(self.light_current_color, 16)
        except TypeError:
            self.brightness = 'Unknown'

        return self.brightness

    def get_light_state(self):
        """Get the light state."""
        brightness = self.get_brightness
        is_on = True if brightness > 0 else False
        try:
            self.on = is_on
        except TypeError:
            self.on = 'Unknown'

        return bool(self.on)

    def get_fv(self):
        """Get the current firmware version."""
        self.get_status()
        try:
            self.fv = self.data['device']['fv']
        except TypeError:
            self.fv = 'Unknown'

        return self.fv

    ## Setting parameters
    def set_brightness(self, brightness):
        """Set brightness of the light"""

        if 0 <= int(brightness) <= 255:
            pass
        else:
            raise ValueError('Brightness %s out of bound' % int(brightness))

        try:
            request = requests.get(self.resource + "/s/" + config.int_to_hex(brightness))
            if request.status_code == 200:
                pass
        except requests.exceptions.ConnectionError:
            raise exceptions.wLightBoxSConnectionError()

    def set_on(self):
        """Turn the light on with"""
        self.set_brightness(255)

    def set_off(self):
        """Turn the light off."""
        self.set_brightness(0)
