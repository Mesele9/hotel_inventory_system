from flask import Blueprint
from flask import render_template, url_for, redirect, request, flash
from app.dbcon import db
from flask_login import login_required
from app.manage_product.form import NewProductForm, EditProductForm

product_bp = Blueprint('product_bp', __name__, url_prefix='/products')


from app.models.products import Products

@product_bp.route('/')
@login_required
def index():
    products = Products.query.all()    
    return render_template('products/products_list.html', title='Product List', products=products)


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
        
    return render_template('products/add_product.html', title='Add Product', form=form)


@product_bp.route('/editproduct/<int:product_id>', methods=('GET', 'POST'))
@login_required
def editproduct():
    form = EditProductForm()
    if form.validate_on_submit():
        product_name = form.product_name.data
        current_user.username = form.username.data
        current_user.role = form.role.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users_bp.account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.username.data = current_user.username
        form.role.data = current_user.role

    return render_template('users_auth/account.html', title='Edit User Account', form=form)

