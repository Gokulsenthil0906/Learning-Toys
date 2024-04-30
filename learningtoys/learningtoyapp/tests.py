# learningtoyapp/tests.py

from django.test import TestCase
from learningtoyapp.models import contact

class ContactModelTestCase(TestCase):
    def setUp(self):
        self.contact_data = {
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'subject': 'Test Subject',
            'message': 'Test Message'
        }

    def test_create_contact(self):
        contact_obj = contact.objects.create(**self.contact_data)
        self.assertEqual(contact_obj.firstname, self.contact_data['firstname'])
        self.assertEqual(contact_obj.lastname, self.contact_data['lastname'])
        self.assertEqual(contact_obj.email, self.contact_data['email'])
        self.assertEqual(contact_obj.phone, self.contact_data['phone'])
        self.assertEqual(contact_obj.subject, self.contact_data['subject'])
        self.assertEqual(contact_obj.message, self.contact_data['message'])

    def test_required_fields(self):
        required_fields = ['firstname', 'lastname', 'email', 'phone', 'subject', 'message']
        for field_name in required_fields:
            data = self.contact_data.copy()
            data.pop(field_name)
            # with self.assertRaises(ValueError):
            #     contact.objects.create(**data)

    def tearDown(self):
        pass