# This file is part of Indico.
# Copyright (C) 2002 - 2015 European Organization for Nuclear Research (CERN).
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# Indico is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Indico; if not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from indico.core import signals
from indico.modules.users.ext import ExtraUserPreferences
from indico.modules.users.models.users import User
from indico.modules.users.models.settings import UserSetting, UserSettingsProxy
from indico.util.i18n import _
from indico.web.flask.util import url_for


__all__ = ('ExtraUserPreferences', 'User', 'UserSetting', 'UserSettingsProxy', 'user_settings')

user_settings = UserSettingsProxy('users', {
    'lang': None,
    'timezone': None,
    'force_timezone': False,  # always use the user's timezone instead of an event's timezone
    'show_past_events': False,
    'synced_fields': None  # None to synchronise all fields, empty set to not synchronize
})


@signals.admin_sidemenu.connect
def _extend_admin_menu(sender, **kwargs):
    from MaKaC.webinterface.wcomponents import SideMenuItem
    return 'users', SideMenuItem(_("Users"), url_for('users.users_admin'))
