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

from indico.modules.vc.controllers import (RHVCManageEvent, RHVCManageEventSelectService, RHVCManageEventCreate,
                                           RHVCManageEventModify, RHVCManageEventRefresh, RHVCManageEventRemove,
                                           RHVCEventPage, RHVCManageSearch, RHVCManageAttach)
from indico.web.flask.wrappers import IndicoBlueprint

vc_blueprint = _bp = IndicoBlueprint('vc', __name__, template_folder='templates')

# Event management
_bp.add_url_rule('/event/<confId>/manage/videoconference/', 'manage_vc_rooms', RHVCManageEvent)
_bp.add_url_rule('/event/<confId>/manage/videoconference/select', 'manage_vc_rooms_select',
                 RHVCManageEventSelectService, methods=('GET', 'POST'))
_bp.add_url_rule('/event/<confId>/manage/videoconference/<service>/create', 'manage_vc_rooms_create',
                 RHVCManageEventCreate, methods=('GET', 'POST'))
_bp.add_url_rule('/event/<confId>/manage/videoconference/<service>/<int:vc_room_id>/<int:event_vc_room_id>/',
                 'manage_vc_rooms_modify', RHVCManageEventModify, methods=('GET', 'POST'))
_bp.add_url_rule('/event/<confId>/manage/videoconference/<service>/<int:vc_room_id>/<int:event_vc_room_id>/remove',
                 'manage_vc_rooms_remove', RHVCManageEventRemove, methods=('POST',))
_bp.add_url_rule('/event/<confId>/manage/videoconference/<service>/<int:vc_room_id>/<int:event_vc_room_id>/refresh',
                 'manage_vc_rooms_refresh', RHVCManageEventRefresh, methods=('POST',))
_bp.add_url_rule('/event/<confId>/manage/videoconference/<service>/attach/',
                 'manage_vc_rooms_search_form', RHVCManageAttach, methods=('GET', 'POST'))
_bp.add_url_rule('/event/<confId>/manage/videoconference/<service>/search/',
                 'manage_vc_rooms_search', RHVCManageSearch)

# Event page
_bp.add_url_rule('/event/<confId>/videoconference/', 'event_videoconference', RHVCEventPage)