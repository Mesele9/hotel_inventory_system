from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from flask_login import current_user



class NewProductForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    product_category = SelectField('Product Category', choices=[('', 'Product Category'), ('food', 'Food'), ('beverage', 'Beverage'), ('house_keeping', 'House Keeping'), ('stationary', 'Stationary')], validators=[DataRequired()])
    uom = SelectField('UOM', choices=[('', 'Unit of Measurment'), ('g', 'Gram'), ('kg', 'Kilo Gram'), ('bottle', 'Bottle'), ('liter', 'Liter'), ('crate', 'Crate'), ('pack', 'Pack'), ('piece', 'Piece')], validators=[DataRequired()])
    unit_price = FloatField('Unit Price', validators=[DataRequired(), NumberRange(min=0)])
    quantity = IntegerField('Available Quantity', validators=[DataRequired()])
    reorder_level = IntegerField('Reorder Level', validators=[DataRequired()])
    submit = SubmitField('Add Product')

    def validate_product_name(self, product_name):
        from app.models.products import Products
        product = Products.query.filter_by(product_name=product_name.data).first()
        if product:
            raise ValidationError('Product already exist!')


class EditProductForm(FlaskForm):
    product_name = StringField('Product Name', validators=[DataRequired()])
    product_category = SelectField('Product Category', choices=[('', 'Product Category'), ('food', 'Food'), ('beverage', 'Beverage'), ('house_keeping', 'House Keeping'), ('stationary', 'Stationary')], validators=[DataRequired()])
    uom = SelectField('UOM', choices=[('', 'Unit of Measurment'), ('g', 'Gram'), ('kg', 'Kilo Gram'), ('bottle', 'Bottle'), ('liter', 'Liter'), ('crate', 'Crate'), ('pack', 'Pack'), ('piece', 'Piece')], validators=[DataRequired()])
    unit_price = FloatField('Unit Price', validators=[DataRequired(), NumberRange(min=0)])
    quantity = IntegerField('Available Quantity', validators=[DataRequired()])
    reorder_level = IntegerField('Reorder Level', validators=[DataRequired()])
    submit = SubmitField('Update')


    def validate_product_name(self, product_name):
        from app.models.products import Products
        product = Products.query.filter_by(product_name=product_name.data).first()
        if product_name.data != product.product_name:
            raise ValidationError('Product already exist!')