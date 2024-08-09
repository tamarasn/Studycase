from odoo import models, fields, api

class TrainSchedule(models.Model):
    _name = 'train.schedule'
    _description = 'Train Schedule'

    code = fields.Char(string='Code', required=True, readonly=True, default=lambda self: self._get_default_code())
    origin = fields.Many2one('train.station', string='Origin', required=True)
    destination = fields.Many2one('train.station', string='Destination', required=True)
    schedule_time = fields.Datetime(string='Schedule Time', required=True)
    duration = fields.Float(string='Duration', required=True)
    arrival_time = fields.Datetime(string='Arrival Time', compute='_compute_arrival_time')
    train_id = fields.Many2one('train.train', string='Train', required=True)
    capacity = fields.Integer(related='train_id.capacity', string='Capacity', readonly=True)

    @api.model
    def _get_default_code(self):
        return self.env['ir.sequence'].next_by_code('train.schedule')

    @api.depends('schedule_time', 'duration')
    def _compute_arrival_time(self):
        for record in self:
            if record.schedule_time and record.duration:
                record.arrival_time = record.schedule_time + timedelta(hours=record.duration)
