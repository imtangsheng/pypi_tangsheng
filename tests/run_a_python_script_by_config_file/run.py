import os
from configs import *


if __name__ == "__main__":
    print(__file__)
    # json_file_path = r"E:\Development\1-Pre-Alpha\sound_animation\tests\test_config\configs.json"
    json_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "configs.json")
    data = load_json_file(json_file_path)
    print(data["ENV"])
