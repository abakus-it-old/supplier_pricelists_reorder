{
    'name': "Supplier pricelists reorderer",
    'version': '9.0.1.0',
    'depends': ['product',],
    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Product',
    'description': """
Supplier pricelist reorderer

This modules creates a cron task that will reorder pricelists in products (using seqence) regarding the price for this supplier and the last update date

This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
""",
    'data': [
            'reorderer_cron.xml',
             ],
}
