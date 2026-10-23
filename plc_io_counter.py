"""统计三菱 PLC X/Y 地址列表；输入为大写的 X/Y 地址字符串。"""

from collections import Counter


def count_io_addresses(addresses):
    """返回不重复的 X/Y 地址数量，以及按首次出现顺序排列的重复地址。"""
    counts = Counter(addresses)
    return {
        "X": sum(address.startswith("X") for address in counts),
        "Y": sum(address.startswith("Y") for address in counts),
        "duplicates": [address for address, count in counts.items() if count > 1],
    }


def main():
    addresses = ["X0", "X1", "Y0", "Y1", "X1"]
    result = count_io_addresses(addresses)
    print(f"X={result['X']}、Y={result['Y']}")
    print("重复地址：" + ("、".join(result["duplicates"]) or "无"))


if __name__ == "__main__":
    main()
