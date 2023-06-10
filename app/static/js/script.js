// JavaScript code for dynamically adding/removing product fields
document.addEventListener('DOMContentLoaded', function() {
	var addProductButton = document.getElementById('add-product');
	var productsContainer = document.getElementById('products-container');
	var productEntry = document.querySelector('.product-entry');
	var productIndex = 0;

	addProductButton.addEventListener('click', function() {
		var clone = productEntry.cloneNode(true);
		var productFields = clone.querySelectorAll('input, select');

		productFields.forEach(function(field) {
			field.setAttribute('name', field.getAttribute('name').replace('products-0', 'products-' + productIndex));
		});

		clone.querySelector('.remove-product').addEventListener('click', function() {
			this.parentNode.remove();
		});

		productsContainer.appendChild(clone);
		productIndex++;
	});
});                                                                                             
