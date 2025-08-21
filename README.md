# lichess-dataset
Lichess Dataset Observation

## Current Goals:
1. Import Database from the csv file to postgresql
2. Correlate Relative Ratings of white and black players to winrate
3. Correlate resignation rate affected by player rating and opponents
4. Train a classifier which predicts player win rate based on other inputs
5. Visualisation of data

## Observations of Dataset:
When importing the csv file into postgre, created_at and last_move_at are in the form of x.xxxxxE+12. This is a timestamp, so I tried to store it as bigint, but ended up having to import it as text.

The field 'moves' is a very long string of chess moves like 'A5 E3 D2' and so on. Originally attempted to store it as Varchar, but upon further research its better to use text for a datatype unless you need to verify length of string.

Tried to use the field 'id' as primary key, but found duplicate entries. Upon checking the fields such as white id, black id, , it is not just the id that is repeated, but the whole field is the same. To clean up the data set, repeated entries will be dropped.

## Thought Process of goals
### Goal 2
#### Thought Process
To calculate the correlation of relative ratings to winrate, we can take the difference between white and black player ranks. Additionally, we can also factor in the average rating between white and black player in one game to see the player skill level in a game, as I feel like that would make a difference. Players with less skill rating might produce less consistent results as it is more likely their plays are less consistent.

Using sql queries for min and max entries, we can see that the ratings are about 750-2750. A rank category split of 200 seems good. We will split the tiers into different dataframes and generate correlation from that.

Another thing to be aware of is not all games end with someone winning, it might be a draw. We can check whether black or white is favoured to win and then return 1 if they actually do, or -1 if they don't. We can equate draws to 0.

Since we end up with 8 data points, we can use a linear line of best fit.
#### Reflection
Instead of the -1,1 system that I implemented, we could instead assign white wins to 1 and black wins to -1. We can then take that value and divide it by the rank difference, then round up to 1. This would be easier to implement. Draws would be counted as 0.

We could also take draws as a loss for whoever was favoured, if we wanted to be harsher. This is because we're checking if having a higher rank means a win, which a draw is not.

### Goal 3
#### Thought Process
Again, we take the difference of ranks, but this time, we compare it to resignation rate. This time, I won't split the rank difference into tiers, as I want to analyse the mindset of a player who has to face a larger rank than them. I will take the difference in rank, and then see whether the weaker individual resigned or not. We can take a percentage of resigns/games made.

I can also now implement the system described in Goal 2 reflections for easier sorting of wins.
#### Reflection
It may have been a good idea to take into account how fast the player resigned. This would show the difference in someone resigning just because they've already lost the game, compared to someone who forfeits because they feel like they'll lose. A way to implement this would be to take the start and end timestamps. Alternatively, we can check the length of the string field for moves. We would have to decide how many moves/how much time is(are) considered relevant to our data, especially because some chess games end in 4 moves, or very fast.
