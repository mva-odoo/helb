from odoo import models, fields


class Course(models.Model):
    _name = "openacademy.person"
    _description = "Person"

    name = fields.Char(required=True)
    birthday_date = fields.Date()
