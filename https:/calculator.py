from math_utils import compute_arithmetic_mean

def calculate_averages(cos_cum, bio_cum, chm_cum, elements):
    cos_avg = compute_arithmetic_mean(cos_cum, elements)
    bio_avg = compute_arithmetic_mean(bio_cum, elements)
    chm_avg = compute_arithmetic_mean(chm_cum, elements)

    return cos_avg, bio_avg, chm_avg
