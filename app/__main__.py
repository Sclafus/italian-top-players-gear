import csv
import tabulate
from .playerinfo.PlayerInfo import PlayerInfo


def get_data(filename: str = 'data.tsv'):
    data = _load_data(filename)
    return data


def _load_data(filename: str = 'data.tsv'):
    data = _load_raw_data(filename)
    data_trimmed = _trim_raw_data(data)
    return transform_raw_data(data_trimmed)


def _load_raw_data(filename: str = 'data.tsv'):
    with open(filename) as file:
        tsv_file = csv.reader(file, delimiter="\t")
        next(tsv_file)
        return [l for l in tsv_file]


def _trim_raw_data(data: list[list[str]]):
    data = [row for row in data if row[1] != '']
    return data


def transform_raw_data(data: list[list[str]]):
    return [
        PlayerInfo(
            rank = int(line[0]) if line[0] != '#ERROR!' else -1,
            pp = int(line[1].replace(',', '')) if line[1] != '#ERROR!' else 0,
            username = line[2],
            city = line[3],
            play_style = line[4],
            tap_style = line[5],
            tablet_mouse = line[6],
            area_filter_sensitivity = line[7],
            grip = line[8],
            keyboard = line[9],
            switch = line[10],
            osu_resolution = line[11],
            skin = line[12]
        )
    for line in data[1:]]


def get_headers(filename: str = 'data.tsv'):
    data = _load_raw_data(filename)
    return [entry.replace('|', '/') for entry in data[0]]


def make_table(data: list[PlayerInfo]):
    return tabulate.tabulate(data, headers=get_headers(), tablefmt='github')


def write_table(new_table: str, separator = '[//]: # (Table)\n'):
    file_content = ""
    with open('README.md') as f:
        file_content = f.read()

    header, _ = file_content.split(separator)

    with open('README.md', 'w') as f:
        f.write(f"{header}{separator}\n{new_table}")


if __name__ == '__main__':
    data = get_data()
    table = make_table(data)
    write_table(table)
