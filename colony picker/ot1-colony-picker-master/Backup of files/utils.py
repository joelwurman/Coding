import csv

PLATE_WIDTH_MM = 86.0
PLATE_HEIGHT_MM = 129.0

PLATE_INNER_WIDTH_MM = 75.7
PLATE_INNER_HEIGHT_MM = 114.8

NO_TOUCH_Z_OFFSET = 2

X_OFFSET = 0.2
Y_OFFSET = -0.5
Z_OFFSET = 0

GRID_96 = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
            "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
            "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
            "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
            "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
            "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
            "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
            "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8",
            "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9",
            "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10",
            "A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11",
            "A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12"]


def get_vector_from_csv(path="/Users/joelwurman-rodrich/Desktop/ot1-colony-picker-master/csvs/joeltest2.csv"):
    with open(path, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        vector_list = []
        for row in spamreader:
            if row[1] == " 1":
                x = row[2]
                y = row[3]
                print("X: {}, Y:{}".format(x, y))
                vector_list.append([x, y, 0])
    return vector_list


def translate_vector_for_robot(vector=[0, 0, 0]):
    from PIL import Image
    im = Image.open('/Users/joelwurman-rodrich/Desktop/ot1-colony-picker-master/2020_cropped.jpg')
    width, height = im.size
    print("W: {}, H: {}".format(width, height))

    w_px_to_mm_ratio = width / PLATE_WIDTH_MM
    h_px_to_mm_ratio = height / PLATE_HEIGHT_MM
    x_mm = float(vector[0]) / w_px_to_mm_ratio
    y_mm = (height - float(vector[1])) / h_px_to_mm_ratio
    return ([x_mm, y_mm, 0])


def _read_content_and_index(path, line_start):
    f = open(path, "r")
    contents = f.readlines()
    index = 0
    for i, line in enumerate(contents):
        if line.startswith(line_start):
            index = i + 1
            break
    f.close()
    return (index, contents)


def write_moves_to_python_file(path, lines_to_add):
    index, contents = _read_content_and_index(path, "#!---")

    if not index:
        print("No index to insert robot commands found. Continuing..")
    else:
        next_well_idx = 0
        for line in lines_to_add:
            contents.insert(index, "pipette.pick_up_tip()\n")
            contents.insert(index + 1, "robot.move_to((input_plate, [{} + {}, {} + {}, {}]), pipette)\n".format(line["x"], line["x_offset"], line["y"], line["y_offset"], NO_TOUCH_Z_OFFSET))
            contents.insert(index + 2, "pipette.move_to(output_plate.wells('{}').bottom())\n".format(GRID_96[next_well_idx]))
            contents.insert(index + 3, "pipette.aspirate(50)\n")
            contents.insert(index + 4, "pipette.dispense(50)\n")
            contents.insert(index + 5, "pipette.drop_tip()\n")
            index = index + 6
            next_well_idx += 1

    f = open(path, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


def set_offsets(vector=[0, 0, 0]):
    x = vector[0]
    y = vector[1]

    x_offset = X_OFFSET
    y_offset = Y_OFFSET

    if x < (75.7 / 3):
        x_offset += 0
    if x > ((75.7 / 3) * 2):
        x_offset += 0
    if y < (114.8 / 3):
        y_offset -= 0
    if y > ((114.8 / 3) * 2):
        y_offset += 0
    return (x_offset, y_offset)


translated_vector_list = []
for vector in get_vector_from_csv("csvs/realRun.csv"):
    translated_vector_list.append(translate_vector_for_robot(vector))
vectors = []
for vector in translated_vector_list:
    x_offset, y_offset = set_offsets([vector[0], vector[1], vector[2]])
    vectors.append({"x":vector[0], "y": vector[1], "x_offset": x_offset, "y_offset": y_offset})
    print("X: {}, Y:{}, Z:{}".format(vector[0], vector[1], vector[2]))

write_moves_to_python_file("move_to.py", vectors)
