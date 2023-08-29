from iostuff.readers import BinaryReader


def test_binary_reader_read() -> None:
    with BinaryReader("data.dat") as reader:
        assert reader.read(1) == b'\xdd'


def test_binary_reader_read_byte() -> None:
    with BinaryReader("data.dat") as reader:
        assert reader.read_ubyte() == 221
        assert reader.read_byte() == -35


def test_binary_reader_read_short() -> None:
    with BinaryReader("data.dat") as reader:
        assert reader.read_ushort() == 56797
        assert reader.read_short() == -8739


def test_binary_reader_read_int() -> None:
    with BinaryReader("data.dat") as reader:
        assert reader.read_uint() == 3722304989
        reader.seek(0)
        assert reader.read_int() == -572662307


def test_binary_reader_read_long() -> None:
    with BinaryReader("data.dat") as reader:
        assert reader.read_ulong() == 18446744073136889309
        reader.seek(0)
        assert reader.read_long() == -572662307


def test_binary_reader_read_utf8_string() -> None:
    with BinaryReader("data.dat") as reader:
        reader.seek(8)
        assert reader.read_utf8_string(6) == "Hello!"


def test_binary_reader_read_utf8_nt_string() -> None:
    with BinaryReader("data.dat") as reader:
        reader.seek(8)
        assert reader.read_utf8_nt_string() == "Hello!"


def test_binary_reader_align() -> None:
    with BinaryReader("data.dat") as reader:
        reader.seek(6)
        reader.align(4)
        assert reader.tell() == 8


def test_binary_reader_skip() -> None:
    with BinaryReader("data.dat") as reader:
        reader.skip(4)
        assert reader.tell() == 4
