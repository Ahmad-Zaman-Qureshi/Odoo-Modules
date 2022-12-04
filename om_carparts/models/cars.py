from odoo import api, fields, models

class Car_Details(models.Model):
    # a database with this name will be created in Postgress
    _name = "car.details"
    # a simple description of the class
    _description = "Details of all the cars in the database."

    # Table columns
    name = fields.Char(string='Car Model')
    engine = fields.Integer(string='Engine Size: ')
    company = fields.Selection([('honda', 'Honda'), ('toyota', 'Toyota')], string='Company')
    driven = fields.Float(string='Miles Driven')
    car_image = fields.Image(string='Car Image')