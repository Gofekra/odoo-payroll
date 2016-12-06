# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2016- Vertel AB (<http://vertel.se>).
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
{
'name': 'Payroll Contract Hour Salary',
'version': '0.1',
'summary': 'Extends contract with rules for Hour Salary',
'category': 'hr',
'description': """Extends contract with rules for Hour Salary using benefits for hour rate
    Uses benefit hour_salary for salary calculation

""",
'author': 'Vertel AB',
'website': 'http://www.vertel.se',
'depends': ['hr_contract_work_time','hr_payroll_benefit'],
'data': ['hr_salary_rule_data.xml'],
'installable': True,
}
