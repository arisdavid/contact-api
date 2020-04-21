from flask import url_for
from src.app import create_app
from src.extensions import db
import unittest
import json


class ContactTestCase(unittest.TestCase):
    """ These are the TestCases for Contact API"""

    def setUp(self):
        """ Define test variables and initialize app"""
        params = {
            'DEBUG': False,
            'TESTING': True
        }

        self.app = create_app(settings_override=params)
        self.client = self.app.test_client()

        self.contact = {'username': 'arisdavid3',
                        'firstName': 'Aristotle',
                        'lastName': 'David'}

        # binds the app to the current context
        with self.app.app_context():
            db.create_all()

    def test_add_contact_api_success(self):

        """ Test that we can create a contact (CREATE) """
        res = self.client.post(url_for('api.add_contact'), json=self.contact)
        self.assertEqual(res.status_code, 201)
        self.assertIn('arisdavid3', str(res.data))

    def test_get_contact_by_id_success(self):

        """ Test that we can retrieve a contact by id (READ)"""
        res = self.client.post(url_for('api.add_contact'), json=self.contact)
        self.assertEqual(res.status_code, 201)

        result_in_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
        result = self.client.get(f"{url_for('api.get_contact', id=result_in_json['id'])}")
        self.assertEqual(result.status_code, 200)
        self.assertIn('arisdavid3', str(result.data))

    def test_get_contacts_success(self):

        """ Test we can retrieve all contacts (READ) """
        res = self.client.post(url_for('api.add_contact'), json=self.contact)
        self.assertEqual(res.status_code, 201)

        result = self.client.get(url_for('api.get_contacts'))
        self.assertEqual(result.status_code, 200)
        self.assertIn('arisdavid3', str(result.data))

    def test_update_contact_by_id_success(self):

        """ Test that we can update a contact by id (UPDATE) """
        res = self.client.post(url_for('api.add_contact'), json=self.contact)
        self.assertEqual(res.status_code, 201)

        new_payload = {"username": "floydmayweather",
                       "firstName": "Floyd",
                       "lastName": "Mayweather"}

        result_in_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
        out = self.client.put(f"{url_for('api.update_contact', id=result_in_json['id'])}",
                              json=new_payload)

        self.assertEqual(out.status_code, 200)
        result = self.client.get(f"{url_for('api.get_contact', id=result_in_json['id'])}")
        self.assertIn('Mayweather', str(result.data))

    def test_delete_contact_by_id_success(self):
        """ Test that we can delete a contact by id (DELETE) """
        res = self.client.post(url_for('api.add_contact'), json=self.contact)
        self.assertEqual(res.status_code, 201)

        result_in_json = json.loads(res.data.decode('utf-8').replace("'", "\""))
        result = self.client.delete(f"{url_for('api.delete_contact', id=result_in_json['id'])}")
        self.assertEqual(result.status_code, 200)

        # Test to see if it exists returns 404
        out = self.client.get(f"{url_for('api.get_contact', id=result_in_json['id'])}")
        self.assertEqual(out.status_code, 404)

    def tearDown(self):
        """ Tear down. Don't commit anything from unit test """
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


def test_api_documentation_page(client):
    """ Test the index page responds with 200 """

    response = client.get(url_for('api.api_doc'))
    assert response.status_code == 200
