import datetime
import unittest
from unittest.mock import patch
from src.space_travel import Planet


class PlanetTests(unittest.TestCase):

    @patch('space_travel.datetime')
    def test_get_correct_age_on_mercury(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        earth = Planet(planet_name='Earth', days_in_year=88)
        years, days = earth.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(154, years)
        self.assertEqual(7, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_venus(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        earth = Planet(planet_name='Earth', days_in_year=225)
        years, days = earth.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(60, years)
        self.assertEqual(59, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_earth(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        earth = Planet(planet_name='Earth', days_in_year=365)
        years, days = earth.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(37, years)
        self.assertEqual(54, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_mars(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        earth = Planet(planet_name='Earth', days_in_year=686)
        years, days = earth.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(19, years)
        self.assertEqual(525, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_jupiter(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        earth = Planet(planet_name='Earth', days_in_year=4329)
        years, days = earth.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(3, years)
        self.assertEqual(572, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_saturn(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        earth = Planet(planet_name='Earth', days_in_year=10753)
        years, days = earth.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(1, years)
        self.assertEqual(2806, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_uranus(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        earth = Planet(planet_name='Earth', days_in_year=30664)
        years, days = earth.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(0, years)
        self.assertEqual(13559, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_neptune(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        earth = Planet(planet_name='Earth', days_in_year=60148)
        years, days = earth.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(0, years)
        self.assertEqual(13559, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_pluto(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        earth = Planet(planet_name='Earth', days_in_year=90735)
        years, days = earth.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(0, years)
        self.assertEqual(13559, days)