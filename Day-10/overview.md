<div class="markdown-converter__text--rendered"><h3>Overview</h3>
    <p>The data has been split into two groups:</p>
    <ul>
    <li>training set (train.csv)</li>
    <li>test set (test.csv)</li>
    </ul>
    <p><b> The training set </b>should be used to build your machine learning models. For the training set, we provide the outcome (also known as the “ground truth”) for each passenger. Your model will be based on “features” like passengers’ gender and class. You can also use <a rel="nofollow noreferrer" href="https://triangleinequality.wordpress.com/2013/09/08/basic-feature-engineering-with-the-titanic-data/"> feature engineering </a>to create new features.</p>
    <p><b>The test set </b>should be used to see how well your model performs on unseen data. For the test set, we do not provide the ground truth for each passenger. It is your job to predict these outcomes. For each passenger in the test set, use the model you trained to predict whether or not they survived the sinking of the Titanic.</p>
    <p>We also include <b>gender_submission.csv</b>, a set of predictions that assume all and only female passengers survive, as an example of what a submission file should look like.</p>
    <h3>Data Dictionary</h3>
    <table>
    <tbody>
    <tr><th><b>Variable</b></th><th><b>Definition</b></th><th><b>Key</b></th></tr>
    <tr>
    <td>survival</td>
    <td>Survival</td>
    <td>0 = No, 1 = Yes</td>
    </tr>
    <tr>
    <td>pclass</td>
    <td>Ticket class</td>
    <td>1 = 1st, 2 = 2nd, 3 = 3rd</td>
    </tr>
    <tr>
    <td>sex</td>
    <td>Sex</td>
    <td></td>
    </tr>
    <tr>
    <td>Age</td>
    <td>Age in years</td>
    <td></td>
    </tr>
    <tr>
    <td>sibsp</td>
    <td># of siblings / spouses aboard the Titanic</td>
    <td></td>
    </tr>
    <tr>
    <td>parch</td>
    <td># of parents / children aboard the Titanic</td>
    <td></td>
    </tr>
    <tr>
    <td>ticket</td>
    <td>Ticket number</td>
    <td></td>
    </tr>
    <tr>
    <td>fare</td>
    <td>Passenger fare</td>
    <td></td>
    </tr>
    <tr>
    <td>cabin</td>
    <td>Cabin number</td>
    <td></td>
    </tr>
    <tr>
    <td>embarked</td>
    <td>Port of Embarkation</td>
    <td>C = Cherbourg, Q = Queenstown, S = Southampton</td>
    </tr>
    </tbody>
    </table>
    <h3>Variable Notes</h3>
    <p><b>pclass</b>: A proxy for socio-economic status (SES)<br> 1st = Upper<br> 2nd = Middle<br> 3rd = Lower<br><br> <b>age</b>: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5<br><br> <b>sibsp</b>: The dataset defines family relations in this way...<br> Sibling = brother, sister, stepbrother, stepsister<br> Spouse = husband, wife (mistresses and fiancés were ignored)<br><br> <b>parch</b>: The dataset defines family relations in this way...<br> Parent = mother, father<br> Child = daughter, son, stepdaughter, stepson<br> Some children travelled only with a nanny, therefore parch=0 for them.</p></div>