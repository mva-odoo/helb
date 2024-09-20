from odoo import models, fields


class Session(models.Model):
    _name = "openacademy.session"
    _description = "Session"

    name = fields.Char(required=True)
    date_start = fields.Date(required=True)
    date_stop = fields.Date(required=True)
    teacher_id = fields.Many2one('openacademy.person')
    student_ids = fields.Many2many('openacademy.person')
    rate = fields.Integer()
    course_id = fields.Many2one('openacademy.course')
