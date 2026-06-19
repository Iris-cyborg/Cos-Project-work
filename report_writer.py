def write_report(elements, cos_avg, bio_avg, chm_avg):
    with open("report.txt", "w") as out_txt:
        out_txt.write("============ STUDENT PERFORMANCE REPORT ============\n")
        out_txt.write(f"Total Students Processed: {elements}\n\n")
        out_txt.write(f"Average COS102 Score: {cos_avg:.2f}\n")
        out_txt.write(f"Average BIO102 Score: {bio_avg:.2f}\n")
        out_txt.write(f"Average CHM102 Score: {chm_avg:.2f}\n")
        out_txt.write("====================================================\n")
