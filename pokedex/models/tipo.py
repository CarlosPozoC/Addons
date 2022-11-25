from odoo import models, fields, api

class tipo(models.Model):
    _name='pokedex.tipo'
    _description='Registra los tipo/os de un pokemon'
    name= fields.Char(string="Tipo/os del pokemon",required=True)
    description=fields.Text(string="Contien una breve descripcion de los tipos del pokemon")