# Data-Visualization-using-Flask

 Topic: Lyme: Visualizing Disease Spread

Questions:
1.	Can you visualize the number of dengue fever cases reported each week in Colorado Counties for the years 2002 to 2004?
2.	Can you visualize the number of dengue cases each week (in each location) based on environmental variables describing changes in temperature, precipitation and humidity?

Dataset:
The data has taken from drivenData.org, it was released as a part of their competition DengAI.
Dataset from the competition has only 2 cities Sanjuan and Iquitos, but we have added three more cities Cusco, Tijuana and Rosario with random precipitation, humidity and temperature.
Dengue fever is a mosquito-borne disease that occurs in tropical and sub-tropical parts of the world. In mild cases, symptoms are similar to the flu: fever, rash, and muscle and joint pain. In severe cases, dengue fever can cause severe bleeding, low blood pressure, and even death. Because it is carried by mosquitoes, the transmission dynamics of dengue are related to climate variables such as temperature and precipitation. An understanding of the relationship between climate and dengue dynamics can improve research initiatives and resource allocation to help fight life-threatening pandemics.

Our data contains Climatic variables such as precipitation, temperature, humidity for each City. And also, we have total cases of Dengue Affected Cases for the Corresponding Year and Week of the Year.

Column Names:
1.	City- Name of the city
2.	Year-Dengue Affected Year
3.	Weekofyear-Week of the Year 
4.	week_start_date-Week start data in the format mm-dd-yy
5.	avg_temp- Average air temperature according to Climate Forecast System Reanalysis                             measurements (0.5x0.5-degree scale).
6.	precip_amt-Total Precipitation amount according to Climate Forecast System Reanalysis                                measurements (0.5x0.5-degree scale).
7.	Humidity_amt-Mean Specific humidity according to Climate Forecast System Reanalysis                                        measurements (0.5x0.5-degree scale).
8.	total_cases- Total cases predicted.


