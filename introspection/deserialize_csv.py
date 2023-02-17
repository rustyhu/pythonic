'Simulate a "deserialize" process from a csv file, using metaprogramming to generate class'

import csv
import json
from typing import List, Any


def collect(csvfilename) -> List[Any]:
    "Unsafe! Dynamically generates a class, and returns a list of this type of objects"
    with open(csvfilename, newline='', encoding='utf8') as f:
        riter = csv.reader(f)
        collection = []
        for lineno, row in enumerate(riter):
            if lineno == 0:
                # must create class first!!!
                class csvdata:
                    """
                    Each line of the csv correspond to an object of me.
                    Pour the data of the each line into this constructor!
                    """
                    names = row

                    def __init__(self, vals: List[str]):
                        # length of vals must equal length of names!
                        for i, name in enumerate(self.names):
                            # parse int
                            try:
                                v = int(vals[i])
                            except ValueError:
                                v = vals[i]

                            setattr(self, name, v)

                    def __str__(self) -> str:
                        s = self.__class__.__name__ + "{"
                        for name in self.names:
                            if s[-1] != "{":
                                s += ", "
                            s += f"{name} : {getattr(self, name)}"

                        s += "}"
                        return s

            else:
                collection.append(csvdata(row))

    return collection


def collection_ser_to_json(filename, indent=4, sort_keys=False) -> str:
    collection = collect(filename)
    print(f"Serialize total {len(collection)} element...")

    # For UTF8 characters https://docs.python.org/3/library/json.html#character-encodings
    return json.dumps(collection,
                      ensure_ascii=False,
                      default=lambda o: o.__dict__,
                      indent=indent,
                      sort_keys=sort_keys)
    # res = ""
    # for ele in collection:
    #     res += json.dumps(ele,
    #                       default=lambda o: o.__dict__,
    #                       indent=indent,
    #                       sort_keys=sort_keys)

    # return res
