# -*- coding: utf-8 -*-
#
# tw2.recaptcha2.widgets - TW2 widget for reCAPTCHA v2.0
#
# Copyright © 2017 Nils Philippsen <nils@tiptoe.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from tw2.core import Widget, Param

from .resources import recaptcha2_js


class ReCaptcha2Widget(Widget):

    resources = [recaptcha2_js]

    template = 'tw2.recaptcha2.templates.recaptcha2'

    sitekey = Param("Google reCAPTCHA API v2.0 site key", request_local=False,
                    attribute=True, view_name="data-sitekey")

    theme = Param("Theme to use (light, dark)", default=None, attribute=True,
                  view_name="data-theme")

    captcha_type = Param("Type of captcha to use (image, audio)", default=None,
                         attribute=True, view_name="data-type")
    size = Param("Size of Captcha (normal, compact)", default=None,
                 attribute=True, view_name="data-size")
    tabindex = Param("Optional tabindex of the widget", default=None, attribute=True,
                     view_name="data-tabindex")
    callback = Param("Name of optional callback to execute when the user submits a "
                     "successful CAPTCHA response", default=None,
                     attribute=True, view_name="data-callback")
    expired_callback = Param("Name of optional callback to execute when the recaptcha "
                             "response expires and the user needs to solve a new CAPTCHA",
                             default=None, attribute=True,
                             view_name="data-expired-callback")

    def prepare(self):
        if self.theme not in (None, 'light', 'dark'):
            raise ValueError("Theme must be 'light' or 'dark'")
        if self.captcha_type not in (None, 'image', 'audio'):
            raise ValueError("CAPTCHA type must be 'image' or 'audio'")
        if self.size is not None and not (isinstance(self.size, int) and
                                          self.size > 0):
            raise ValueError("Tabindex must be a positive integer")
        if self.css_class:
            classes = self.css_class.split()
            if 'g-recaptcha' not in classes:
                classes.append('g-recaptcha')
                self.safe_modify('css_class')
                self.css_class = " ".join(classes)

        super(ReCaptcha2Widget, self).prepare()
