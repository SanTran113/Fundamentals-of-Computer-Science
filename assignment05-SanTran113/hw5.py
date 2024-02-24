import build_data
import sys

import county_demographics
import hw4

full_data = build_data.getData()

if __name__ == "__main__":
    # f = open("/inputs")
    #inputs = input()
    # hw5.py inputs/ca.ops
    inputs = sys.argv[1]
    try:
        f = open(inputs, "r")
        for line in f:
            l = line.split(":")
            if "display" in line:
                for ele in full_data:
                    print(f"{ele.county}, {ele.state}")
                    print(f"        Population: {ele.population.get('2014 Population')}\n")
                    print("         Age:")
                    print(f"                < 5: {ele.age.get('Percent Under 5 Years')}%")
                    print(f"                < 18: {ele.age.get('Percent Under 18 Years')}%")
                    print(f"                > 65: {ele.age.get('Percent 65 and Older')}%\n")
                    print("         Education")
                    print(f"                >= High School: {ele.education.get('High School or Higher')}%")
                    print("                >= Bachelor's: " + str(ele.education.get("Bachelor's Degree or Higher")) + "%")
                    print(" ")
                    print("         Ethnicity Percentages")
                    print(f"                American Indian and Alaska Native Alone: {ele.ethnicities.get('American Indian and Alaska Native Alone')}%")
                    print(f"                Asian Alone: {ele.ethnicities.get('Asian Alone')}%")
                    print(f"                Black Alone: {ele.ethnicities.get('Black Alone')}%")
                    print(f"                Hispanic or Latino: {ele.ethnicities.get('Hispanic or Latino')}%")
                    print(f"                Native Hawaiian and Other Pacific Islander Alone: {ele.ethnicities.get('Native Hawaiian and Other Pacific Islander Alone')}%")
                    print(f"                Two or More Races: {ele.ethnicities.get('Two or More Races')}%")
                    print(f"                White Alone: {ele.ethnicities.get('White Alone')}%")
                    print(f"                White Alone, not Hispanic or Latino: {ele.ethnicities.get('White Alone, not Hispanic or Latino')}%\n")
                    print("         Income")
                    print(f"                Median Household Income: {ele.income.get('Median Household Income')}")
                    print(f"                Per Capita: {ele.income.get('Per Capita Income')}")
                    print(f"                Below Poverty Level: {ele.income.get('Persons Below Poverty Level')}% \n")

            elif "filter-state" in line:
                x = line.split(":")
                y = x[1].strip("\n")
                full_data = hw4.filterByState(full_data, y)
                print(f"Filter: state == {y} {hw4.filterByState(full_data, y)}")
                print(len(hw4.filterByState(full_data, y)))
            elif "filter-gt" in line:
                x = line.split(":")
                y = x[1].split(".")
                if "Education" in y[0]:
                    full_data = hw4.educationGreaterThan(full_data, y[1], float(x[2]))
                    print(f"Filter: {y[1]} gt {x[2]} ({len(full_data)} entries)")
                elif "Ethnicities" in y[0]:
                    full_data = hw4.ethnicityGreaterThan(full_data, y[1], float(x[2]))
                    print(f"Filter: {y[1]} gt {x[2]} ({len(full_data)} entries)")
                elif "Income" in y[0]:
                    full_data = hw4.belowPovertyLevelGreaterThan(full_data, float(x[2]))
                    print(f"Filter: {y[1]} gt {x[2]} ({len(full_data)} entries)")
            elif "filter-lt" in line:
                x = line.split(":")
                y = x[1].split(".")
                if "Education" in y[0]:
                    full_data = hw4.educationLessThan(full_data, y[1], float(x[2]))
                    print(f"Filter: {y[1]} lt {x[2]} ({len(full_data)} entries)")
                elif "Ethnicities" in y[0]:
                    full_data = hw4.ethnicityLessThan(full_data, y[1], float(x[2]))
                    print(f"Filter: {y[1]} lt {x[2]} ({len(full_data)} entries)")
                elif "Income" in y[0]:
                    full_data = hw4.belowPovertyLevelLessThan(full_data, float(x[2]))
                    print(f"Filter: {y[1]} lt {x[2]} ({len(full_data)} entries)")
            elif "population-total" in line:
                print (f"2014 population:  {hw4.populationTotal(full_data)}")
            elif "population" in line:
                x = line.split(":")
                y = x[1].split(".")
                z = y[1].strip("\n")
                if "Education" in y[0]:
                    print(f"2014 {z} population: {hw4.populationByEducation(full_data, z)}")
                elif "Ethnicities" in y[0]:
                    print(f"2014 {z} population: {hw4.populationByEthnicity(full_data, z)}" )
                elif "Income" in y[0]:
                    print(f"2014 {z} population: {hw4.populationBelowPovertyLevel(full_data)}" )
            elif "percent" in line:
                a = line.split(".")
                b = line.split(":")
                # print(line)
                # print(a[0])
                # print(a[1])
                if "Education" in line:
                    x = a[1].split("\n")
                    y = x[0]
                    b = str(y)
                    # b = str(a[1].split("\n")[0])
                    print(f"2014 {a[1]} percentage: {hw4.percentByEducation(full_data, b)}")
                elif "Ethnicities" in line:
                    b = str(a[1].split("\n")[0])
                    print(f"2014 {a[1]} percentage: {hw4.percentByEthnicity(full_data, b)}")
                elif "Income" in line:
                    b = str(a[1].split("\n")[0])
                    print(f"2014 {a[1]} percentage: {hw4.percentBelowPovertyLevel(full_data)}")
    except ValueError:
        print("error")
    except FileNotFoundError:
        print("No File error")