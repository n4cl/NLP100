
def generate_n_gram(n: int, seq: str) -> list:
    return [seq[_pos:_pos+n] for _pos in range(len(seq) - n + 1)]


_seq = "これはテストです。"
print(generate_n_gram(1, _seq))
print(generate_n_gram(2, _seq))
print(generate_n_gram(3, _seq))
