import datetime
import unittest
from unittest.mock import patch
from space_travel import Planet


class PlanetTests(unittest.TestCase):

    @patch('space_travel.datetime')
    def test_get_correct_age_on_mercury(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        mercury = Planet(planet_name='Mercury', days_in_year=88)
        years, days = mercury.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(153, years)
        self.assertEqual(81, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_venus(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        venus = Planet(planet_name='Earth', days_in_year=225)
        years, days = venus.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(60, years)
        self.assertEqual(45, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_earth(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        earth = Planet(planet_name='Earth', days_in_year=365)
        years, days = earth.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(37, years)
        self.assertEqual(40, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_mars(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        mars = Planet(planet_name='Mars', days_in_year=686)
        years, days = mars.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(19, years)
        self.assertEqual(511, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_jupiter(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        jupiter = Planet(planet_name='jupiter', days_in_year=4329)
        years, days = jupiter.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(3, years)
        self.assertEqual(558, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_saturn(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        saturn = Planet(planet_name='Saturn', days_in_year=10753)
        years, days = saturn.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(1, years)
        self.assertEqual(2792, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_uranus(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        uranus = Planet(planet_name='Uranus', days_in_year=30664)
        years, days = uranus.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(0, years)
        self.assertEqual(13545, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_neptune(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        neptune = Planet(planet_name='Neptune', days_in_year=60148)
        years, days = neptune.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(0, years)
        self.assertEqual(13545, days)

    @patch('space_travel.datetime')
    def test_get_correct_age_on_pluto(self, mock_datetime):
        test_now = datetime.datetime(2019, 9, 1)
        mock_datetime.now.return_value = test_now
        pluto = Planet(planet_name='Earth', days_in_year=90735)
        years, days = pluto.get_age(_birth_date=datetime.datetime(1982, 8, 1))
        self.assertEqual(0, years)
        self.assertEqual(13545, days)