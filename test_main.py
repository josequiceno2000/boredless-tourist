import pytest
from main import get_destination_index, get_travaler_location


class TestGetDestinationIndex:
    def test_get_destination_index_one(self):
        destination = "Paris, France"
        assert get_destination_index(destination) == 0
    
    def test_get_destination_index_two(self):
        destination = "Los Angeles, USA"
        assert get_destination_index(destination) == 2
    
    def test_get_destination_index_failure(self):
        destination = "Hyderabad, India"
        with pytest.raises(ValueError):
            get_destination_index(destination)

class TestGetTravelerLocation:
    def test_get_traveler_location_one(self):
        traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]
        assert get_travaler_location(traveler) == 1
    
    def test_get_traveler_location_two(self):
        traveler = ["Clint Barton", "Cairo, Egypt", ["historical site", "art"]]
        assert get_travaler_location(traveler) == 4
    
    def test_get_traveler_location_three(self):
        traveler = ["Sherlock Holmes", "Paris, France", ["historical site", "art"]]
        assert get_travaler_location(traveler) == 0
