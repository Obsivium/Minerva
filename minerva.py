import requests
import random

name_data = [
    {
        "link": "https://raw.githubusercontent.com/dariusk/corpora/refs/heads/master/data/materials/gemstones.json",
        "element": "gemstones",
        "extract_func": lambda x: x.split(" ")[-1]
    },
    {
        "link": "https://raw.githubusercontent.com/dariusk/corpora/refs/heads/master/data/mythology/greek_gods.json",
        "element": "greek_gods",
        "extract_func": lambda x: x.split(" ")[-1]
    },
    {
        "link": "https://raw.githubusercontent.com/dariusk/corpora/refs/heads/master/data/mythology/roman_deities.json",
        "element": "roman_deities",
        "extract_func": lambda x: x.split(" ")[-1]
    }
]

def extract_data(data_object):
    """Fetches data from URL, processes it, and returns a list of formatted elements."""
    url, extract_func, element = (
        data_object["link"],
        data_object["extract_func"],
        data_object["element"],
    )

    try:
        response = requests.get(url)
        response.raise_for_status() 
        elements = response.json().get(element, [])

        return [extract_func(item).title() for item in elements if isinstance(item, str)]
    
    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"Error fetching or parsing data: {e}")
        return []

def get_random_name():
    """Selects a random name from a random source."""
    selected_data = random.choice(name_data)
    names = extract_data(selected_data)
    if names:
        return random.choice(names)
    else:
        return "No valid name found"


print(get_random_name())
