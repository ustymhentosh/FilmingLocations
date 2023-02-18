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

## database_transformation.py

The script reads a database of movie titles and filming locations, finds the coordinates for each location using the **`geopy`** library and writes the results to a text file.

### **Dependencies**

- **`re`**
- **`geopy`**
- **`tqdm`**
- **`argparse`**

### **Installation**

Use the package manager **[pip](https://pip.pypa.io/en/stable/)** to install **`geopy`**:

```powershell

pip install geopy

```

### **Usage**

To use the execute this

❗❗❗ this will start a process of creating more that 100 files in `**generate_year_partition**` folder and will take more than `**9 hours**`. I do not recommend to run It. Only for test purposes. Also `**internet connection**` is required

```powershell

python database_transformation.py.py locations.list

```

### **Functionality**

**`read_transform_write(database_path: str) -> dict`**: Reads the input database, finds coordinates for each filming address, and writes the results to a new file.

**`engage_decoding(universal_dictionary: dict, year = '') -> dict`**: Reads in the dictionary produced by **`read_transform_write()`**, processes the data, and produces a new dictionary that maps the coordinates of each filming location to the corresponding movie titles. This function can also operate on a subset of the data for a specific year.

**`get_coords(address: str, precise = False) -> None`**: Gets the coordinates for a given address using the **`geopy`** library. If **`precise = True`**, the function will keep removing the last comma-separated value from the address until a valid coordinate is found.

## **Dataset**

The application uses a dataset of movie filming locations that can be found in the **`locations.list`** file, which can be downloaded from the IMDb website.

## Examples

```powershell
python main\Generate_map\main.py 2015 40.83826 24.02324 path_to_dataset
```

![Untitled](https://github.com/ustymhentosh/Filming_locations/blob/develop/photos/Greece.png)

```powershell
python main\Generate_map\main.py 2015 -33.8688 151.2093 path_to_dataset
```

![Untitled](https://github.com/ustymhentosh/Filming_locations/blob/develop/photos/Sydney.png)

```powershell
python main\Generate_map\main.py 2011 -0.628508, -150.42300  path_to_dataset
```

![Untitled](https://github.com/ustymhentosh/Filming_locations/blob/develop/photos/Pacific.png)

## **Credits**

This project was created by **[Ustym Hentosh](https://github.com/ustymhentosh)**.

## **License**

This project is licensed under the GNU General Public License v3.0.
