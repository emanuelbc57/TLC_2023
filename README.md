# 2023 YELLOW TAXI TRIP DATA PROJECT

## Objectives
This project aims on:
- Describing key characteristics of the data
- Performing data exploration, cleaning, hypothesis testing about which features of the data influence the most on the total amount charged to passengers in a trip
- Create a Machine Learning (ML) model to predict fares for new data performing cross validation and testing for all models accessed

## About the data

The data used in this project is a sample of 1,915,511 observations (berofe data cleaning) from the "2023 Yellow Taxi Trip Data" data-set available on <https://data.cityofnewyork.us/Transportation/2023-Yellow-Taxi-Trip-Data/4b4i-vvec/data_preview>. The sample was made using the code available in the ```./data/raw/sampling_tlc_2023.py``` python script. If you wish to replicate the sample, remember to use your own Socrata keys and token and to install ```polars``` and ```sodapy``` libraries before performing sample. The license of the dataset is unespecified but, as mentioned, the data is publicly available in the NYC Open Data website.

### Columns and datatypes (this information is available in the documentation of the dataset)
To more detailed information, see the ```Yellow_Taxi_Trip_Data_Data_Dictionary.xlsx``` attachment available on <https://data.cityofnewyork.us/Transportation/2023-Yellow-Taxi-Trip-Data/4b4i-vvec/about_data>

- **vendorid:**	A code indicating the provider of the data - 1=Creative Mobile Technologies, LLC 2=VeriFone Inc.
- **tpep_pickup_datetime:**	The date and time when the meter was engaged.
- **tpep_dropoff_datetime:** The date and time when the meter was disengaged.
- **passenger_count:** The number of passengers in the vehicle reported by the driver. 
- **trip_distance:** The elapsed trip distance in miles reported by the taximeter.	
- **ratecodeid:** The final rate code in effect at the end of the trip. - 1= Standard rate 2= JFK 3= Newark 4= Nassau or Westchester 5= Negotiated fare 6= Group ride 99 = Null/unknown
- **store_and_fwd_flag:** This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka “store and forward,” because the vehicle did not have a connection to the server - Y= store and forward trip N= not a store and forward trip
- **pulocationid:** TLC Taxi Zone in which the taximeter was engaged
- **dolocationid:**	TLC Taxi Zone in which the taximeter was disengaged	
- **payment_type:**	Says how the passenger paid for the trip - 0= Flex Fare trip 1= Credit card 2= Cash 3= No charge 4= Dispute 5= Unknown 6= Voided trip
- **fare_amount:**	The time-and-distance fare calculated by the meter.
- **extra:** Miscellaneous extras and surcharges.
- **mta_tax:** Tax that is automatically triggered based on the metered rate in use.
- **tip_amount:** Tip amount, automatically populated for credit card tips, cash tips are not included.	
- **tolls_amount:**	Total amount of all tolls paid in trip.	
- **improvement_surcharge:** Improvement surcharge assessed trips at the flag drop. The improvement surcharge began being levied in 2015.	
- **total_amount:**	The total amount charged to passengers. Does not include cash tips.	
- **congestion_surcharge:**	Total amount collected in trip for NYS congestion surcharge.
- **airport_fee:** For pick up only at LaGuardia and John F. Kennedy Airports.	

The ```tpep_pickup_datetime``` and ```tpep_dropoff_datetime:``` are date-time columns.
The ```store_and_fwd_flag``` is a categorical variable
All the other columns are numerical data, where ```passenger_count, pulocationid, dolocationid,``` and ```payment_type,``` are encoded data and shall be treated as categorical in the analysis.

More information about data recording, completedeness and reliability can be consulted on <https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page>.

### Geografical Data
As one may expect, PULocationID and DOLocationID variables are associated with geographical points, the analysis regarding these variables will be conducted using the shapefiles provided by TLC in the link <https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page>

## Personal notes on the project:

This project is inspired on one of the projects of the Google Advanced Data Analytics Professional Certificate available on Coursera (The Automatidata Case Scenario). The workflow used here though will not be the same as proposed there, neither the data used is the same (the Automatidata case scenario uses a sample of the "2017 Yellow Taxi Trip Data" dataset.

## Abbreviations used in the project
(This section will be completed as the project advances)

