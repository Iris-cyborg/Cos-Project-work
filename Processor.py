def process_records(parser, cos_cum, bio_cum, chm_cum, elements):
    for structured_row in parser:
        cos_cum += int(structured_row['COS102'])
        bio_cum += int(structured_row['BIO102'])
        chm_cum += int(structured_row['CHM102'])
        elements += 1

    return cos_cum, bio_cum, chm_cum, elements
