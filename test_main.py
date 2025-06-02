import pytest
from main import get_destination_index

test_traveler = ["erin Wilkes", "Shanghai, China", ["historical site", "art"]]

class TestClass:
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


