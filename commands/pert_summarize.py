from ..work_with_data import *
from ..calculations import *

def summarize(cache: list=None) -> dict:
    output_data_buf = cache if cache else bufferize("PERT/data/output_data.csv")
    time_sum = calc_time_sum(output_data_buf)
    deviation_sum = calc_deviation_sum(output_data_buf)
    summarize = {"ALL TIME": time_sum, "DEVIATION": deviation_sum}
    return summarize