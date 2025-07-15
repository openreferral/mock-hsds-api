#!/usr/bin/env python3

# TODO license and authorship goes here

from flask import Flask, jsonify, request, make_response
import json
from pathlib import Path

app = Flask(__name__)


# ===================================================
# Helper functions
# 
# These functions reduce code duplication
# ===================================================


def build_page_from_contents(contents):
    """
    Returns a HSDS API Page object from a list of contents
    """

    page = {}

    if len(contents) == 0:
        page["empty"] = True
    else:
        page["empty"] = False
        page["total_items"] = len(contents)
        page["page_number"] = 1
        page["size"] = len(contents)
        page["contents"] = contents

    return page

def get_all_json_file_contents_from_directory(directory):
    """
    Given a directory, will return the contents of all the JSON files in a dict
    """

    contents = []

    directory = Path(directory)

    for filepath in directory.glob('*.json'):
        contents.append(json.loads(filepath.read_text()))

    return contents

def get_file_contents_from_uuid_in_directory(uuid, directory):
    """
    Given a uuid representing an object, and a directory, find that file and return its contents as a dict
    """

    file_location = f"{directory}/{uuid}.json"
    filepath = Path(file_location)

    if filepath.exists():
        return json.loads(filepath.read_text())
    else:
        return None


 
# ===================================================
# Routes
# 
# Add various routes here to add them to the mock API
# ===================================================


# ------------------------
# Required Endpoints
# These endpoints are required by the spec
# http://docs.openreferral.org/en/latest/hsds/api_reference.html
# ------------------------

# GET /
@app.route('/', methods=['GET'])
def get_api_root_object():

    with open('data/root.json', 'r') as api_response:
        return jsonify(json.loads(api_response.read()))


# GET /services
@app.route('/services', methods=['GET'])
def get_all_services():

    services = get_all_json_file_contents_from_directory("data/services")

    page = build_page_from_contents(services)

    return jsonify(page)

# GET /services/{id}
@app.route('/services/<uuid:service_id>', methods=['GET'])
def get_service(identifier):

    content = get_file_contents_from_uuid_in_directory(identifier, "data/services")

    if content is not None:
        return jsonify(service)
    else:
        return make_response("Item Not Found", 404)

# ------------------------
# Optional Endpoints
# These endpoints are NOT required by the spec
# http://docs.openreferral.org/en/latest/hsds/api_reference.html
# ------------------------

# GET /taxonomies
@app.route('/taxonomies', methods=['GET'])
def get_all_taxonomies():

    contents = get_all_json_file_contents_from_directory("data/taxonomies")

    page = build_page_from_contents(contents)

    return jsonify(page)

# GET /taxonomies/{id}
@app.route('/taxonomies/<uuid:identifier>', methods=['GET'])
def get_taxonomy(identifier):

    content = get_file_contents_from_uuid_in_directory(identifier, "data/taxonomies")

    if content is not None:
        return jsonify(content)
    else:
        return make_response("Item Not Found", 404)

# GET /taxonomy_terms
@app.route('/taxonomy_terms', methods=['GET'])
def get_all_taxonomy_terms():

    contents = get_all_json_file_contents_from_directory("data/taxonomy_terms")

    page = build_page_from_contents(contents)

    return jsonify(page)

# GET /taxonomy_terms/{id}
@app.route('/taxonomy_terms/<uuid:identifier>', methods=['GET'])
def get_taxonomy_term(identifier):

    content = get_file_contents_from_uuid_in_directory(identifier, "data/taxonomy_terms")

    if content is not None:
        return jsonify(content)
    else:
        return make_response("Item Not Found", 404)

# GET /organizations
@app.route('/organizations', methods=['GET'])
def get_all_organizations():

    contents = get_all_json_file_contents_from_directory("data/organizations")

    page = build_page_from_contents(contents)

    return jsonify(page)

# GET /organizations/{id}
@app.route('/organizations/<uuid:identifier>', methods=['GET'])
def get_organization(identifier):

    content = get_file_contents_from_uuid_in_directory(identifier, "data/organizations")

    if content is not None:
        return jsonify(content)
    else:
        return make_response("Item Not Found", 404)

# GET /service_at_locations
@app.route('/service_at_locations', methods=['GET'])
def get_all_service_at_locations():

    contents = get_all_json_file_contents_from_directory("data/service_at_locations")

    page = build_page_from_contents(contents)

    return jsonify(page)

# GET /service_at_locations/{id}
@app.route('/service_at_locations/<uuid:identifier>', methods=['GET'])
def get_service_at_location(identifier):

    content = get_file_contents_from_uuid_in_directory(identifier, "data/service_at_locations")

    if content is not None:
        return jsonify(content)
    else:
        return make_response("Item Not Found", 404)


# ===================================================
# Entry point
# 
# This is the application entry point
# ===================================================

if __name__ == '__main__':
    app.run(debug=True)
