from odoo import models, fields

class TrainStation(models.Model):
    _name = 'train.station'
    _description = 'Train Station'

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Name', required=True)
    city_id = fields.Many2one('train.city', string='City', required=True)
    address = fields.Text(string='Address')
