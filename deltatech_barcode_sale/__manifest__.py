# -*- coding: utf-8 -*-
# ©  2008-2018 Deltatech
#              Dorin Hongu <dhongu(@)gmail(.)com
# See README.rst file on addons root folder for license details

{
    "name": "Deltatech Barcode Sale",
    'version': '11.0.1.0.0',
    "author": "Terrabit, Dorin Hongu",
    "website": "www.terrabit.ro",

    'category': 'Sales',

    "depends": ["sale",'barcodes'],

    "description": """
Features:    
 - Add product to the sale order using barcode scanner
 
""",
    "data": [
        'views/sale_views.xml'
    ],
    "active": False,
    "installable": True,

}
