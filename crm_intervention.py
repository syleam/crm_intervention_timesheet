# -*- coding: utf-8 -*-
##############################################################################
#
#    crm_intervention_timesheet module for OpenERP, CRM Intervention Timesheet
#    Copyright (C) 2011 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sebastien LANGE <sebastien.lange@syleam.fr>
#
#    This file is a part of crm_intervention_timesheet
#
#    crm_intervention_timesheet is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    crm_intervention_timesheet is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields


class crm_intervention(models.Model):
    _inherit = 'crm.intervention'
    _name = "crm.intervention"

    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account', ondelete='cascade')
    timesheet_ids = fields.One2many('account.analytic.line', 'intervention_id', 'Timesheet', default=False)

crm_intervention()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
