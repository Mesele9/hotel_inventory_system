from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField ,FieldList, FormField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from flask_login import current_user


class ProductForm(FlaskForm):
    product_id = IntegerField('Product', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])


class NewPurchaseOrderForm(FlaskForm):
    order_date = DateField('Order Date', validators=[DataRequired()])
    created_by = IntegerField('Created By', validators=[DataRequired()])
    supplier = StringField('Supplier')
    status = SelectField('Status', choices=[('created', 'Requested'), ('approved', 'approved'), ('purchased', 'Purchased')], validators=[DataRequired()])
    products = FieldList(FormField(ProductForm), min_entries=1)
    submit = SubmitField('New Purchase Order')

    