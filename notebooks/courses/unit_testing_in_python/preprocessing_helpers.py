def convert_to_int(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.split(",")
    integer_string_without_commas = "".join(comma_separated_parts)

    for i in range(len(comma_separated_parts)):
        if len(comma_separated_parts[i]) > 3:
            return None
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None

    try:
        return int(integer_string_without_commas)
    except ValueError:
        return None


def row_to_list(row):
    row = row.rstrip("\n")
    separated_entries = row.split("\t")

    if len(separated_entries) == 2 and "" not in separated_entries:
        return separated_entries

    return None
