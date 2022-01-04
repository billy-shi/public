#! /usr/bin/python

"""
/////////// Description

Version 1.0

Author: Billy Shi
Date: Jan 3, 2022
"""

import numpy as np
import pandas as pd
import matplotlib as mat

# load data from uk.gov public databases
# links obtained on Jan 2, 2022; links should auto update
url="https://api.coronavirus.data.gov.uk/v2/data?areaType=utla&metric=cumVaccinationFirstDoseUptakeByVaccinationDatePercentage&format=csv"
vaccinated = pd.read_csv(url)
uk_schools = pd.read_csv(r"uk_schools_data_01jan2022.csv")

# select only relevant columns of data
uk_schools = uk_schools[['location', 'location_code', 'number_of_schools']]
vaccinated = vaccinated[['areaCode', 'areaName', 'date', 'cumVaccinationFirstDoseUptakeByVaccinationDatePercentage']]
vaccinated = vaccinated.drop_duplicates(subset='areaCode')
# merge datasets and verify merge
dataset = pd.merge(uk_schools, vaccinated, left_on = 'location_code', right_on = 'areaCode')
dataset['validation'] = np.where(dataset['location'] == dataset['areaName'], True, False)
# to manually check area name misfit
# print(dataset.loc[dataset['validation']==False])

