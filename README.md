Justin Penner
Student ID: s2310787025

Sample call statements
-----------------------
python3 s2310787025.py
>> this will run in default mode and ask the user to select from road surfaces with
>> know coefficients of friction (can select multiple different road surfaces).

python3 s2310787025.py --friction=0.18
>> will run simulation with only the defined (ex. 0.18) coefficient of friction

python3 s2310787025.py -f=0.18
>> alternative naming to define friction coefficient

Description
------------
If the program is called without any input, will ask user to choose from list of
know road surface friction coefficients. An alternative user defined value can also
be defined as shown in the above sample call statements. The terminal will then
ask for input from user on vehicle mass, an initial vehicle speed, and a selected
road type. It then uses this information to simulate how long it will take for the
vehicle to come to a standstill along with the traveled distance. Losses taken into
consideration are: rolling resistance, and aerodynamic resistance.

Output
------
Creates a figure with two subplots. The first contains a plot of the vehicle velocity
over time and the second the travelled distance over time.
