from odoo import api, fields, models

class Spare_Parts(models.Model):
    # a database with this name will be created in Postgress
    _name = "spare.parts"
    # a simple description of the class
    _description = "Details of all the spare parts in the database."

    # Table columns
    part_name = fields.Char(string='Part Name')
    part_ride = fields.Many2one('car.details', string='Concerned Car')
    part_category = fields.Selection([('tyre', 'Tyre'), ('mirror', 'Mirror')], string='Part Category')