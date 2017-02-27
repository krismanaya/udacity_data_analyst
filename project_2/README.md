## Titanic Data Description

**VARIABLE DESCRIPTIONS:**
* survival        **Survival (0 = No; 1 = Yes)**
* pclass          **Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)**
* name            **Name**
* sex             **Sex**
* age             **Age**
* sibsp           **Number of Siblings/Spouses Aboard**
* parch           **Number of Parents/Children Aboard**
* ticket          **Ticket Number**
* fare            **Passenger Fare**
* cabin           **Cabin** 
* embarked        **Port of Embarkation**
                (C = Cherbourg; Q = Queenstown; S = Southampton)

**SPECIAL NOTES:**

* Pclass is a proxy for socio-economic status (SES)
   * 1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower

* Age is in Years; Fractional if Age less than One (1)
  * If the Age is Estimated, it is in the form xx.5

**With respect to the family relation variables (i.e. sibsp and parch)
some relations were ignored.  The following are the definitions used
for sibsp and parch.** 

1. *Sibling:  Brother, Sister, Stepbrother, or Stepsister of Passenger Aboard Titanic*. 

2. *Spouse:   Husband or Wife of Passenger Aboard Titanic (Mistresses and Fiances Ignored)*.

3. *Parent:   Mother or Father of Passenger Aboard Titanic*.

4. *Child:    Son, Daughter, Stepson, or Stepdaughter of Passenger Aboard Titanic*. 

Other family relatives excluded from this study include cousins,
nephews/nieces, aunts/uncles, and in-laws.  Some children travelled
only with a nanny, therefore parch=0 for them.  As well, some
travelled with very close friends or neighbors in a village, however,
the definitions do not support such relations.

**Titanic_src** 

This folder contains the report that is writen along with the source code obtained from the titanic.csv file. If you would like to view the report on the blog please click [here](http://krismanaya.github.io)

