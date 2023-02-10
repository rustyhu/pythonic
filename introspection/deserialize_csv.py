'Simulate a "deserialize" process from a csv file'

import csv
import json
from typing import List, Any


def collect(csvfilename) -> List[Any]:
    with open(csvfilename, newline='', encoding='utf-8') as f:
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

                    def __init__(self, *vals):
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
                        isFirst = True
                        for name in self.names:
                            if isFirst:
                                isFirst = False
                            else:
                                s += ", "

                            s += f"{name} : {getattr(self, name)}"
                        s += "}"
                        return s

            else:
                collection.append(csvdata(*row))

    return collection


def collection_ser_to_json():
    collection = collect("ruleset.csv")
    print(f"Show total {len(collection)} element:")

    for ele in collection:
        # print(ele)
        print(
            json.dumps(ele,
                       default=lambda o: o.__dict__,
                       sort_keys=True,
                       indent=4))


collection_ser_to_json()
