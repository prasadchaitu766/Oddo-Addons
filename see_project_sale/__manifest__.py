# -*- coding: utf-8 -*-

{
    'name'        : 'Sales Order On Project',
    'author'      : 'Adgensee',
    'category'    : 'Sales',
    'summary'     : 'Sales Order On Project',
    'website'     : 'https://www.adgensee.com',
    'license'     : 'AGPL-3',
    'description' : """  """,
    'version'     : '0.1',
    'depends'     : ['base','sale','project'],
    'data'        : [
                    'views/sale_order_view.xml',
                    'views/project_view.xml',
                    ],
    'images': ['static/description/banner.png'],
    'installable' : True,
    'auto_install': False,
    'application' : True,
}
