destinations = [
        "Paris, France",
        "Shanghai, China",
        "Los Angeles, USA",
        "São Paulo, Brazil",
        "Cairo, Egypt",
    ]

def get_destination_index(destination: str) -> int:
        """Return the array index of the given destination"""
        return destinations.index(destination)

def get_travaler_location(traveler: str) -> int:
     """Returns the array index of the traveler's destination"""
     traveler_destination = traveler[1]
     return get_destination_index(traveler_destination)


def main():
    pass

    

if __name__ == "__main__":
    main()