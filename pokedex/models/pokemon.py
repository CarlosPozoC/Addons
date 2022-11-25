from odoo import models, fields, api

class pokemon(models.Model):
    _name='pokedex.pokemon'
    _description='Permite dar una descripcion breve de un pokemon'
    _inherit='pokedex.base'
    
    
    name = fields.Char(string='Nombre del pokemon', required=True)
    description = fields.Text(string='Descripcion del pokemon')
    tipo_ids=fields.Many2many('pokedex.tipo',string="Tipo")