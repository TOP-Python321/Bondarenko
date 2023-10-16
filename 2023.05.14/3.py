def numbers_strip(sample: list[float], n: int = 1, *, copy: bool = False) -> list:
    global sample_stripped
    sample_stripped = sample
    sample_copy = sample.copy()
    for _ in range(n):
        sample_copy.remove(max(sample_copy))
        sample_copy.remove(min(sample_copy))


    if copy:
        sample_stripped = sample_copy
        return sample_stripped


    else:
        sample_stripped[0:] = sample_copy[0:]
        return sample_stripped






# sample = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
# numbers_strip(sample, 1)
# [0.2, 0.3, 0.4, 0.5]
# sample is sample_stripped
# True

