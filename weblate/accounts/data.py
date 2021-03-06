# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2020 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from __future__ import unicode_literals

from weblate.accounts.notifications import FREQ_INSTANT, SCOPE_ADMIN, SCOPE_DEFAULT

DEFAULT_NOTIFICATIONS = [
    (SCOPE_DEFAULT, FREQ_INSTANT, 'LastAuthorCommentNotificaton'),
    (SCOPE_DEFAULT, FREQ_INSTANT, 'MentionCommentNotificaton'),
    (SCOPE_DEFAULT, FREQ_INSTANT, 'NewWhiteboardMessageNotificaton'),
    (SCOPE_ADMIN, FREQ_INSTANT, 'MergeFailureNotification'),
    (SCOPE_ADMIN, FREQ_INSTANT, 'ParseErrorNotification'),
    (SCOPE_ADMIN, FREQ_INSTANT, 'NewTranslationNotificaton'),
    (SCOPE_ADMIN, FREQ_INSTANT, 'NewComponentNotificaton'),
    (SCOPE_ADMIN, FREQ_INSTANT, 'NewAlertNotificaton'),
    (SCOPE_ADMIN, FREQ_INSTANT, 'NewWhiteboardMessageNotificaton'),
]


def create_default_notifications(user):
    for scope, frequency, notification in DEFAULT_NOTIFICATIONS:
        user.subscription_set.get_or_create(
            scope=scope,
            notification=notification,
            defaults={
                'frequency': frequency
            }
        )
