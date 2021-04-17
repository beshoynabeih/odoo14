# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Menu(models.Model):
    _inherit = 'ir.ui.menu'

    def _get_external_id(self):
        for menu in self:
            model_data = self.env['ir.model.data'].search([
                ('res_id', '=', menu.id),
                ('model', '=', self._name)
            ], limit=1)
            if model_data:
                menu.external_id = "%s.%s" % (model_data.module, model_data.name)
            else:
                menu.external_id = ''

    external_id = fields.Char('External ID', compute='_get_external_id')