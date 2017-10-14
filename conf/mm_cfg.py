# -*- python -*-

# Copyright (C) 1998,1999,2000 by the Free Software Foundation, Inc.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301 USA


"""This is the module which takes your site-specific settings.

From a raw distribution it should be copied to mm_cfg.py.  If you
already have an mm_cfg.py, be careful to add in only the new settings
you want.  The complete set of distributed defaults, with annotation,
are in ./Defaults.  In mm_cfg, override only those you want to
change, after the

  from Defaults import *

line (see below).

Note that these are just default settings - many can be overridden via the
admin and user interfaces on a per-list or per-user basis.

Note also that some of the settings are resolved against the active list
setting by using the value as a format string against the
list-instance-object's dictionary - see the distributed value of
DEFAULT_MSG_FOOTER for an example."""


#######################################################
#    Here's where we get the distributed defaults.    #

from Defaults import *

##############################################################
# Put YOUR site-specific configuration below, in mm_cfg.py . #
# See Defaults.py for explanations of the values.            #

#-------------------------------------------------------------
# The name of the list Mailman uses to send password reminders
# and similar. Don't change if you want mailman-owner to be
# a valid local part.
MAILMAN_SITE_LIST = 'mailman'

#-------------------------------------------------------------
# If you change these, you have to configure your http server
# accordingly (Alias and ScriptAlias directives in most httpds)

DEFAULT_URL_PATTERN = 'https://%s__MAILMAN_WEB_PATH__/'
IMAGE_LOGOS         = '/mailman/images/'
SITE_LOGO           = '/mailman/images/debianpowered.png'

#-------------------------------------------------------------
# Default domain for email addresses of newly created MLs
DEFAULT_EMAIL_HOST = '__MAILMAN_DOMAIN__'
#-------------------------------------------------------------
# Default host for web interface of newly created MLs
DEFAULT_URL_HOST   = '__MAILMAN_DOMAIN__'
#-------------------------------------------------------------
# Required when setting any of its arguments.
add_virtualhost(DEFAULT_URL_HOST, DEFAULT_EMAIL_HOST)

#-------------------------------------------------------------
# We need this for the virtual alias file to explicitly
# contain @localhost
VIRTUAL_MAILMAN_LOCAL_DOMAIN = "localhost"

#-------------------------------------------------------------
# Path for archives
PUBLIC_ARCHIVE_URL = 'https://%(hostname)s/mailman/archives/%(listname)s'

#-------------------------------------------------------------
# The default language for this server.
DEFAULT_SERVER_LANGUAGE = '__MAILMAN_LANGUAGE__'

#-------------------------------------------------------------
# Iirc this was used in pre 2.1, leave it for now
USE_ENVELOPE_SENDER    = 0              # Still used?

#-------------------------------------------------------------
# Unset send_reminders on newly created lists
DEFAULT_SEND_REMINDERS = 0

#-------------------------------------------------------------
# Uncomment this if you configured your MTA such that it
# automatically recognizes newly created lists.
# (see /usr/share/doc/mailman/README.Exim4.Debian or
# /usr/share/mailman/postfix-to-mailman.py)
# MTA=None   # Misnomer, suppresses alias output on newlist

#-------------------------------------------------------------
# Uncomment if you use Postfix virtual domains (but not
# postfix-to-mailman.py), but be sure to see
# /usr/share/doc/mailman/README.Debian first.
MTA='Postfix'

POSTFIX_STYLE_VIRTUAL_DOMAINS = [ '__MAILMAN_DOMAIN__' ]

#-------------------------------------------------------------
# Uncomment if you want to filter mail with SpamAssassin. For
# more information please visit this website:
# http://www.jamesh.id.au/articles/mailman-spamassassin/
# GLOBAL_PIPELINE.insert(1, 'SpamAssassin')

# Note - if you're looking for something that is imported from mm_cfg, but you
# didn't find it above, it's probably in /usr/lib/mailman/Mailman/Defaults.py.


#-------------------------------------------------------------
# Web page style configuration

WEB_BG_COLOR = '#f0f0f0'                          # Page background
WEB_HEADER_COLOR = '#f0f0f0'                      # Major section headers
WEB_SUBHEADER_COLOR = '#fff0d0'                   # Minor section headers
WEB_ADMINITEM_COLOR = '#e7e7e7'                   # Option field background
WEB_ADMINPW_COLOR = '#ff9999'                     # Password box color
WEB_ERROR_COLOR = 'red'                           # Error message foreground
WEB_LINK_COLOR = ''                               # If true, forces LINK=
WEB_ALINK_COLOR = ''                              # If true, forces ALINK=
WEB_VLINK_COLOR = ''                              # If true, forces VLINK=
WEB_HIGHLIGHT_COLOR = '#dddddd'                   # If true, alternating rows
                                                  # in listinfo & admin display

