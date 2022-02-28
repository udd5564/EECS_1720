for i in range(1, 51):
    with open("week.txt" +str(i), "w") as report_file:
        report_file.write(" - week {0} report -".format(i))
        report_file.write("\nDepartment : ")
        report_file.write("\nName : ")
        report_file.write("\nWork Summary : ")

