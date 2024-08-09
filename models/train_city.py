from odoo import models, fields

class TrainCity(models.Model):
    _name = 'train.city'
    _description = 'Train City'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
