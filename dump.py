import zlib
import sys

def dump(inf, outf):
    blocks = open(inf, 'rb').read().split(b'\r\n\r\n')
    out = open(outf, 'wb')

    for block in blocks[:-1]:
        if block.startswith(b'GET ') or block.startswith(b'POST '):
            out.write(block.split(b'\r\n', 1)[0])
            out.write(b'\n')

        elif block.startswith(b'pve_level'):
            out.write(block.split(b'HTTP/', 1)[0])
            out.write(b'\n')

        elif block.startswith(b'HTTP/'):
            pass

        else:
            data = b''
            while True:
                t = block.split(b'\r\n', 1)
                size = int(t[0], 16)
                if size == 0:
                    break
                block = t[1]
                data += t[1][:size]
                block = t[1][size + 2:]
            out.write(zlib.decompress(data))
            out.write(b'\n\n')

if __name__ == '__main__':
    dump(sys.argv[1], sys.argv[2])
