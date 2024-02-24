# Name: San Tran
# Date: 11 / 9 / 22
# GitHub: SanTran113

from typing import List
import build_data

# Part 1
def populationTotal(l: List[build_data.CountyDemographics]) -> int:
    """
    For each county(dictionary) in the l list,
    add the 2014 population data into the totalSum variable

    Type Annotations:
        l (List(CountyDemographics)): list of county dictionaries
        with specific demographics

    Returns:
          int: Sum of population of counties in the list l

    """
    totalSum = 0
    for county in l:
        totalSum += county.population.get('2014 Population')
        #print(county.population)
        #print(totalSum)
    return totalSum


# Part 2
def filterByState(l: List[build_data.CountyDemographics], abb: str) -> List[build_data.CountyDemographics]:
    """
    Check each county in the list l in the state abbrivation is in the county's dictionary

    Type Annotations:
        l(List(CountyDemographics)): county dictionaries with specific demographics
        abb (str): abbreviation of state

     Returns:
        List(CountyDemographics): county dictionaries
        with specific demographics
            Testing for number of counties in the list(l) that are in the specific state(abb)

     """
    countyList = []
    for counties in l:
        if abb in counties.state:
            countyList.append(counties)
    return countyList


# Part 3
def populationByEducation(l: List[build_data.CountyDemographics], edu: str) -> float:
    """
    Because the county of education is in percentage form I will divide it by 100
     to get fraction in decimal form,then multiply it with the total population
     to get the accurate population count within that percentage.
     Then I will add it into the totalSum variable.

    Type Annotations:
        l(List(CountyDemographics)): county dictionaries with specific demographics
        edu (str): education level of interest

    Returns:
        float: total 2014 population of all peoples in the list of counties
        that is within the education level of interest

    """

    totalSum = 0
    for county in l:
        if edu in county.education:
            x = county.education.get(edu) / 100
            num = county.population.get("2014 Population") * x
            totalSum += num
        else:
            totalSum = 0
    return totalSum

def populationByEthnicity(l: List[build_data.CountyDemographics], ethn: str) -> float:
    """
    Because the county measuring ethnicities is in percentage form I will divide it by 100
     to get fraction in decimal form,then multiply it with the total population
     to get the accurate population count within that percentage.
     Then I will add it into the totalSum variable.

    Type Annotations:
        l(List(CountyDemographics)): county dictionaries with specific demographics
        ethn (str): ethnicity of interest

    Returns:
        float: total 2014 population of all peoples in the list of counties
        that is within the ethnicity of interest

    """
    totalSum = 0
    for county in l:
        if ethn in county.ethnicities:
            x = county.ethnicities.get(ethn) / 100
            num = county.population.get("2014 Population") * x
            totalSum += num
        else:
            totalSum = 0
    return totalSum

def populationBelowPovertyLevel(l: [build_data.CountyDemographics]) -> float:
    """
    Because the county measuring income of "Persons Below Poverty Level"
     is in percentage form I will divide it by 100 to get fraction in decimal form,
     then multiply it with the total population
     to get the accurate population count within that percentage.
     Then I will add it into the totalSum variable.

    Type Annotations:
        l(List(CountyDemographics)): county dictionaries with specific demographics

    Returns:
        float: total 2014 population of all peoples in the list of counties
        that is within the key "Persons Below Poverty Level"

    """
    totalSum = 0
    for county in l:
        x = county.income.get('Persons Below Poverty Level') / 100
        num = county.population.get("2014 Population") * x
        totalSum += num
    return totalSum

# Part 4

def percentByEducation(l: List[build_data.CountyDemographics], edu: str) -> float:
    """
    Because the county of education is in percentage form I will divide it by 100
     to get fraction in decimal form,then multiply it with the total population
     to get the accurate population count within that percentage.
     Then I will add it into the totalSum variable, while adding each population
     of each county as I go through the list. At the end I will divide
     the totalSum with the total population. If the key in interest does
     not exist the total percent will be 0.

      Type Annotations:
        l(List(CountyDemographics)): county dictionaries with specific demographics
        edu (str): education level of interest

    Returns:
        float: percent of 2014 population of all peoples in the list of counties
        that is within the education level of interest
    """
    totalSum = 0
    totalPop = 0
    for county in l:
        if edu in county.education:
            # print(county.education)
            x = county.education.get(edu) / 100
            num = county.population.get("2014 Population") * x
            totalSum += num
            totalPop += county.population.get("2014 Population")
        else:
            totalSum = 0
            totalPop = 1
        #print(f"total sum: {totalSum}")
        #print(county.population.get("2014 Population"))
        totalPercent = totalSum / totalPop * 100
        #print(totalPercent)
    return totalPercent

def percentByEthnicity(l: List[build_data.CountyDemographics], ethn: str) -> float:
    """
    Because the county of ethnicity is in percentage form I will divide it by 100
     to get fraction in decimal form,then multiply it with the total population
     to get the accurate population count within that percentage.
     Then I will add it into the totalSum variable, while adding each population
     of each county as I go through the list. At the end I will divide
     the totalSum with the total population. If the key in interest does
     not exist the total percent will be 0.

    Type Annotations:
        l(List(CountyDemographics)): county dictionaries with specific demographics
        ethn (str): ethnicity of interest

    Returns:
        float: percent of 2014 population of all peoples in the list of counties
        that is within the ethnicity of interest
    """
    totalSum = 0
    totalPop = 0
    for county in l:
        if ethn in county.ethnicities:
            x = county.ethnicities.get(ethn) / 100
            num = county.population.get("2014 Population") * x
            totalSum += num
            totalPop += county.population.get("2014 Population")
        else:
            totalSum = 0
            totalPop = 1
        totalPercent = totalSum / totalPop * 100
    return totalPercent

def percentBelowPovertyLevel(l: List[build_data.CountyDemographics]) -> float:
    """
    Because the county measuring income of "Persons Below Poverty Level"
     is in percentage form I will divide it by 100 to get fraction in decimal form,
     then multiply it with the total population
     to get the accurate population count within that percentage.
     Then I will add it into the totalSum variable, while adding each population
     of each county as I go through the list. At the end I will divide
     the totalSum with the total population.

    Type Annotations:
        l(List(CountyDemographics)): county dictionaries with specific demographics

    Returns:
        float: total 2014 population of all peoples in the list of counties
        that is within the key "Persons Below Poverty Level"

    """
    totalSum = 0
    totalPop = 0
    for county in l:
        x = county.income.get('Persons Below Poverty Level') / 100
        num = county.population.get("2014 Population") * x
        totalSum += num
        totalPop += county.population.get("2014 Population")
    totalPercent = totalSum / totalPop * 100
    return totalPercent


# Part 5
def educationGreaterThan(l: List[build_data.CountyDemographics], edu: str, num: float) -> List[build_data.CountyDemographics]:
    """
    We are checking for every county in the list l and if the key(edu) is in the county(dictionary)
    and if the key is greater than the numerical value of comparison (num) than add it into the empty list(counties)

    Type Annotations:
        l(List(CountyDemographics)): county dictionaries with specific demographics
        edu (str): education level of interest
        num (float): numerical value for comparison

    Returns:
    List(CountyDemographics): county dictionaries that is greater than the numerical value and
    in the education level of interest
        Testing for number of counties in the list(l) of the return
    """
    counties = []
    for county in l:
        if edu in county.education:
            if county.education.get(edu) > num:
                counties.append(county)
    return counties

def educationLessThan(l: List[build_data.CountyDemographics], edu: str, num: float) -> List[build_data.CountyDemographics]:
    """
    We are checking for every county in the list l and if the key(edu) is in the county(dictionary)
    and if the key is less than the numerical value of comparison (num) than add it into the empty list(counties)

    Type Annotations:
        l(List(CountyDemographics)): county dictionaries with specific demographics
        edu (str): education level of interest
        num (float): numerical value for comparison

    Returns:
    List(CountyDemographics): county dictionaries that is less than the numerical value and
    in the education level of interest
        Testing for number of counties in the list(l) of the return
    """
    counties = []
    for county in l:
        if edu in county.education:
            if county.education.get(edu) < num:
                counties.append(county)
    return counties

def ethnicityGreaterThan(l: List[build_data.CountyDemographics], ethn: str, num: float) -> List[build_data.CountyDemographics]:
    """
    We are checking for every county in the list l and if the key(ethn) is in the county(dictionary)
    and if the key is greater than the numerical value of comparison (num) than add it into the empty list(counties)

    Type Annotations:
        l(List(CountyDemographics)): county dictionaries with specific demographics
        ethn (str): ethnicity of interest
        num (float): numerical value for comparison

    Returns:
    List(CountyDemographics): county dictionaries that is greater than the numerical value and
    in the ethnicity of interest
        Testing for number of counties in the list(l) of the return
    """
    counties = []
    for county in l:
        if ethn in county.ethnicities:
            if county.ethnicities.get(ethn) > num:
                counties.append(county)
    return counties

def ethnicityLessThan(l: List[build_data.CountyDemographics], ethn: str, num: float) -> List[build_data.CountyDemographics]:
    """
    We are checking for every county in the list l and if the key(ethn) is in the county(dictionary)
    and if the key is less than the numerical value of comparison (num) than add it into the empty list(counties)

    Type Annotations:
        l(List(CountyDemographics)): county dictionaries with specific demographics
        ethn (str): ethnicity of interest
        num (float): numerical value for comparison

    Returns:
    List(CountyDemographics): county dictionaries that is less than the numerical value and
    in the ethnicity of interest
        Testing for number of counties in the list(l) of the return
    """
    counties = []
    for county in l:
        if ethn in county.ethnicities:
            # print(county.ethnicities)
            if county.ethnicities.get(ethn) < num:
                counties.append(county)
    return counties

def belowPovertyLevelGreaterThan(l: List[build_data.CountyDemographics], num: float) -> List[build_data.CountyDemographics]:
    """
    We are checking for every county in the list l and if "Persons Below Poverty Level" is in the county(dictionary)
    and if the key is greater than the numerical value of comparison (num) than add it into the empty list(counties)

    Type Annotations:
        l(List(CountyDemographics)): county dictionaries with specific demographics
        num (float): numerical value for comparison

    Returns:
    List(CountyDemographics): county dictionaries that is greater than the numerical value and
    in "Persons Below Poverty Level" in the income category
        Testing for number of counties in the list(l) of the return
    """
    counties = []
    for county in l:
        if county.income.get("Persons Below Poverty Level") > num:
            counties.append(county)
    return counties

def belowPovertyLevelLessThan(l: List[build_data.CountyDemographics], num: float) -> List[build_data.CountyDemographics]:
    """
    We are checking for every county in the list l and if "Persons Below Poverty Level" is in the county(dictionary)
    and if the key is less than the numerical value of comparison (num) than add it into the empty list(counties)

    Type Annotations:
        l(List(CountyDemographics)): county dictionaries with specific demographics
        num (float): numerical value for comparison

    Returns:
    List(CountyDemographics): county dictionaries that is less than the numerical value and
    in "Persons Below Poverty Level" in the income category
        Testing for number of counties in the list(l) of the return
    """
    counties = []
    for county in l:
        if county.income.get("Persons Below Poverty Level") < num:
            counties.append(county)
    return counties
