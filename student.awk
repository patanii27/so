BEGIN {
    print "Student Report"
    print "Name\tAverage\tGrade"
    print "\t\t"
}

{	
    if ($1 == "Rollno") next;
    avg = ($3 + $4 + $5 + $6 + $7) / 5
    
    if (avg < 40) {
        grade = "F"
    } else if (avg < 55) {
        grade = "C"
    } else if (avg < 65) {
        grade = "B"
    } else if (avg < 75) {
        grade = "B+"
    } else if (avg < 80) {
        grade = "A"
    } else if (avg < 85) {
        grade = "A+"
    } else {
        grade = "O"
    }

    print $2 "\t" avg "\t" grade
}

END {
    print ""
    print "End of report"
}
