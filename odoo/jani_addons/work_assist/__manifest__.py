{
    'name': 'Work Assist', 
    'version': '17.0.1.0.0',
    'author': 'sk jani', 
    'category': 'Custom',
    'summary': 'A custom module for learning',
    'depends': ['base'],  # Base module dependency
    'data': [
        'security/ir.model.access.csv',
        'views/my_model_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

}
