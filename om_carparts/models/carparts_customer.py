from odoo import api, fields, models

class Car_Customer(models.Model):
    # a database with this name will be created in Postgress
    _name = "car.customer"
    # a simple description of the class
    _description = "Details of all the customers buying spare parts in the database."

    # Table columns
    car_customer_name = fields.Char(string='Customer Name: ')
    car_customer_age = fields.Integer(string='Customer Age: ')
    car_customer_ride = fields.Many2one('car.details', string='Customer Car')