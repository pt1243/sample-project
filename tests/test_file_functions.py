from my_package.file_functions import simple_read, DATA_DIR


def test_simple_read():
    assert simple_read(DATA_DIR / "data_file.txt") == "Hello world!"
