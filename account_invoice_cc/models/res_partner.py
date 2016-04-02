# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    invoice_cc_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='rel_model_res_partner_invoice_cc_res_partner',
        inverse_name='invoice_ccd_on_ids',
        column1='rel_invoice_cc_ids',
        column2='rel_invoice_ccd_on_ids',
        string='Automatic Invoice Followers',
        help='CC These Users When Invoicing',
    )
    invoice_ccd_on_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='rel_model_res_partner_invoice_cc_res_partner',
        inverse_name='invoice_cc_ids',
        column1='rel_invoice_ccd_on_ids',
        column2='rel_invoice_cc_ids',
        string='CCd By',
        help='CCd On Invoices By These Users',
    )
