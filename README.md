# Blackjack-ML

Developer: Scott Nguyen

The scope of this project is to create a playable blackjack game as well as apply machine learning to the model in order to determine if "basic strategy" is the best strategy for players in the long-term. The project utilizes a Model-View-Controller design pattern and take an object-oriented approach. 

# Project Roadmap

## Step 1 - `Model` <- `Here`
The model represents the Blackjack game itself. It will be responsible for implementing the rules of the game as well as making the appropriate updates based on player and dealer actions. The model will never call any of its own methods, rather, these will be handled by the controller.

## Step 2 - `Controller` 
The controller delegates the appropriate calls to both the model and the view whenever an action is made in the view. This delegation process uses an enumeration of valid actions to perform the action. 

## Step 3 - `View`
The view displays the current state of the blackjack game as well as provides a user interface that allows for button events, key events, etc. 

## Step 4 - `Generate Training and Test Data`
Utilizing the model, we can simulate millions of blackjack hands and record the actions and subsequent results. The data generated here will be stored in a mySQL or equivalent server in order to be easily parsed and accessed. 

## Step 5 - `Machine-Learning`
Leveraging API's such as Scikit-Learn, we can apply machine learning algorithms on our training and test data in order to hopefully derive meaningful conclusions. At the moment, Decision Trees and Neural Networks seem like prudent algorithms to utilize. 

## Step 6 - `Statistical Analysis`
Once we generate conclusions and data from our machine learning models, we will perform a statistical analysis on our data in order to determine if all of our work was worth it! 
