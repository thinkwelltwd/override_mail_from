# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2015 Therp BV <http://therp.nl>.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Override mail from reply-to",
    "version": "10.0.1.0.0",
    "author": "Therp BV, Stella Fredö",
    "license": "AGPL-3",
    "category": "Tools",
    "summary":
    "Allows you to override all mail sender (from and reply-to) in case you need to use smtp server",
    "depends": [
        'base'
    ],
    "data": [
        "data/ir_config_parameter.xml",
        "data/installer.xml",
    ],
}