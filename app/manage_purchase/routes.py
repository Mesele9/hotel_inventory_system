from datetime import datetime
from flask import Blueprint
from flask import render_template, url_for, request, redirect, flash
from app.dbcon import db
from flask_login import login_required, current_user
from app.models.purchase import PurchaseOrder, ProductPurchaseOrder
from app.manage_purchase.form import PurchaseForm, ProductForm


purchase_bp = Blueprint('purchase_bp', __name__, url_prefix='/purchase')



@purchase_bp.route('/')
@login_required
def purchase_list():
    purchase_orders = PurchaseOrder.query.all()
    return render_template('purchase/purchase_list.html', title='Purchase List', purchase_orders=purchase_orders)
    

@purchase_bp.route('/create_purchase_order', methods=('GET', 'POST'))
@login_required
def create_purchase_order():
    print('create purchase order route trigerred')
    form = PurchaseForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            # create the purchase order instance
            purchase_order = PurchaseOrder(created_by=current_user.id, supplier=form.supplier.data)
            db.session.add(purchase_order)
            db.session.commit()
            print(form.data)

            for entry in form.products.entries:
                product_id = entry.form.product.data
                quantity = entry.form.quantity.data

                product_purchase_order = ProductPurchaseOrder(purchase_order_id=purchase_order.id, product_id=product_id, quantity=quantity
                        )
            
                db.session.add(product_purchase_order)
            db.session.commit()

            flash('Purchase Order{} created successfully'.format(purchase_order.id))
            return redirect(url_for('purchase_bp.purchase_list'))
        else:
            print('Form validation error', form.errors)
    
    else:
        return render_template('/purchase/new_purchase.html', title='Create Purchase Order', form=form)
