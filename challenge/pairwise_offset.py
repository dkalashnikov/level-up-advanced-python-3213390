def pairwise_offset(sequence, fillvalue='*', offset=0):
    for i in range(0, len(sequence)+offset):
        try:
            first = sequence[i]
        except IndexError:
            first = fillvalue

        sec_index = i-offset
        try:
            sec = sequence[sec_index]
            if sec_index < 0:
                sec = fillvalue
        except IndexError:
            sec = fillvalue
        yield (first, sec)
