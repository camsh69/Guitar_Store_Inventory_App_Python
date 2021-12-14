from enum import unique
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.manufacturers_controller import manufacturers
from models.product import Product
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

products_blueprint = Blueprint("books", __name__)


@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    # retrieves list of categories from all products
    categories = product_repository.category_list(products)
    # removes duplicates from list of categories
    unique_categories = list(dict.fromkeys(categories))
    # retrieves list of manufacturers from all products
    manufacturers = manufacturer_repository.manufacturers_list(products)
    # removes duplicates from list of manufacturers
    unique_manufacturers = list(dict.fromkeys(manufacturers))
    return render_template("products/index.html", title="Products", all_products=products, unique_categories=unique_categories, unique_manufacturers=unique_manufacturers)


@products_blueprint.route("/products/new")
def new_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/products/new.html", all_manufacturers=manufacturers, title="Add New Product")


@products_blueprint.route("/products/new", methods=['POST'])
def create_product():
    item = request.form['item']
    description = request.form['description']
    category = request.form['category']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    manufacturer = manufacturer_repository.select(
        request.form['manufacturer_id'])
    product = Product(item, description, category, stock_quantity,
                      buying_cost, selling_price, manufacturer)
    product_repository.save(product)
    return redirect("/products")


@products_blueprint.route("/products/<id>")
def show_product(id):
    product = product_repository.select(id)
    return render_template('products/show.html', title="View Product", product=product)


@products_blueprint.route("/products/<id>/edit")
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/edit.html", title="Edit Product", product=product, all_manufacturers=manufacturers)


@products_blueprint.route("/products/<id>/edit", methods=['POST'])
def update_product(id):
    product = product_repository.select(id)
    item = request.form['item']
    description = request.form['description']
    category = request.form['category']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    manufacturer = manufacturer_repository.select(
        request.form['manufacturer_id'])
    product = Product(item, description, category, stock_quantity,
                      buying_cost, selling_price, manufacturer, id)
    product_repository.update(product)
    return redirect("/products")


@products_blueprint.route("/products/<id>/delete")
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')
