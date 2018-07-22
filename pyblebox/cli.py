"""
Copyright (c) 2018 Tomasz 'Zen' Napierala <tomasz@napierala.org>

Licensed under Apache 2 licence. All rights reserved.
"""

import requests
import click

from pyblebox.wlightboxs import wLightBoxS

wLightBoxSAPIdevice = 'api/device'

TIMEOUT = 5

@click.group()
@click.version_option()
def main():
    """Simple command-line tool to get and set the values of a Blebox devices.
    """

@main.group('config')
def config():
    """Get and set the configuration of a Blebox device."""

@config.command('read')
@click.option('--ip', prompt="IP address of the device",
              help="IP address of the device.")
def read_config(ip):
    """Read the current configuration of a Blebox device."""
    click.echo("Read configuration from %s" % ip)
    api_caddr = 'http://{}/{}/state'.format(ip, wLightBoxSAPIdevice)
    #click.echo(api_caddr)
    request = requests.get(
        api_caddr, timeout=TIMEOUT)
    print(request.json())

@main.group('wlightboxs')
def wlightboxs():
    """Get and set details of a wlightboxs light."""

@wlightboxs.command('on')
@click.option('--ip', prompt="IP address of the wlightboxs",
                  help="IP address of the wlightboxs.")
def on(ip):
    """Switch the wlightboxs on."""
    click.echo("Switching %s ON" % ip)
    wlightboxs = wLightBoxS(ip)
    wlightboxs.set_brightness(255)

@wlightboxs.command('off')
@click.option('--ip', prompt="IP address of the wlightboxs",
                  help="IP address of the wlightboxs.")
def on(ip):
    """Switch the wlightboxs off."""
    click.echo("Switching %s OFF" % ip)
    wlightboxs = wLightBoxS(ip)
    wlightboxs.set_brightness(0)

@wlightboxs.command('brightness')
@click.option('--ip', prompt="IP address of the wlightboxs",
                  help="IP address of the wlightboxs.")
@click.option('--br', prompt="Brightness to set (0-255)",
                  help="Brightness to be set (0-255).")

def on(ip,br):
    """Change the brightness of the wlightboxs."""
    click.echo("Changing brightness of %s" % ip)
    wlightboxs = wLightBoxS(ip)
    wlightboxs.set_brightness(br)

if __name__ == '__main__':
    main()
