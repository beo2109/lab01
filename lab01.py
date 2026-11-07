# -*- coding: utf-8 -*-
"""Lab 1 - Python cơ bản và hệ nhị phân.

Môn: Giới thiệu ngành Kỹ thuật phần mềm - Phenikaa School of Computing.
Chỉ dùng thư viện chuẩn của Python 3.10+.
"""


# ---------------------------------------------------------------- Bài 1
def dec_to_bin(n, width=0):
    """Đổi số nguyên không âm n sang chuỗi nhị phân (không dùng bin()/format()).

    width: nếu > 0, đệm '0' bên trái cho đủ độ rộng.
    >>> dec_to_bin(10)
    '1010'
    >>> dec_to_bin(5, 8)
    '00000101'
    """
    if n < 0:
        raise ValueError("n phải không âm")
    if n == 0:
        res = "0"
    else:
        bits = []
        while n > 0:
            remainder = n % 2
            bits.append(str(remainder))
            n = n // 2

        bits.reverse()
        res = "".join(bits)
    if width > 0 and len(res) < width:
        res = res.zfill(width)

    return res

def bin_to_dec(s):
    """Đổi chuỗi nhị phân sang số nguyên (không dùng int(s, 2)).

    >>> bin_to_dec('1010')
    10
    """
    if not isinstance(s, str) or len(s) == 0:
        raise ValueError("Chuỗi không hợp lệ")

    res = 0
    for char in s:
        if char not in ('0', '1'):
            raise ValueError ("Ký tự không hợp lệ trong chuỗi nhị phân")

        res = res * 2 + int(char)

    return res

# ---------------------------------------------------------------- Bài 2
def _pad(a, b):
    w = max(len(a), len(b))
    return a.zfill(w), b.zfill(w)


def bit_and(a, b):
    """AND từng bit hai chuỗi nhị phân (đệm 0 bên trái cho cùng độ dài).

    >>> bit_and('1100', '1010')
    '1000'
    """
    a, b = _pad(a, b)
    res = []
    for i in range (len(a)):
        if a[i] == '1' and b[i] == '1':
              res.append('1')
        else:
            res.append('0')
    return "".join(res)
            
def bit_or(a, b):
    """OR từng bit.

    >>> bit_or('1100', '1010')
    '1110'
    """
    a, b = _pad(a, b)
    res = []
    for i in range(len(a)):
        if a[i] == '1' or b[i] == '1':
            res.append('1')
        else:
            res.append('0')
        return "".join(res)

def bit_xor(a, b):
    """XOR từng bit.

    >>> bit_xor('1100', '1010')
    '0110'
    """
    a, b = _pad(a, b)
    res = []
    for i in range(len(a)):
        if a[i] != b[i]:
            res.append('1')
        else:
            res.append('0')
    return ''.join(res)
    
def truth_table(op):
    """Trả về danh sách (x, y, kết quả) cho x, y thuộc {0, 1}.

    op là hàm nhận hai chuỗi 1 ký tự ('0'/'1'), ví dụ bit_and.
    >>> truth_table(bit_xor)
    [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
    """
    table = []
    for x in(0, 1):
        for y in (0, 1):
            res_str = op(str(x), str(y))
            table.append((x,y), int(res_str))
    return table

# ---------------------------------------------------------------- Bài 3
def add_bin(a, b):
    """Cộng hai số nhị phân (chuỗi) bằng thuật toán nhớ (carry), không đổi sang int.

    >>> add_bin('1011', '110')
    '10001'
    """
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = []

    while i >= 0 or j >= 0 or carry:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        total = digit_a + digit_b + carry

        res.append(str(total % 2))
        carry = total // 2
        i -= 1
        j -= 1

    res.reverse()
    return "".join(res)

def sub_bin(a, b):
    """Trừ a - b (a >= b) bằng thuật toán mượn (borrow).

    Kết quả bỏ các số 0 thừa ở đầu (giữ lại '0' nếu bằng 0).
    >>> sub_bin('10001', '110')
    '1011'
    """
    a_clean = a.lstrip('0') or '0'
    b_clean = b.lstrip('0') or '0'

    if len(a_clean) < len(b_clean) or len(len(a_clean) == len(b_clean) and a_clean < b_clean):
        raise ValueError("a phải lớn hơn hoặc bằng b")

    max_len = max(len(a), len(b))
    a_padded, b_padded = a.zfill(max_len), b.zfill(max_len)

    borrow = 0
    res = []
    for k in range(max_len - 1, -1, -1):
        diff = int(a_padded[k]) - int(b_padded[k]) - borrow
        if diff < 0:
            diff += 2 
            borrow = 1
        else:
            borrow = 0
        res.append(str(diff))

    res.reverse()
    res_str = "".join(res).lstrip('0')
    return res_str if res_str else '0'

# ---------------------------------------------------------------- Bài 4
def count_ones(n):
    """Số bit 1 của n (popcount) bằng phép n & (n - 1).

    >>> count_ones(13)
    3
    """
    count = 0 
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count

def is_power_of_two(n):
    """n là lũy thừa của 2? (n > 0 và chỉ có đúng 1 bit 1)

    >>> is_power_of_two(64)
    True
    """
    return n > 0 and (n & (n - 1)) == 0

def swap_xor(a, b):
    """Hoán đổi hai số nguyên bằng XOR (không dùng biến phụ). Trả về (a, b) mới.

    >>> swap_xor(3, 9)
    (9, 3)
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


# ---------------------------------------------------------------- Bài 5
def image_size_bytes(width, height, bits_per_pixel=24):
    """Dung lượng ảnh thô (byte) = rộng x cao x bit/pixel / 8 (làm tròn lên).

    Ví dụ màn hình TV Full HD 1920x1080, 24 bit/pixel.
    >>> image_size_bytes(1920, 1080)
    6220800
    """
    return (width * height * bits_per_pixel) // 8


def color_levels(bits_per_channel):
    """Số mức cho mỗi kênh màu và tổng số màu của ảnh RGB.

    >>> color_levels(8)
    (256, 16777216)
    """
    levels = 2 ** bits_per_channel
    total_colors = levels ** 3
    return levels, total_colors
   


def human_size(num_bytes):
    """Định dạng dung lượng: 'B', 'KB', 'MB', 'GB' (bội số 1024, 2 chữ số thập phân).

    >>> human_size(6220800)
    '5.93 MB'
    """
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = float(num_bytes)

    for unit in units:
        if size < 1024 or unit == units[-1]:
            if unit == 'B':
                return f"{int(size)} B"
            return f"{size: .2f} {unit}"
        size /= 1024.0 
        
# ---------------------------------------------------------------- Bài về nhà
def bin_to_hex(s):
    """Đổi chuỗi nhị phân sang thập lục phân (nhóm 4 bit), chữ hoa.

    >>> bin_to_hex('11111111')
    'FF'
    """
    if not s:
        return ""

    hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }

    res = []
    for i in range(0, len(s), 4):
        group = s[i:i + 4]
        res.append(hex_map[group])

        return "".join(res)

def gray_code(n):
    """Danh sách mã Gray n bit (chuỗi), liền kề khác nhau đúng 1 bit.

    >>> gray_code(2)
    ['00', '01', '11', '10']
    """
    res = []
    for i in range(1 << n):
        g = i ^ (i >> 1)
        res.append(dec_to_bin(g, n))
    return res

def main():
    print("Lab 1 - nhị phân")
    print("10 ->", dec_to_bin(10))
    print("1011 + 110 =", add_bin("1011", "110"))
    print("Full HD:", human_size(image_size_bytes(1920, 1080)))

if __name__ == "__main__":
    main()