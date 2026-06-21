from loader import load_file
from csv_reader import create_reader
from initializer import initialize
from processor import process_records
from calculator import calculate_averages
from report_writer import write_report
from display import display_report

# Step 1: Load file
file_obj = load_file()

# Step 2: Create CSV reader
parser = create_reader(file_obj)

# Step 3: Initialize variables
cos_cum, bio_cum, chm_cum, elements = initialize()

# Step 4: Process records
cos_cum, bio_cum, chm_cum, elements = process_records(
    parser, cos_cum, bio_cum, chm_cum, elements
)

# Step 5: Calculate averages
cos_avg, bio_avg, chm_avg = calculate_averages(
    cos_cum, bio_cum, chm_cum, elements
)

# Step 6: Write report
write_report(elements, cos_avg, bio_avg, chm_avg)

# Step 7: Display result
display_report()
