# ihmistenLuonti
Python excercise that creates random finnish people. Create dummy persons, their (obv. fake) contact information and formally correct social security numbers. It takes about half an hour to create the finnish population (roughly 5.5 million).


### Usage
The program asks for the amount of people you want to create and starts executing. Once it's done, it asks whether or not you would like to save the file. After naming the file (no need to give an extension) you can choose if you want to save the file as .txt or .csv.

### Import data to database from CSV (MariaDB / MySQL)

First, create table with the following command: 
create table asiakkaat (Etunimi VARCHAR(30) NOT NULL, Sukunimi VARCHAR(30) NOT NULL, Syntymaaika VARCHAR(10) NOT NULL, Henkilotunnus VARCHAR(11) NOT NULL, Katuosoite VARCHAR(30) NOT NULL, Postinumero_ja_toimipaikka VARCHAR(30) NOT NULL, Puhelinnumero VARCHAR(30) NOT NULL);
(replace "asiakkaat" with the name you want to give the table)

Then, import data from the CSV-file:
LOAD DATA LOCAL infile '/root/Python/ihmistenLuonti/viisimiljoonaa.csv' INTO TABLE asiakkaat FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
(replace "asiakkaat" with your table's name and the path '/root/Python/ihmistenLuonti/viisimiljoonaa.csv' with the one you have saved your file to)

