class KeyValueStorage:

    class_dict = dict()

    def __init__(self, path):
        self.path = path

        with open(path) as file:
            for line in file:
                temp_list = line.strip().split("=")
                if temp_list[1].isdigit():
                    KeyValueStorage.class_dict.update({temp_list[0]: int(temp_list[1])})
                else:
                    KeyValueStorage.class_dict.update({temp_list[0]: temp_list[1]})

                if temp_list[0] not in dir(KeyValueStorage):
                    if temp_list[1].isdigit():
                        setattr(self, temp_list[0], int(temp_list[1]))
                    else:
                        setattr(self, temp_list[0], temp_list[1])
                else:
                    raise ValueError(f"Value {temp_list[0]} can't be attribute")

    def __getitem__(self, key):
        return KeyValueStorage.class_dict[key]
