
from flask import Blueprint
from flask import render_template, url_for, request, redirect, flash
from app.dbcon import db
from flask_login import login_required
from app.models.purchase import ProductPurchaseOrder, PurchaseOrder
from app.manage_purchase.form import NewPurchaseOrderForm, ProductForm



purchase_bp = Blueprint('purchase_bp', __name__, url_prefix='/purchase')


@purchase_bp.route('/')
@login_required
def purchase_list():
    purchase_orders = PurchaseOrder.query.all()
    return render_template('purchase/purchase_list.html', title='Purchase List', purchase_orders=purchase_orders)
    

@purchase_bp.route('/create_purchase_order', methods=('GET', 'POST'))
@login_required
def create_purchase_order():
    form = NewPurchaseOrderForm()
    if form.validate_on_submit():
        # create the purchase order instance
        purchase_order = PurchaseOrder(
            order_date = form.order_date.data,
            created_by = form.created_by.data, 
            supplier = form.supplier.data,
            status = form.status.data 
        )
        # Add products to the purchase order
        for product_form in form.products:
            product_purchase_order = ProductPurchaseOrder(
                product_id = product_form.product_id.data,
                quantity = product_form.quantity.data 
            )
            purchase_order.products.append(product_purchase_order)

        # save the order to the database
        db.session.add(purchase_order)
        db.session.commit()

        flash('Purchase Order{} created successfully'.format(purchase_order.id))
        return redirect(url_for('index'))
    
    return render_template('/purchase/new_purchase.html', title='Create Purchase Order', form=form)