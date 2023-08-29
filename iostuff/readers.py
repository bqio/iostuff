from .common import BinaryEndian
from struct import unpack as up


class BinaryReader:
    def __init__(self, file_path: str, endian: BinaryEndian = BinaryEndian.Little) -> None:
        self.file_path = file_path
        self.endian = "<" if endian == BinaryEndian.Little else ">"
        self.file_mode = "rb"
        self.fp = None

    def __enter__(self):
        self.fp = open(self.file_path, self.file_mode)
        return self

    def __exit__(self, type, value, traceback):
        self.fp.close()

    def read(self, number: int) -> bytes:
        return self.fp.read(number)

    def __read_num(self, type: str, size: int) -> int:
        return up(f"{self.endian}{type}", self.read(size))[0]

    def read_ubyte(self) -> int:
        return self.__read_num("B", 1)

    def read_byte(self) -> int:
        return self.__read_num("b", 1)

    def read_ushort(self) -> int:
        return self.__read_num("H", 2)

    def read_short(self) -> int:
        return self.__read_num("h", 2)

    def read_uint(self) -> int:
        return self.__read_num("I", 4)

    def read_int(self) -> int:
        return self.__read_num("i", 4)

    def read_ulong(self) -> int:
        return self.__read_num("Q", 8)

    def read_long(self) -> int:
        return self.__read_num("q", 8)

    def seek(self, offset: int) -> int:
        return self.fp.seek(offset)

    def tell(self) -> int:
        return self.fp.tell()

    def skip(self, number: int) -> int:
        return self.seek(self.tell() + number)

    def read_utf8_string(self, length: int) -> str:
        return self.read(length).decode('utf-8')

    def read_utf8_nt_string(self, nt: int = 0) -> str:
        byte_array = bytearray()
        while (byte := self.read_byte()) != nt:
            byte_array.append(byte)
        return bytes(byte_array).decode('utf-8')

    def align(self, number: int) -> int:
        offset = self.tell()
        align = (number - (offset % number)) % number
        return self.seek(offset + align)
