# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    partner_cc_to_ids = fields.Many2many(
        comodel_name='res.partner',
        related='partner_id.invoice_cc_ids',
    )

    @api.multi
    def invoice_validate(self):
        for rec_id in self:
            rec_id.message_subscribe([p.id for p in rec_id.partner_cc_to_ids])
        return super(AccountInvoice, self).invoice_validate()
