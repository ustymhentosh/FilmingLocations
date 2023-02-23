import re
from geopy.geocoders import Nominatim
from tqdm import tqdm
import argparse

## execute if you don`t have this module
# subprocess.call('pip install geopy')

def get_coords(address: str, precise = False) -> None:
    """
    Gets coords from adderss
    >>> get_coords('Lviv, Ukraine', precise = True)
    (49.841952, 24.0315921)
    """
    try:
        geolocator = Nominatim(user_agent = "Movies location search")
        location = geolocator.geocode(address.strip(), timeout=None)
        if precise:
            while not location:
                address = address[address.find(',') + 1 :]
                location = geolocator.geocode(address.strip(), timeout=None)
        if location:
            return (location.latitude, location.longitude)
    except KeyboardInterrupt:
        return 'Safe stop'
    except:
        return None


def read_transform_write(database_path: str) -> dict:
    """
    Reads database, finds coordinates, and writes to the new file
    """
    names = set()
    count = set()
    universal_dictionary = {}
    with open(database_path, 'r') as raw_file:
        for line in raw_file:
            try:
                # extracting names
                name = line[:line.find('(')]

                # extracting year
                year_span = re.search(r'\(\d{4}\)', line).span()
                year = line[year_span[0] + 1: year_span[1] - 1]

                # extractind address
                address_search = line[year_span[1]:].strip()
                address_search = re.sub(pattern = r'\([^)]*\)', repl = '', string = address_search)
                address_search = re.sub(pattern = r'\{[^)]*\}', repl = '', string = address_search).strip()

                # writing to dictionary
                if name not in names:
                    if universal_dictionary.get(year):
                        if universal_dictionary[year].get(address_search):
                            universal_dictionary[year][address_search].append(name)
                        else:
                            universal_dictionary[year][address_search] = [name]
                    else:
                        universal_dictionary[year] = {address_search: [name]}
                    count.add(address_search)
                names.add(name)
            except KeyboardInterrupt:
                break
            except:
                continue
    return universal_dictionary


def engage_decoding(universal_dictionary: dict, year = '') -> dict:
    """
    Writes by years and modifies dict
    >>> engage_decoding({2000: {'Lviv, Ukraine': ["point"]}}, 2000)
    {(49.841952, 24.0315921): ['point']}
    """
    memory = {}

    # one year operation
    one_year_dct = {}
    if year:
        with open(f'{year}.txt', 'w') as write_here:
            for address in tqdm(universal_dictionary[year]):
                if not memory.get(address):
                    result = get_coords(address)
                    memory[address] = result
                else:
                    result = memory[address]
                # catching stop and writing to the file
                if result == 'Safe stop':
                    return None
                if result:
                    one_year_dct[result] = universal_dictionary[year][address]
                    write_here.write(f'{result} == {universal_dictionary[year][address]}\n')
        return one_year_dct

    # all years
    dream_dictionary = {}
    for year in tqdm(universal_dictionary.keys()):
        with open(f'{year}.txt', 'w') as write_here:
            dream_dictionary[year] = {}
            for address in tqdm(universal_dictionary[year].keys()):
                # remembering done things
                if not memory.get(address):
                    result = get_coords(address)
                    memory[address] = result
                else:
                    result = memory[address]
                # catching stop and writing to the file
                if result == 'Safe stop':
                    return None
                if result:
                    dream_dictionary[year][result] = universal_dictionary[year][address]
                    write_here.write(f'{result} == {universal_dictionary[year][address]}\n')

    return dream_dictionary


if __name__ == '__main__':

    import doctest
    print(doctest.testmod())

    parser = argparse.ArgumentParser(
                    prog = 'transforn data',
                    description = 'transformes data into needed files')
    parser.add_argument('file',
                    type = str,
                    help ='file where to read')
    args = parser.parse_args()

    engage_decoding(read_transform_write(args.file))
