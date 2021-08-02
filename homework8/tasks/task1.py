
class KeyValueStorage:

    class_dict = dict()

    def __init__(self, path):
        self.path = path

        with open(path) as file:
            for line in file:
                local_lost = line.strip().split("=")
                if local_lost[1].isdigit():
                    KeyValueStorage.class_dict.update({local_lost[0]: int(local_lost[1])})
                else:
                    KeyValueStorage.class_dict.update({local_lost[0]: local_lost[1]})

                if local_lost[0] not in dir(KeyValueStorage):
                    if local_lost[1].isdigit():
                        setattr(self, local_lost[0], int(local_lost[1]))
                    else:
                        setattr(self, local_lost[0], local_lost[1])
                else:
                    raise ValueError(f"Value {local_lost[0]} can't be attribute")

    def __getitem__(self, key):
        return KeyValueStorage.class_dict[key]
