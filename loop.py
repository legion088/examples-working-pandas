import re


def check_inclusion(doc_readlines: list, df: object) -> list:
    list_inclusion = list()
    for row in df.itertuples(index=False):
        expression = re.compile(row[0], re.IGNORECASE)
        if any(line for line in doc_readlines if expression.search(line)):
            list_inclusion.append(row[0])
    return list_inclusion
