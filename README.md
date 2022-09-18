# **Airbnb Recommendation System**
## *Aim of the project*
To build a recommender for Airbnbs in Western Cape, South Africa based on guest preferences i.e location, number of bedrooms, amenities etc
![](https://th.bing.com/th/id/R.b7026f03d76d7999d642c57bd86051dd?rik=ayFeV62qBnDLFw&riu=http%3a%2f%2flatfusa.com%2fmedia%2fuploads%2f2020%2f12%2f10%2fairbnb-678x381.jpg&ehk=ygq%2b0vwi%2fzEoTYEvWfsJBqmk%2fkR5qvJOeZ21pB3tL2o%3d&risl=&pid=ImgRaw&r=0)
# Overview
**What is Airbnb?**
Airbnb is an online marketplace that connects people who want to rent out their homes with people who are looking for accommodations in specific locales. The company was founded in 2007. <a href = "https://news.airbnb.com/about-us/">According to Airbnb</a>, the company has over 6 million active listings worldwide, in over 100k cities in more than 220 countries. It has revolutionized the hospitality industry, a paradigm shift from hotels and hostels to a wide variety of staying options. Travellers can choose from luxury homes, to boats to quirky spaces like these listed in this <a href = "https://www.dwell.com/article/unique-airbnb-fund-weirdest-home-rentals-e665f737">article</a>
# **Business Understanding**
Guest and host experiences are essential for the success of this industry. Customers want to have a five star experience when they check into the airbnbs. According to a consumer survey commissioned by Airbnb, the majority of travelers say amenities are a top priority for a great trip. This is even more important now, as guests search for longer stays. On the other hand, the hosts want to get as many customers as possible. What’s more, guests often filter their search results to find 10 top amenities. To stand out in search results, the hosts must make sure they’re adding or updating their amenities to include these in their listing if they have them.

## **Problem Statement**
Preferences, features and amenities might change with time,and someone has to be on their toes to keep up. As a consulting company, we plan to keep our clients(the airbnb hosts) upto date with the industry changes and help them know how to get and maintain the coveted 5-star rating and become Superhosts.

The guests are a big part of the industry. In the airbnb listing sites, a user is limited to just choosing from the amenities and features given. They aren’t given a choice to write a description of what they want. Our company is looking to optimize user experience by having  a recommendation system with the possibility to choose features already present and/or write a description of what they want.
 ### Main Objectives
1.) To do an analysis of South africa Airbnb data comparing superhosts and standard hosts.

2.) To build a content-based recommendation system for Airbnbs in Cape Town and Western Cape areas in South Africa. 

### Specific Objectives


# **Data Understanding**
## Data
Data was obtained <a href = "http://insideairbnb.com/get-the-data/">Inside Airbnb</a>. Data has two csv files listings which contains 18903 records and 74 features that give information about each listing in western cape and host information. The reviews file has 363,065 rows and 6 columns which provide guest information and their reviews of the airbnb they stayed at.

## Data Preparation
Data was cleaned and preprocessed before developing a recommender system. Columns with null values of more than 40% were dropped, the rest were imputed with median, unknown, empty string.

## **Exploratory Data Analysis**
Superhosts have a higher rating compared to non superhosts. Through data exploration the following insights were identified:
Hosts with higher ratings have a response time of  within an our, have top rated amenities sucha as Wifi, Long Term Stay, Kitchen and its essentials, Hair Dryer, Dishwasher, Washer, Iron, Fire Extinguisher, Private Entrance, Free Parking, First Aid Kit
The most frequently used double words include:

![](https://github.com/Rachael-Osoro/Git-Practice-2/blob/main/images/frequent_words.png)
