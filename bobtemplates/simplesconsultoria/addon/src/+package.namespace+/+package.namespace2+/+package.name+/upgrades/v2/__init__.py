# -*- coding: utf-8 -*-
from {{{ package.namespace }}}.{{{ package.namespace2 }}}.{{{ package.name }}}.config import PROJECTNAME
from plone.app.upgrade.utils import loadMigrationProfile

import logging


def apply_profile(context):
    """Apply profile."""
    logger = logging.getLogger(PROJECTNAME)
    profile = 'profile-{{{ package.namespace }}}.{{{ package.namespace2 }}}.{{{ package.name }}}.upgrades.v1010:default'
    loadMigrationProfile(context, profile)
    logger.info('Profile migrated')

