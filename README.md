# Election_analysis
Overview: We were asked to provide a written analysis of the election audit for the election commission. We have already gathered information on candidate votes (percentages and winning). The election commission is asking for new results for the voter turnout for each county, percentage of  votes from each county out of the total count and county with the highest turnout. The request also include that we have a clearly written outline overview of the analysis methodologies. 

## Requirements and Details of the Analysis
1. For this challenge, we are to use for loops and conditional statements with membership and logical operators to find the requested results. Then, print the results tot he command line and save them to a text file. 

2. We were to initialize a county list and dictionaries that will hold county names, the key and votes cast for each county as the value.

![image](https://user-images.githubusercontent.com/98235755/159043385-a0ab9634-36b1-46a7-9d14-847e89746c6d.png)


3. Write a for loop script that gets the county name from each row and decision statement with a logical operator to check if the county name acquires is in the county list. If not, it should be added to the county list. Start tracking the vounty votes, initializing it to zero. 

![image](https://user-images.githubusercontent.com/98235755/159043485-bf279b23-2b6a-47a8-af10-c17ddeba9693.png)


4. Write a script that calculates the county's votes as a percentage of the total votes

![image](https://user-images.githubusercontent.com/98235755/159043549-4d66bb48-8d73-4052-b344-b67f955cc290.png)


5. Write a script that print the current county, its percentage of the total votes, and its total votes to the command line. Determine the winning county. Write a script to print and save results in a text file.

![image](https://user-images.githubusercontent.com/98235755/159043592-b9129a3b-d834-445a-bd9d-3ceff0fcf407.png)


## Results of the Analysis
### Election-Audit Results
1. There were 369,711 total votes cast in this congressional election
2. The breakdown of the county and candidate votes are shown below.  

![image](https://user-images.githubusercontent.com/98235755/159043845-03a99d73-276a-4ff3-ad90-49be6ac78675.png)

3. The county that had the largest turnout was Denver and the candidate that earned the most vote was Diana DeGette with 73.8%, 272,892 votes.

### Election-Audit Summary

Overall, this analysis and how the codes have been written has proven to be accurate. Given that, this same analysis/code set could be used (with some modifications) in an expanded analysis to include other states like for national(presidential) vote audits. We could modify so that we would have a breakdown of the total votes per state and the largest state that casted the vote. 

In including other states, we would need to initialize a state list and dictionaries that will hold state names, the key and votes cast for each states as the value; write some for loop scripts that gets the state name from each row and decision statement with a logical operator to check if the state name acquired is in the state list. If not, it should be added to th state list, etc. Basically the same steps we did when we analyzes the county level. 

For the purposes of illustration of code moidifcation sample, I did add some MD data to the dataset to show the results.

Below is a sample of the code modifications and how the result would be printed into the terminal:

<img width="549" alt="Screen Shot 2022-03-18 at 2 21 22 PM" src="https://user-images.githubusercontent.com/98235755/159061152-8521bc42-8f03-46b3-be0c-dff345f184fb.png">

<img width="358" alt="Screen Shot 2022-03-18 at 2 23 12 PM" src="https://user-images.githubusercontent.com/98235755/159061402-905c4107-4a6c-4937-b1c0-a517747dab58.png">
