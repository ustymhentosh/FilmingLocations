# Filming Locations

This project is a Python application that generates an interactive map of movie filming locations. The user provides their current location (latitude and longitude) and the year of the movies they're interested in, and the application generates a map with markers indicating the ten closest movie filming locations and a circle that encompasses all ten locations.

## **Prerequisites**

- Python 3.10
- Required libraries: argparse, folium, math

## **Installation**

1. Clone the repository: **`git clone https://github.com/ustymhentosh/Filming_locations.git`**
2. Navigate to the project directory: **`cd Filming_locations\main\generate_map`**

## **Usage**

❗❗❗ run **`main.py`** from `**generate_map**` folder or else It won’t work. Pass the following arguments:

```powershell

python main.py [year] [latitude] [longitude] [path_to_dataset]

```

The **`year`** argument specifies the year of the movies you're interested in. The **`latitude`** and **`longitude`** arguments specify your current location. The **`path_to_dataset`** argument specifies the path to the movies dataset. ❗❗❗But, because dataset `**locations.list**` was to big, program actually uses other, already generated files in `**Years partition**` folder. That is why It is crucial to run this from `**generate_map**` folder

## main.py - F**unctions**

The code includes the following functions:

- **`find_distance(lat_1, lon_1, lat_2, lon_2)`**: Calculates the distance between two points on the Earth's surface, given their latitudes and longitudes in degrees.
- **`find_ten_closest_places(year, latitude, longitude)`**: Returns a list of the ten closest places where movies were filmed in a given year, sorted by distance from the user's current location.
- **`generate_map(year, latitude, longitude)`**: Generates an HTML map of the ten closest places where movies were filmed in a given year, with the center of the map at the user's current location.

If you want to understand more about analyzing file **`locations.list`** read this:

[database_transformation.py](https://www.notion.so/database_transformation-py-960036ee60e446588c3d9d992df6f16b)

## **Dataset**

The application uses a dataset of movie filming locations that can be found in the **`locations.list`** file, which can be downloaded from the IMDb website.

## **Credits**

This project was created by **[Ustym Hentosh](https://github.com/ustymhentosh)**.

## **License**

This project is licensed under the MIT License.
