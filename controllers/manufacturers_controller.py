from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturer", __name__)


@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", title="List of Manufacturers", all_manufacturers=manufacturers)


@manufacturers_blueprint.route("/manufacturers/new")
def new_manufacturer():
    return render_template("/manufacturers/new.html")


@manufacturers_blueprint.route("/manufacturers/new", methods=['POST'])
def create_manufacturer():
    name = request.form['name']
    is_active = request.form['is_active']
    manufacturer = Manufacturer(name, is_active)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')


@manufacturers_blueprint.route("/manufacturers/<id>")
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("/manufacturers/show.html", manufacturer=manufacturer)


@manufacturers_blueprint.route("/manufacturers/<id>/edit")
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturers/edit.html", manufacturer=manufacturer)


@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['POST'])
def update_manufacturer(id):
    name = request.form['name']
    is_active = request.form['is_active']
    manufacturer = Manufacturer(name, is_active, id)
    manufacturer_repository.update(manufacturer)
    return redirect("/manufacturers")
