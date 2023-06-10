from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField ,FieldList, FormField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models.products import Products


class ProductForm(FlaskForm):
    product = SelectField('Product', validators=[DataRequired()], coerce=int)
    quantity = IntegerField('Quantity', validators=[DataRequired()])


class PurchaseForm(FlaskForm):
    supplier = StringField('Supplier', validators=[DataRequired()])
    products = FieldList(FormField(ProductForm), min_entries=1)
    submit = SubmitField('Create Purchase Order')

    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)
        products = Products.query.all()

        for field in self.products:
            field.product.choices = [(p.id, p.product_name) for p in products]


    