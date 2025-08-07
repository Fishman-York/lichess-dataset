# lichess-dataset
Lichess Dataset Observation

Current Goals:
1. Import Database from the csv file to postgresql
2. Correlate Relative Ratings of white and black players to winrate
3. Correlate resignation rate affected by player rating and opponents
4. Train a classifier which predicts player win rate based on other inputs
5. Visualisation of data

Observations of Dataset:
When importing the csv file into postgre, created_at and last_move_at are in the form of x.xxxxxE+12. This is a timestamp, so I tried to store it as bigint, but ended up having to import it as text.

The field 'moves' is a very long string of chess moves like 'A5 E3 D2' and so on. Originally attempted to store it as Varchar, but upon further research its better to use text for a datatype unless you need to verify length of string.

Tried to use the field 'id' as primary key, but found duplicate entries. Upon checking the fields such as white id, black id, , it is not just the id that is repeated, but the whole field is the same. To clean up the data set, repeated entries will be dropped.