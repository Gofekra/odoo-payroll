# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2004-2016 Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _, http, tools
from openerp.http import request
from datetime import datetime, timedelta
import time

import logging
_logger = logging.getLogger(__name__)

class attendanceReport(http.Controller):

    @http.route(['/hr/attendance'], type='http', auth="user", website=True)
    def attendance(self, employees=None, **post):
        return request.website.render("hr_payroll_attendance.hr_attendance_form", {'employees': request.env['hr.employee'].search([('active', '=', True),('id', '!=', request.env.ref('hr.employee').id)]),})

    @http.route(['/hr/attendance/report'], type='json', auth="user", website=True)
    def attendance_report(self, employee=None, **kw):
        state = request.env['hr.employee'].search_read([('id', '=', int(employee))], ['state'])[0]['state']
        return state

    @http.route(['/hr/attendance/come_and_go'], type='json', auth="user", website=True)
    def attendance_comeandgo(self, employee_id=None, **kw):
        employee = request.env['hr.employee'].browse(int(employee_id))
        try:
            employee.attendance_action_change()
        except Exception as e:
            _logger.warn(e)
            return ': '.join(e)
        return None

    @http.route(['/hr/attendance/<model("hr.attendance"):attendance>'], type='json', auth="user", website=True)
    def get_attendance(self, attendance=None, **kw):
        return {'attendance': {
                    'name': attendance.name,
                    'action': attendance.action,
                    'flex_working_hours': attendance.flex_working_hours,
                    'flextime': attendance.flextime,
                },
                'employee': {
                    'img': attendance.employee_id.image_medium,
                    'name': attendance.employee_id.name,
                    'state': attendance.employee_id.state,
                }
            }

    #~ @http.route(['/hr/attendance/source'], type='http', auth="public", website=True)
    #~ def attendance_source(self, employee=None, **post):
        #~ while True:
            #~ employee_login = request.env['hr.employee'].search([('state', '=', 'present')])
            #~ while employee_login - request.env['hr.employee'].search([('state', '=', 'present')]):
                #~ # send to client
                #~ headers=[('Content-Type', 'text/plain; charset=utf-8')]
                #~ r = werkzeug.wrappers.Response(request_id, headers=headers)
                #~ break
        #~ state = request.env['hr.employee'].browse(int(employee)).state
        #~ return state

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
