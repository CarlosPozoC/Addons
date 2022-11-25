from odoo import models, fields, api

class base(models.Model):
    _name = 'pokedex.base'
    _description = 'Clase base para que hereden el resto'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')