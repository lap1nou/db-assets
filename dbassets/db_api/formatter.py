import json


def format_into_txt(objects):
    output = ""

    for object in objects[1:]:
        for attribute in object:
            output += attribute
            output += "\n"

    return output


def format_into_csv(objects):
    output = ""

    for object in objects:
        for attribute in object:
            output += attribute
            if attribute != object[-1]:
                output += ","

        output += "\n"

    return output


def format_into_json(objects):
    output = []
    columns_name = objects[0]

    for object in objects[1:]:
        tmp = dict()
        i = 0

        for attribute in object:
            tmp[columns_name[i].lower()] = attribute
            i += 1

        output.append(tmp)

    return json.dumps(output)
