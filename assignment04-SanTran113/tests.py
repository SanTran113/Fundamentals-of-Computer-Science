# Name: San Tran
# Date: 11 / 9 / 22
# GitHub: SanTran113

import build_data
import unittest
import hw4

full_data = build_data.getData()

reduced_data = [
    build_data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    build_data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    build_data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    build_data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    build_data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    build_data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    build_data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

sample_data = [
    build_data.CountyDemographics(
    # age
    {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
    # county
    'San Luis Obispo County',
    # education
    {"Bachelor's Degree or Higher": 31.5,
               'High School or Higher': 89.6},
    # ethnicities
    {'American Indian and Alaska Native Alone': 1.4,
                 'Asian Alone': 3.8,
                 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4,
                 'White Alone': 89.0,
                 'White Alone, not Hispanic or Latino': 69.5},
    # income
    {'Median Household Income': 58697,
            'Per Capita Income': 29954,
            'Persons Below Poverty Level': 14.3},
    # population
    {'2010 Population': 269637,
                '2014 Population': 279083,
                'Population Percent Change': 3.5,
                'Population per Square Mile': 81.7},
    # state
    'CA'
)
]

class TestCases(unittest.TestCase):
    pass

# Part 1
    def test_populationTotal_eq_1(self):
        l = full_data
        self.assertEqual(318857056, hw4.populationTotal(l))

    def test_populationTotal_eq_2(self):
        l = reduced_data
        self.assertEqual(655813, hw4.populationTotal(l))

# Part 2
    def test_filterByState_eq_1(self):
        l = full_data
        abb = 'CA'
        self.assertEqual(len(hw4.filterByState(l, abb)), 58)

    def test_filterByState_eq_2(self):
        l = reduced_data
        abb = 'NY'
        self.assertEqual((hw4.filterByState(l, abb)), [])

# Part 3
# test populationByEducation
    def test_populationByEducation_eq_1(self):
        l = sample_data
        edu = "Bachelor's Degree or Higher"
        self.assertEqual(87911.145, hw4.populationByEducation(l, edu))

    def test_populationByEducation_eq_2(self):
        l = full_data
        edu = "Bachelor's Degree or Higher"
        self.assertEqual(92216021.02199993, hw4.populationByEducation(l, edu))

    def test_populationByEducation_eq_3(self):
        l = full_data
        edu = "Master's Degree"
        self.assertEqual(0, hw4.populationByEducation(l, edu))

# test populationByEthnicity
    def test_populationByEthnicity_eq_1(self):
        l = full_data
        ethn = "Other"
        self.assertEqual(0, hw4.populationByEthnicity(l, ethn))
    def test_populationByEthnicity_eq_2(self):
        l = sample_data
        ethn = "Two or More Races"
        self.assertEqual(9488.822, hw4.populationByEthnicity(l, ethn))
    def test_populationByEthnicity_eq_3(self):
        l = full_data
        ethn = "Asian Alone"
        self.assertEqual(17346856.558999952, hw4.populationByEthnicity(l, ethn))

    # test populationBelowPovertyLevel
    def test_populationBelowPoverty_eq_1(self):
        l = sample_data
        self.assertEqual(39908.869, round(hw4.populationBelowPovertyLevel(l), 3))

    def test_populationBelowPoverty_eq_2(self):
        l = full_data
        self.assertEqual(48996488.474, round(hw4.populationBelowPovertyLevel(l), 3))

# Part 4
# test percenByEducation
    def test_percentByEducation_eq_1(self):
        l = sample_data
        edu = "Bachelor's Degree or Higher"
        self.assertEqual(31.5, hw4.percentByEducation(l, edu))

    def test_percentByEducation_eq_2(self):
        l = reduced_data
        edu = "Bachelor's Degree or Higher"
        self.assertEqual(29.751482663503165, hw4.percentByEducation(l, edu))

    def test_percentByEducation_eq_3(self):
        l = sample_data
        edu = "Master's Degree or Higher"
        self.assertEqual(0, hw4.percentByEducation(l, edu))

# test percentByEthnicity
    def test_percentByEtnicity_eq_1(self):
        l = sample_data
        ethn = "Two or More Races"
        self.assertEqual(3.4, round(hw4.percentByEthnicity(l, ethn), 1))

    def test_percentByEthnicity_eq_2(self):
        l = full_data
        ethn = 'Black Alone'
        self.assertEqual(13.2, round(hw4.percentByEthnicity(l, ethn), 1))

    def test_percentByEthnicity_eq_3(self):
        l = reduced_data
        ethn = "Other"
        self.assertEqual(0, round(hw4.percentByEthnicity(l, ethn), 1))

# test percentBelowPovertyLevel
    def test_percentBelowPoverty_eq_1(self):
        l = sample_data
        self.assertEqual(14.3, round(hw4.percentBelowPovertyLevel(l), 3))

    def test_percentBelowPoverty_eq_2(self):
        l = full_data
        self.assertEqual(15.366, round(hw4.percentBelowPovertyLevel(l), 3))

# Part 5
# test educationGreaterThan
    def test_educationGreaterThan_eq_1(self):
        l = sample_data
        edu = "Bachelor's Degree or Higher"
        num = 30.0
        self.assertEqual(1, len(hw4.educationGreaterThan(l, edu, num)))

    def test_educationGreaterThan(self):
        l = reduced_data
        edu = "Bachelor's Degree or Higher"
        num = 20.0
        self.assertEqual(3, len(hw4.educationGreaterThan(l, edu, num)))

# test educationLessThan
    def test_educationLessThan_eq_1(self):
        l = sample_data
        edu = "Bachelor's Degree or Higher"
        num = 30.0
        self.assertEqual(0, len(hw4.educationLessThan(l, edu, num)))

    def test_educationLessThan(self):
        l = reduced_data
        edu = "High School or Higher"
        num = 90.0
        self.assertEqual(6, len(hw4.educationLessThan(l, edu, num)))

# test ethnicityGreaterThan
    def test_ethnicityGreaterThan_eq_1(self):
        l = sample_data
        ethn = "Hispanic or Latino"
        num = 20.0
        self.assertEqual(1, len(hw4.ethnicityGreaterThan(l, ethn, num)))

    def test_ethnicityGreaterThan_eq_2(self):
        l = reduced_data
        ethn = 'White Alone'
        num = 90.0
        self.assertEqual(4, len(hw4.ethnicityGreaterThan(l, ethn, num)))

# test ethnicityLessThan
    def test_ethnicityLessThan_eq_1(self):
        l = sample_data
        ethn = 'Native Hawaiian and Other Pacific Islander Alone'
        num = 1.0
        self.assertEqual(1, len(hw4.ethnicityLessThan(l, ethn, num)))

    def test_ethnicityLessThan_eq_2(self):
        l = reduced_data
        ethn = 'White Alone'
        num = 90.0
        self.assertEqual(3, len(hw4.ethnicityLessThan(l, ethn, num)))

# test belowPovertyLevelGreaterThan
    def test_belowPovertyLevelGreaterThan_eq_1(self):
        l = sample_data
        num = 10.0
        self.assertEqual(1, len(hw4.belowPovertyLevelGreaterThan(l, num)))

    def test_belowPovertyLevelGreaterThan_eq_2(self):
        l = reduced_data
        num = 15.0
        self.assertEqual(4, len(hw4.belowPovertyLevelGreaterThan(l, num)))

# test belowPovertyLevelLessThan
    def test_belowPovertyLevelLessThan_eq_1(self):
        l = sample_data
        num = 10.0
        self.assertEqual(0, len(hw4.belowPovertyLevelLessThan(l, num)))

    def test_belowPovertyLevelLessThan_eq_2(self):
        l = reduced_data
        num = 15.0
        self.assertEqual(3, len(hw4.belowPovertyLevelLessThan(l, num)))


if __name__ == '__main__':
    unittest.main()
