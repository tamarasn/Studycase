from odoo import models, fields, api

class TrainScheduleWizard(models.TransientModel):
    _name = 'train.schedule.wizard'
    _description = 'Train Schedule Wizard'

    train_id = fields.Many2one('train.train', string='Train', required=True)
    schedule_ids = fields.One2many('train.schedule.line', 'wizard_id', string='Schedules')

    @api.multi
    def action_create_schedules(self):
        for wizard in self:
            for schedule in wizard.schedule_ids:
                schedule.copy(default={'train_id': wizard.train_id.id})
