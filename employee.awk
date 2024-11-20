BEGIN {
    FS=":";  # Set the field separator as ":"
    print "Emp No.\tEmpName\t\tBasic Salary\tDA\t\tHRA\t\tGross Salary";
    print "---------------------------------------------------------------------------------------------";
}

{
    emp_no = $1;
    emp_name = $2;
    basic_salary = $3;

    # Calculate DA (50% of Basic Salary)
    da = basic_salary * 0.50;

    # Calculate HRA (30% of Basic Salary)
    hra = basic_salary * 0.30;

    # Calculate Gross Salary
    gross_salary = basic_salary + da + hra;

    # Print the result in the required format
    printf "%s\t%s\t%.2f\t%.2f\t%.2f\t%.2f\n", emp_no, emp_name, basic_salary, da, hra, gross_salary;
}
