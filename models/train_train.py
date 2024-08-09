from odoo import models, fields

class TrainTrain(models.Model):
    _name = 'train.train'
    _description = 'Train'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    capacity = fields.Integer(string='Capacity', required=True)
    state = fields.Selection([
        ('ready', 'Ready'),
        ('not_ready', 'Not Ready'),
        ('maintenance', 'Maintenance')
    ], string='State', default='ready')
    active = fields.Boolean(string='Active', default=True)
    schedule_line_ids = fields.One2many('train.schedule.line', 'train_id', string='Schedule Line')
