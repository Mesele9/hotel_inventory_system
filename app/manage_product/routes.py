from flask import Blueprint
from flask import render_template, url_for, redirect, request, flash
from app.dbcon import db
from flask_login import login_required, current_user
from app.manage_product.form import NewProductForm

product_bp = Blueprint('product_bp', __name__, url_prefix='/products')


from app.models.products import Products

@product_bp.route('/')
@login_required
def products_list():
    products = Products.query.all()    
    return render_template('products/products_list.html', title='Products List', products=products)


@product_bp.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    form = NewProductForm()
    if form.validate_on_submit():
        new_product = Products(product_name=form.product_name.data, product_category=form.product_category.data, uom=form.uom.data, unit_price=form.unit_price.data, quantity=form.quantity.data, reorder_level=form.reorder_level.data)
        db.session.add(new_product)
        db.session.commit()
        flash('Product: {} added to the database!'.format(form.product_name.data), 'success')
        return redirect(url_for('product_bp.add_product'))
        
    return render_template('products/add_product.html', title='Add Product', form=form, legend='Add New Product')


@product_bp.route('/<int:id>', methods=('GET', 'POST'))
@login_required
def products(id):
    product = Products.query.filter_by(id=id).first()
    return render_template('products/product.html', title='Product Detail', product=product)    
   

@product_bp.route('/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit_products(id):
    product = Products.query.filter_by(id=id).first()
    if current_user.role != 'store_keeper' and current_user.role !='admin':
        flash('Action not allowed!')
        return redirect(url_for('index'))
    form = NewProductForm()
    if form.validate_on_submit():
        product.product_name = form.product_name.data
        product.product_category = form.product_category.data
        product.uom = form.uom.data
        product.unit_price = form.unit_price.data
        product.quantity = form.quantity.data
        product.reorder_level = form.reorder_level.data
        db.session.commit()
        flash('Product: {} has been updated!'.format(form.product_name.data), 'success')
        return redirect(url_for('product_bp.products', id=product.id))
    
    elif request.method == 'GET':
        form.product_name.data = product.product_name
        form.product_category.data = product.product_category
        form.uom.data = product.uom
        form.unit_price.data = product.unit_price
        form.quantity.data = product.quantity
        form.reorder_level.data = product.reorder_level
    return render_template('products/add_product.html', title='Edit Product', form=form, legend='Edit Product')