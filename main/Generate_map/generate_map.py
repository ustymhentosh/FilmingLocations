import argparse
import folium
import math


def find_distance(lat_1, lon_1, lat_2, lon_2):
    """" Returns distance between points """
    lon_1, lat_1, lon_2, lat_2 = map(math.radians, [lon_1, lat_1, lon_2, lat_2])
    haversin = lambda x: math.sin(x/2) ** 2
    d = 2 * 6400 * 1000 * math.asin(math.sqrt(\
        haversin(abs(lat_2 - lat_1)) + 
        math.cos(lat_1) * math.cos(lat_2) * haversin(abs(lon_2 - lon_1))))
    return d


def find_ten_closest_places(year, latitude, longitude):
    """ Finds ten closest places """
    dictionary = {}
    with open(f'Years partition\{year}.txt', 'r') as raw_info:
        for line in raw_info:
            dictionary[eval(line[:line.find(')') + 1])] = eval(line.strip()[line.find('['):])
    
    top_10 =  sorted(dictionary.keys(), key = lambda coords: find_distance(latitude, longitude, coords[0], coords[1]))[:10]
    return [(dictionary[i][0], i) for i in top_10]


def generate_map(year, latitude, longitude):
    """ Generates html map """
    res = find_ten_closest_places(year, latitude, longitude)
    rradius = sorted([find_distance(latitude, longitude, lat_lon[1][0], lat_lon[1][1]) for lat_lon in res])[-1]
    map = folium.Map(location=[latitude, longitude], zoom_start= 6)
    fg = folium.FeatureGroup(name="Movies map")

    for i in res:
        fg.add_child(folium.Marker(location = [i[1][0], i[1][1]],
                            popup = i[0],
                            icon=folium.Icon()))

    fg.add_child(folium.Circle(location = [latitude, longitude],
                                fill_color='#000',
                                radius= rradius, weight=2, color="#000"))
    map.add_child(fg)
    map.save('Final_map.html')
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = 'generate_map',
                    description = 'gererates map of movies')
    parser.add_argument('year',
                    type = int,
                    help ='year when movies were filmed')
    parser.add_argument('latitude',
                    type = float,
                    help ='latitude of user`s position')
    parser.add_argument('longitude',
                    type = float,
                    help ='longitude of user`s position')
    parser.add_argument('path_to_dataset',
                    type = str,
                    help ='path to movies locations dataset')
    args = parser.parse_args()

    generate_map(str(args.year), args.latitude , args.longitude)

    