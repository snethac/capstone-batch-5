# capstone-batch-5


# Problem statement

DVD rental analysis

Our problem statements include 

1. Top 10 customers analysis

2. Most rented films
# Methodology

Data for DVD rental analysis is taken from postgress sql.

This data contains information about customers who have rented the films, customer information like name address, categories of films, languages of films, rental information, film information, stores information, actors iformation, and payment details.

Master table is created to get the required amount of datafrom overall data by running a sql query by joining all the required tables.

After creating the master table EDA is done in python.

using the data in Master table dashboards are created in Tableau for our problem statements.

# Links to dashboards

[Dashboards](https://public.tableau.com/app/profile/snetha.c/viz/capstonestatement2/firstnameandcountoffilm_id?publish=yes "Dasboards")
 
 ## Descriptions of dashboards and worksheets 

 In the above url of dashboards contains analysis of top 10 customers and most rented films.

 Top 10 customers are analysed based on rentals they have taken, amount paid by them,  and in each country top customers and based on category of films.

 simillarly most rented film analysis is done based on film rating, and montly rentals of films.

 # EDA Outputs

 Rental duration is uniformly distributed

 Amount paid by customers and if we look closely at the data we can see that a lot of data points are distributed uniformly.

 There are 183 null values in the data after creating master table those null values are beacuse of customers not returning the rental


​

 # Insights and Recommendation
 #### Rental Analysis
 ***
 We can apply some penalty/late fee forthose who return late.

We can make rent price slab according to number of days or hours of rent duration.

#### Top 10 customer
***
Give them gift cards , special discounts, gift hampers & certificate of appreciation.

Upload their pics with name and positive reviews on sites.

#### Country wise sales revenue (MAP)
***

Focus on those countries where service is not available.

Focus on those countries that have large population but not generate a good amount of revenue, so more advertise will be good for increase revenue.



 # Files and Folders

 ### SQL Query
 [SQL Query for Master Table](https://github.com/snethac/capstone-batch-5/blob/master-table/Master%20table.txt "Master Table")

 ### Python Code 

 [Python code for EDA](https://github.com/snethac/capstone-batch-5/blob/EDA-analysis/EDA%20Analysis_Updated.py "EDA analysis")

 ### Images from EDA

 [Snapshots of EDA Anlysis](https://github.com/snethac/capstone-batch-5/tree/EDA-analysis "snapshots")

 ### Final Presentation

 [click here for ppt](https://github.com/snethac/capstone-batch-5/blob/final-presentation/Final%20PPT%20(2).pptx "final ppt")
