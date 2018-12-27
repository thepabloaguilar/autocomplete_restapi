import unittest

from app import create_app

from flask_testing import TestCase


class PatientSearchTest(TestCase):

    def create_app(self):
        return create_app(testing=True)

    def test_empty_query(self):
        '''
        WHEN the `query` is empty
        THEN the return should be an array with all patients' name in
        `patients` attribute, and `patients` length
        for `patients_count` attribute.
        '''
        response = self.client.get('patients/search?q=').json
        self.assertEqual(len(response['patients']), response['patients_count'])
    
    def test_non_query(self):
        '''
        WHEN the `query` isn't given
        THEN the API should be return error code `400 (Bad Request)`
        '''
        response = self.client.get('patients/search')
        self.assert400(response)
    
    def test_prefix_in_results_contains_query(self):
        '''
        WHEN the `query` is correctly given and API returns a non
        empty array on `patients` attribute
        THEN each item in array should contains the `query` as it
        prefix.
        '''
        query = 'ma'
        response = self.client.get(f'patients/search?q={query}').json
        for patient in response['patients']:
            self.assertTrue(patient.lower().startswith(query))
    
    def test_patients_count_equal_patients_list_length(self):
        '''
        WHEN the `query` is correctly given
        THEN the array's length from `patients` attribute should be
        equal to the number from `patients_count` attribute.
        '''
        response = self.client.get('patients/search?q=ma').json
        self.assertEqual(response['patients_count'], len(response['patients']))

if __name__ == '__main__':
    unittest.main()
