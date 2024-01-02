# Program afisare salarii 
# 02.01.2024
# System Engineer Bogdan F

# module necesare

from tabulate import tabulate
from colored import fg, attr

def calculate_earnings(salaries):
    months = 12
    years = 40

    # Calcul pentru 12 luni
    total_12_months = sum(salaries)

    # Calculate pentru 40 de ani
    total_40_years = total_12_months * years

    return total_12_months, total_40_years

def main():
    # Lista cu salarii predefinite
    predefined_salaries = [400, 1000, 2000, 3000, 4000, 5000, 10000, 30000, 100000]

    table_data = []

    for salary in predefined_salaries:
        salaries = [salary] * 12  
        total_12_months, total_40_years = calculate_earnings(salaries)

        table_data.append([
            f"{fg(9)}For {salary} euros/month{attr(0)}",
            f"{fg(46)}{total_12_months:,} euros{attr(0)}",
            f"{fg(82)}{total_40_years:,} euros{attr(0)}"
        ])

    headers = [
        f"{fg(75)}Salary{attr(0)}",
        f"{fg(75)}Total Earnings (12 months){attr(0)}",
        f"{fg(75)}Total Earnings (40 years){attr(0)}"
    ]
    
    print(tabulate(table_data, headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
