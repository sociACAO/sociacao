#coding: utf-8

from django.test import TestCase
from action.models import Action, Venue


class ActionModelTestCase(TestCase):
    def test_action_should_have_title(self):
        self.assert_field_in('title', Action)

    def test_action_should_have_description(self):
        self.assert_field_in('description', Action)

    def test_action_should_have_date(self):
        self.assert_field_in('date', Action)

    def test_action_should_have_due_to(self):
        self.assert_field_in('due_to', Action)

    def assert_field_in(self, field_name, model):
        self.assertIn(field_name, model._meta.get_all_field_names())


class VenueModelTestCase(TestCase):
    def test_venue_should_have_address(self):
        self.assert_field_in('address', Venue)

    def test_venue_should_have_number(self):
        self.assert_field_in('number', Venue)

    def test_venue_should_have_district(self):
        self.assert_field_in('district', Venue)

    def test_venue_should_have_city(self):
        self.assert_field_in('city', Venue)

    def test_venue_should_have_state(self):
        self.assert_field_in('state', Venue)

    def test_venue_should_have_latitude(self):
        self.assert_field_in('latitude', Venue)

    def test_venue_should_have_longitude(self):
        self.assert_field_in('longitude', Venue)

    def assert_field_in(self, field_name, model):
        self.assertIn(field_name, model._meta.get_all_field_names())
