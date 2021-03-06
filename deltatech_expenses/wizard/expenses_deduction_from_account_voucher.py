# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2008 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com       
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
#
##############################################################################

from odoo import fields, models, api, _



class expenses_deduction_from_account_voucher(models.TransientModel):
    _name = "expenses.deduction.from.account.voucher"
    _description = "Create Expenses Deduction"

    def _get_date_expense(self, cr, uid, context=None):
        if context is None:
            context= {}
        voucher_pool = self.pool.get('account.voucher')
        active_id = context and context.get('active_id', [])
        voucher = voucher_pool.browse(cr,uid, active_id, context)
        return voucher and voucher.date



    date_expense = fields.date('Expense Date', default=_get_date_expense)


    @api.multi
    def create_expenses_deduction(self):
        # trebuie sa citesc datele si sa intru in moul de creare
        data_pool = self.pool.get('ir.model.data')
        voucher_pool = self.pool.get('account.voucher')
        action_model,action_id = data_pool.get_object_reference(cr, uid, 'deltatech_expenses', "action_deltatech_expenses_deduction")
        action_pool = self.pool.get(action_model)
        action = action_pool.read(cr, uid, action_id, context=context)
        res_ids = context and context.get('active_ids', [])
        expenses_pool = self.pool.get('deltatech.expenses.deduction')
        for expense in self.browse(cr, uid, ids,context):
            date_expense = expense.date_expense
        expenses_id = expenses_pool.create(cr, uid, {'date_expense':date_expense}, context )
        voucher_ids = []
        for voucher in voucher_pool.browse(cr,uid, res_ids, context):
            if  not  voucher.expenses_deduction_id:
                voucher_ids.append(voucher.id)
        voucher_pool.write(cr,uid,voucher_ids, {'expenses_deduction_id':expenses_id}, context)
        action['domain'] = "[('id','in', ["+str(expenses_id)+"])]"        
        return action

expenses_deduction_from_account_voucher()


 

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
