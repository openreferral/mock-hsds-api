HSDS Mock API
=================

This is a very basic Mock API for testing tooling related to the [HSDS Specification](https://docs.openreferral.org).

## How it works

You provide HSDS data as JSON files inside the `data/` directory, divided up by different schema type. You just need to provide files containing individual services, organizations, taxonomies etc. where the file name is the UUID of that object, and the script will handle the rest.

Example: the `service` object with UUID `ac148810-d857-441c-9679-408f346de14b` should be stored as the file `data/services/ac148810-d857-441c-9679-408f346de14b.json`

The Mock API will handle retrieving lists of objects for you and build the `Page` schema required by the HSDS API Specification, so all you need to do is provide the JSON files representing your objects to mock an API setup.

## Running the application

1. Set up the Python virtual environment:

```bash
python3 -m venv .ve
source .ve/bin/activate
```
2. Install the dependencies into the environment

```bash
pip install -r requirements.txt
```

3. Run the application `./app.py`

## Limitations

### No support for parameters

There is currently no support for parameters in the Mock API on any endpoint

### Large datasets may cause you to run out of memory

This tool is designed to mock up a basic API with some data for you to test HSDS tools against an API. It doesn't attempt to paginate or stream any data, and naïvely puts responses in a single `page` object. This means if you dump 4000 services into the `data/services/` directory, the mock API will respond to `GET /services` by giving you a single page of 4000 services!
