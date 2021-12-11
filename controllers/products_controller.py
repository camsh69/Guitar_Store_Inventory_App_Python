from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

products_blueprint = Blueprint("books", __name__)


@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", title="Products", all_products=products)


@products_blueprint.route('/products/new')
def new_product():
    manufacturers = manufacturer_repository.select_all
    return render_template("/products/new.html", all_manufacturers=manufacturers)
