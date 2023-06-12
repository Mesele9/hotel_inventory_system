from datetime import datetime
from flask import Blueprint
from flask import render_template, url_for, request, redirect, flash
from app.dbcon import db
from flask_login import login_required, current_user
from app.models.purchase import PurchaseOrder, ProductPurchaseOrder
from app.manage_purchase.form import PurchaseForm, ProductForm, EditPurchaseForm
from app.models.products import Products


purchase_bp = Blueprint('purchase_bp', __name__, url_prefix='/purchase')


@purchase_bp.route('/')
@login_required
def purchase_list():
    purchase_orders = PurchaseOrder.query.all()
    return render_template('purchase/purchase_list.html', title='Purchase List', purchase_orders=purchase_orders)
    

@purchase_bp.route('/create_purchase_order', methods=('GET', 'POST'))
@login_required
def create_purchase_order():
    form = PurchaseForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            # create the purchase order instance
            purchase_order = PurchaseOrder(created_by=current_user.id, supplier=form.supplier.data, status=form.status.data)
            db.session.add(purchase_order)
            db.session.commit()    
            for entry in form.products.entries:
                if entry.form.product.data:
                    product_id = entry.form.product.data
                    quantity = entry.form.quantity.data

                    product_purchase_order = ProductPurchaseOrder(
                        purchase_order_id=purchase_order.id,
                        product_id=product_id,
                        quantity=quantity
                        )
                    
                    db.session.add(product_purchase_order)
                   
        
            db.session.commit()

            flash('Purchase Order{} created successfully'.format(purchase_order.id))
            return redirect(url_for('purchase_bp.purchase_list'))
        else:
            print('Form validation error', form.errors)
    
    else:
        return render_template('/purchase/new_purchase.html', title='Create Purchase Order', form=form)


@purchase_bp.route('/<int:id>', methods=('GET', 'POST'))
@login_required
def product_purchase_order(id):
    products_purchase = ProductPurchaseOrder.query.filter_by(id=id).first()
    product = Products.query.filter_by(id=products_purchase.product_id).first()
    return render_template('purchase/purchase_detail.html', title='Purchase Order Detail', products_purchase=products_purchase, product=product)    


@purchase_bp.route('/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit_purchase_order(id):
    purchase_order = PurchaseOrder.query.filter_by(id=id).first()
    if current_user.role != 'manager' and current_user.role !='admin':
        flash('Action not allowed!')
        return redirect(url_for('index'))
    form = EditPurchaseForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # update the purchase order instance
            purchase_order.supplier = form.supplier.data
            purchase_order.status = form.status.data
            db.session.commit()
            flash('Purchase Order {} status has been changed to {}'.format(purchase_order.id, purchase_order.status), 'success')
            product_purchase_order = ProductPurchaseOrder.query.filter_by(id=purchase_order.id).first()
            if purchase_order.status == 'purchased':
                product = Products.query.filter_by(id=product_purchase_order.product_id).first()
                purchase_quantity = product_purchase_order.quantity
                new_quantity = product.quantity + purchase_quantity
                product.quantity = new_quantity
                db.session.commit()
                flash('{} {} has been purchased'.format(product_purchase_order.quantity, product_purchase_order.product_id), 'success')
                return redirect(url_for('product_bp.products_list'))
            """ purchase_order = PurchaseOrder(created_by=current_user.id, supplier=form.supplier.data, status=form.status.data)
            db.session.add(purchase_order)
            db.session.commit()    
            for entry in form.products.entries:
                if entry.form.product.data:
                    product_id = entry.form.product.data
                    quantity = entry.form.quantity.data

                    product_purchase_order = ProductPurchaseOrder(
                        purchase_order_id=purchase_order.id,
                        product_id=product_id,
                        quantity=quantity
                        )
                    
                    db.session.add(product_purchase_order)
                   
        
            db.session.commit()

            flash('Purchase Order{} created successfully'.format(purchase_order.id)) """
            return redirect(url_for('purchase_bp.product_purchase_order', id=purchase_order.id))
        
    elif request.method == 'GET':
        form.supplier.data = purchase_order.supplier
        form.status.data = purchase_order.status
        
        
    
    return render_template('/purchase/edit_purchase.html', title='Edit Purchase Order', form=form, id=id)


@purchase_bp.route('/<int:id>', methods=('GET', 'POST'))
@login_required
def purchase_order_update(id):

    products_purchase = ProductPurchaseOrder.query.filter_by(id=id).first()
    product = Products.query.filter_by(id=products_purchase.product_id).first()
    return render_template('purchase/purchase_detail.html', title='Purchase Order Detail', products_purchase=products_purchase, product=product) 
    