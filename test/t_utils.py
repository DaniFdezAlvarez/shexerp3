import re

_BLANKS = re.compile("[ \t]+")
_LINE_JUMPS = re.compile("\n+")

_PREFIX = "PREFIX"
_BEG_SHAPE = "{"
_END_SHAPE = "}"


def get_namespaces_and_shapes_from_str(str_target):
    namespaces = []
    shapes = {}
    last_line = ""
    current_shape = None

    for a_line in str_target.split("\n"):
        if a_line.startswith(_PREFIX):
            namespaces.append(a_line)
        elif a_line.startswith(_BEG_SHAPE):
            current_shape = last_line
            shapes[last_line] = []
        elif a_line.startswith(_END_SHAPE):
            current_shape = None
        elif current_shape is not None:
            shapes[current_shape].append(a_line.replace(";", "").strip())  # Avoid trailing ";", that can be there or not

        last_line = a_line  # Always execute

    return namespaces, shapes


def unordered_lists_match(list1, list2):
    return set(list1) == set(list2)


def namespaces_match(names1, names2):
    return unordered_lists_match(names1, names2)


def shapes_match(shapes1, shapes2):
    if len(shapes1) != len(shapes2):
        return False
    for a_key_label in shapes1:
        if a_key_label not in shapes2:
            return False
        if not unordered_lists_match(shapes1[a_key_label], shapes2[a_key_label]):
            return False
    return True


def complex_shape_comparison(str1, str2):
    namespaces1, shapes1 = get_namespaces_and_shapes_from_str(str1)
    namespaces2, shapes2 = get_namespaces_and_shapes_from_str(str2)

    if not namespaces_match(namespaces1, namespaces2):
        return False
    return shapes_match(shapes1, shapes2)


def normalize_str(str_target):
    result = str_target.strip()
    result = _BLANKS.sub(result, " ")
    return _LINE_JUMPS.sub(result, "\n")


def tunned_str_comparison(str1, str2):
    if normalize_str(str1) == normalize_str(str2):
        return True
    else:
        return complex_shape_comparison(str1, str2)

def file_vs_str_tunned_comparison(file_path, str_target):
    with open(file_path, "r") as in_stream:
        content = in_stream.read()
    return tunned_str_comparison(content, str_target)

def file_vs_file_tunned_comparison(file_path1, file_path2):
    with open(file_path1, "r") as in_stream:
        content1 = in_stream.read()
    with open(file_path2, "r") as in_stream:
        content2 = in_stream.read()
    return tunned_str_comparison(content1, content2)

def number_of_shapes(target_str):
    counter = 0
    for a_line in target_str.split("\n"):
        if a_line.startswith(_BEG_SHAPE):
            counter += 1
    return counter

def shape_contains_constraint(target_str, shape, constraint):
    constraint = constraint.replace(";","").strip()
    lines = target_str.split("\n")
    seeking_mode = False
    for i in range(len(lines)):
        if seeking_mode:
            if lines[i].replace(";", "").strip() == constraint:
                return True
            if lines[i].startswith(_END_SHAPE):
                return False
        if lines[i].startswith(_BEG_SHAPE) and shape == lines[i-1].strip():
            seeking_mode = True
    return False
