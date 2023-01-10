import csv
from .playerinfo.PlayerInfo import PlayerInfo


def get_data(filename: str = 'data.tsv'):
    data = _load_data(filename)
    return data


def _load_data(filename: str = 'data.tsv'):
    data = _load_raw_data(filename)
    return transform_raw_data(data)


def _load_raw_data(filename: str = 'data.tsv'):
    with open(filename) as file:
        tsv_file = csv.reader(file, delimiter="\t")
        next(tsv_file)
        return [l for l in tsv_file]


def transform_raw_data(data: str):
    return [
        PlayerInfo(
            rank = int(line[0]),
            pp = int(line[1].replace(',', '')),
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
    import tabulate
    return tabulate.tabulate(data, headers=get_headers(), tablefmt='github')


if __name__ == '__main__':
    data = get_data()
    table = make_table(data)

    with open('README.md', 'w') as f:
        f.write(table)
