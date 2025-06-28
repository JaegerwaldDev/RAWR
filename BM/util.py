class Nibble:
    def merge_int3_bool(a: int, b: bool):
        return ((a % 8) << 1) | int(b)
    def unmerge_int3_bool(a: int):
        return ((a >> 1) & 0b111, (a & 1) == 1)

    def merge_pair(a: int, b: int):
        return ((a % 16) << 4) | (b % 16)
    def unmerge_pair(a: int):
        return ((a >> 4) & 0xF, a & 0xF)
    
    def spread(a: int):
        return (a << 4) | a
    
class Byte:
    def merge(chunk_size: int, chunks: list):
        result = 0

        for i, value in enumerate(chunks):
            result |= value << (len(chunks) - i - 1) * chunk_size

        return result
    
    def split(chunk_size: int, value: int, chunk_count: int):
        result = []

        for i in range(chunk_count):
            result.append(
                (value >> (chunk_count - i - 1) * chunk_size) &
                (1 << chunk_size) - 1
            )

        return result