def central_tendency (num1: float, num2: float, *nums: float) -> dict[str, float]:
    sample = sorted((num1, num2) + nums)
    sample_lenght = len(sample)
    half_sample = sample_lenght // 2
    multiplied = 1
    numerator_sum = 0


    arithmetic = sum(sample) / sample_lenght
    if sample_lenght % 2 :
        median = float(sample[half_sample])
    else:
        median = float(sum(sample[half_sample - 1], sample[half_sample + 1]) / 2)

    for num in sample:
        multiplied *= num
        numerator_sum += 1 / num
        geometric = float(multiplied ** (1 / sample_lenght))
        harmonic = float(sample_lenght / numerator_sum)

    tendency = {
        'median': median,
        'arithmetic': arithmetic,
        'geometric': geometric,
        'harmonic': harmonic
    }

    return tendency
