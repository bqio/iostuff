from iostuff.writers import MemoryWriter, BinaryWriter


def test_binary_writer_write() -> None:
    with BinaryWriter("data2.dat") as writer:
        writer.write_int(4)


def test_memory_writer_write() -> None:
    memory = MemoryWriter()
    memory.write(b'\xdd')
    assert memory.getbuffer() == b'\xdd'


def test_memory_writer_write_byte() -> None:
    memory = MemoryWriter()
    memory.write_ubyte(221)
    memory.write_byte(-35)
    assert memory.getbuffer() == b'\xdd\xdd'


def test_memory_writer_write_short() -> None:
    memory = MemoryWriter()
    memory.write_ushort(56797)
    memory.write_short(-8739)
    assert memory.getbuffer() == b'\xdd\xdd\xdd\xdd'


def test_memory_writer_write_int() -> None:
    memory = MemoryWriter()
    memory.write_uint(3722304989)
    memory.write_int(-1)
    assert memory.getbuffer() == b'\xdd\xdd\xdd\xdd\xff\xff\xff\xff'


def test_memory_writer_write_long() -> None:
    memory = MemoryWriter()
    memory.write_ulong(18446744073136889309)
    assert memory.getbuffer() == b'\xdd\xdd\xdd\xdd\xff\xff\xff\xff'
    memory.seek(0)
    memory.write_long(-572662307)
    assert memory.getbuffer() == b'\xdd\xdd\xdd\xdd\xff\xff\xff\xff'
