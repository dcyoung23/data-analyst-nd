## Summary

Daily Fantasy Sports (DFS) basketball contests entail selecting a lineup of players within position and salary cap limits.  Points are based on the players game performance for specific statistical categories.  Value in a players performance is measured by the difference in actual points scored and their salary based expectation.  The optimal lineup for each day is a linear optimization problem to iterate through every possible lineup combination to find the highest points total within the salary cap.  Selecting a DFS tournament lineup isn't just about identifying players that will score a higher number of points.  It is essential to identify projected performance value and the mix of players that maximizes points scored as a whole.

Would you be happy with a 29.2 point performance from Anthony Davis when he cost $11,200?  Is it best to build a lineup that consists of 2-3 stars and the rest scrubs or a mix of different types of players?  This visualization explores [FanDuel](https://www.fanduel.com) data scraped from the [web](http://rotoguru1.com/cgi-bin/hyday.pl?game=fd) over the first half of the 2015/16 NBA season to answer these types of questions.

As shown in the Required Points Level by Salary chart a player with a salary of $11,200 you really want points scored at or above 48.  You are paying up for a huge star but stars have higher point expectations.  On opening night of the NBA season Anthony Davis had a bad game for him and only scored 29.2 points.  As shown in the Player Performance Value Plot his circle is at the bottom near the x axis.  On the contrary Stephen Curry with a salary of $800 less was on fire and scored 59.7 points and was in the optimal lineup.  This is a perfect example of performance value.

There are many articles published in the industry such as this [one](http://www.dailyfantasydork.com/2015/12/02/nba-dfs-the-intelligent-guide-to-growth-2/) that talk about a strategy of building a lineup around stars and scrubs.  However, historical data for the current season shows that on average this is just not the case.  You would be better offer sticking with a more balanced lineup and make adjustments in either direction when there are players that have higher projected value.

## Design

The initial design concept centered around the relationship between points scored, player performance and salary.  Based on these 3 variables a bubble chart was the most appropriate chart to visualize this relationship.  There is a strong linear relationship between the 3 variables so the radius of the circles and orange color encoding of the players in the optimal lineup was important.  In the first version, I only included a bubble chart and a legend for optimal lineup players.

After receiving feedback I made multiple changes prior to the first project submission.  I changed the color of the players not in the optimal lineup to a more monotone grey which stands out more against the orange optimal lineup players.  I changed the location of the axis labels and added a legend for circle size.  I also added an optimal players table and bar chart showing total points scored based on 3 salary based player type categories (star, mid-level and scrub).  The purpose of the bar chart is to provide a more effective visualization of the total points distribution for each player type.

After the first project review I went back to the drawing board and made additional changes to explain the key findings from the data exploration steps.  A Key Points bullet list was added so the visualization can stand on its own with some textual details.  A bar chart was also added to visualize the number of points you should expect from a player based on their salary in order to cash in a tournament.  The optimal lineup is the holy grail where big money can be won but you can still make money in a tournament with lower scores.  A reasonable estimate of the cash line is 80% of the optimal lineup for the day.  An area chart was also added to show the historical salary cap distribution based on the 3 player types.  There are peaks and valleys each day so the data was binned by week.  Additional minor changes were made to the circle radius, the optimal lineup legend circles were changed to rectangles and the transition on load was removed.  The user can select a date to explore the data further and does not have to sit through all 106 days.

## Feedback

Below is a summary of the feedback I received.

*Udacity project reviewer*

**The review was quite detailed so I will focus on the key issues.  The first project submission did not meet expectations based on two main points: 1) it did not stand on its own with limited context outside of this README.md and 2) it was not effective at explaining the 2 key questions posed in the Summary section.**

The Summary and Design sections were updated to address all revisions made to the visualization based on the feedback received in the project review.  The changes between the second and third versions were pretty significant.

*Udacity forum mentor Uira Caiado de Castro*

**I suggest you add more explanation about the data encoded in of your chart. Perhaps you could even rename the axes to clarify what you are plotting.**

Originally I had the axis labels anchored to the end and on the inside.  I also had pretty short descriptions (Points and Value).  I moved the labels to the middle and outside.  I made the text slightly more descriptive (Points Scored and Performance Value) and added details to the Summary section to describe what these fields represent.  In the first version I did have a written section in the actual index.html file but I moved all summary text for the visualization to the README.md file.  In the third version a key points bullet list was added within the actual visualization.

**I can see a kind of "barrier" in the data, where there are many data point in a linear relationship. Would you know why?  Would be nice if you include some notes about the relationships that you want the users to understand in your dataset.**

The more points a player scores the higher their performance value.  The data points shift to the right as the players salary increases and downward if they don't achieve expectations.  One consideration is there is a higher number of lower salary players (scrubs) and many score similar points each day.  It is essential to identify scrubs that project to score higher than their salary implies and the rest of them are essentially out of consideration on a daily basis.  The circle radius was adjusted in the third version which helped address some of the overplotting.  The bubble chart is also no longer the focus of the visualization and redirected as more of an exploratory tool to dive into the daily results.

*Current employee Sam Ha from LinkedIn share*

**What is the size of the data point indicating?**

The first version the radius was set based on the salary.  The higher the salary the larger the circle but I did not include a legend.  Instead of just adding a legend for salary I grouped players into 3 salary based categories: 

1. Star: Salary $9000+ 
2. Mid-Level: Salary $6000+ 
3. Scrub: Salary $3500+ 

This ultimately was what I was trying to communicate and this gets more clarity in the circle size as well.  In the third version the radius size was adjusted to be consistent with the salary scale.

**Can I use this to get future value picks?**

I spent a good amount of time creating the tidy dataset for the visualization.  It was worth the time as I really wanted to have some fun with this project.  The data could be used to create a predictive model but ultimately the intent here is an explanatory data visualization on some basic strategies to create tournament lineups.  Ultimately, accurate point projections and daily research to identify value plays are critical for success.

*Friend and former employee Justin Garza*

**The date interaction is a little difficult to use and not immediately obvious that you can use it to select a different date.  Maybe you could add a date slider instead?**

This was great catch because initially it was pretty difficult to pick a date.  However, I really liked the uniqueness of the date interaction so I strived to improve it instead of putting in a generic date slider.  I changed it so you have to click on the date to stop the transition.  You could easily mouseover the date and it would stop the transition even though that was not your intent.  
I changed the cursor to a hand when you mouseover to visually show that you can click on the date.  Another issue was when you mouseover the date and then mouseout the selection would change due to the natural movement of the cursor.  I changed it so when you are scrolling to change dates you can click again to disable the mouseover event.  Finally, I changed the color when the label is active to green.  I added a transition to the text label underneath the x axis that explains that you can interact with the date transition.  The color changes from grey to the same active green color then back to grey.  This draws the attention of the user about the interactive nature of the date label.  As described above the initial transition was removed but the date interaction can still be used as desired.

## Resources
1. [Interactive Data Visualization for the Web - Scott Murray](http://alignedleft.com/)

2. [Performance Value statistic is based on Fantasy Labs Plus/Minus calculation](http://www.fantasylabs.com/) 

3. [Mike Bostocks: The Wealth & Health of Nations for date interaction idea](https://bost.ocks.org/mike/nations/) 

4. [Bubble Chart (Tooltip)](http://bl.ocks.org/mmattozzi/7018021) 

5. [D3 HTML Table](http://jasonheppler.org/2013/08/06/getting-started-with-d3/) 

6. [D3 Update HTML Table](http://stackoverflow.com/questions/32871044/how-to-update-d3-table) 

7. [D3 Group Data](http://learnjsdata.com/group_data.html) 

8. [D3 Dashboard Example](http://bl.ocks.org/diethardsteiner/3287802) 

11. [D3 Margin Convention](http://bl.ocks.org/mbostock/3019563) 

12. [HTML Reference](http://www.w3schools.com/tags/) 

13. [CSS Reference](http://www.w3schools.com/css/) 

14. [Dimple JS](https://github.com/PMSI-AlignAlytics/dimple)

15. [Dimple JS Area Chart](http://dimplejs.org/examples_viewer.html?id=areas_horizontal_stacked)

