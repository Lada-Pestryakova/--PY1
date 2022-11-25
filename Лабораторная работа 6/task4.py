import json

INPUT_FILE = "input_1.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as csv_file:  # TODO реализовать конвертер из csv в json
        rows = [((''.join(row.split(new_line))).split(delimiter)) for row in csv_file]
        headers, *data = rows
        list_dict = [{headers[value]: row_[value] for value in range(len(row_))} for row_ in data]
    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
