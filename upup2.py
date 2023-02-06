#!/usr/bin/env python3
import time
import subprocess
import logging

def update_upgrade_autoremove():
    logging.basicConfig(filename='upup.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.info('Running update...')
    update = subprocess.run(["sudo", "apt-get", "update"], capture_output=False, text=True)
    logging.debug(update.stdout)
    logging.debug(update.stderr)

    logging.info('Running upgrade...')
    upgrade = subprocess.run(["sudo", "apt-get", "upgrade"], capture_output=False, text=True)
    logging.debug(upgrade.stdout)
    logging.debug(upgrade.stderr)

    logging.info('Running autoremove...')
    autoremove = subprocess.run(["sudo", "apt-get", "autoremove"], capture_output=False, text=True)
    logging.debug(autoremove.stdout)
    logging.debug(autoremove.stderr)

if __name__ == "__main__":
    update_upgrade_autoremove()
    input("Press Enter to exit...")
    pass


