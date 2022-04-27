# cmpsci-4200-project1-part-1
dataframe used: https://www.kaggle.com/datasets/samuelcortinhas/credit-card-classification-clean-data

This dataset is a cleaned up version or an existing dataset on kaggle. And the idea of the dataset is to try and use it for credit approval by looking at various aspects of a person, such as whether or not they are married, their housing situation, and even if they have a phone or not.

When looking at this dataset for potential relationships, a few seemed reasonable. The first being male vs female incomes and their risks, which showed men made more then women and were also more likly to be higher risk then women. The second was in family status vs income, which showed that surprisingly, those not in a relationship or marriage were on average making more than those who were married, and those who were widows were making far less. When including whether or not they were risky, widows turned out to be on average far less risky then their counterparts, followed by those where were in a marriage, then by people in marriages, then single people.  Next education vs income was looked at, which showed a clear average trend of the higher education you had, the more money you made, and when looking at risk,  academics on average were of far higher risk than their counterparts. The last trend i tried to look at was if there was any connection to account length and income of an individual. When directly graphing them, no. When i tried tying it to target, i saw that the average income most times for risky people was far higher or lower on average than their nonrisky counterparts.None of these alone would allow us to accurately predict if someone was high risk or not. With this in mind, the plan for this dataset is to see that if we can look at a combination of these trends combined and some of the others looked at to see if we can predict if someone is risky or not.

# graphes

#education vs income with a seperation of risky or not
![](/educationvs%20incomehuetarget.PNG)

#family status vs income with a seperation of risky or not
![](/familystatues%20vsincome%20and%20risk.PNG)

#family statues vs risk
![](/efamilystatuesvsriskornot.PNG)

#income vs account length seperated by risk or not
![](/incomevaccountlenhuetarget.PNG)

#male vs female in income and seperated by risk or not
![](/malevfemale%20incomeandriskvnot.PNG)

#owning propery vs risk
![](/owning%20propertyvsnot%20for%20beinghigh%20risk.PNG)
