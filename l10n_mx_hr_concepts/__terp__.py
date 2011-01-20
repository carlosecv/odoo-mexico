# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: nhomar@openerp.com.ve,
#    Planified by: Nhomar Hernandez
#    Finance by: Cli-Per
#    Audited by: Alejandro Negrin alejandro@openerpmexico.com
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################
{
    "name" : "OpenERP Hr Concepts",
    "version" : "0.1",
    "depends" : ["base","hr","product","account"],
    "author" : "OpenERP Venezuela",
    "description" : """
    What do this module:
    Create model to improve RRHH payment on OpenERP.
    Load all concepts related to RRHH in mexico.
                    """,
    "website" : "http://openerp.com.ve",
    "category" : "Localisation/Hr",
    "init_xml" : [
    ],
    "demo_xml" : [
    ],
    "update_xml" : [
        "product_hr_data.xml",
        "product_hr_view.xml",
    ],
    "active": False,
    "installable": True,
}