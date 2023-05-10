# Python_Assignment
final assignment for imprs-python-2023

Option 2: Picture verification task

In a picture verification task, the participant is presented with a word for a given period of
time, then with a break, and subsequently with a picture that either matches or does not
match the presented word. Participants are asked to indicate whether or not this picture
matches the given cue word. Typically, participants will respond faster to matching trials than
to non-matching trials. We are going to build an experiment that can do this. You can use the
stimuli you created for session 2a (images); but if you did not manage to create the stimuli,
or do not like the result, all the stimuli are also in the repository of session 3.
We have a set of image stimuli. We will make a demo that presents matching cue-target
pairs and ask participants to respond. After making this experiment, you can add
mismatching target pairs, and think of a way to properly balance and randomise these.
(There is an example randomisation script in the GitHub repository.)

Key elements of the experiment:
- Read the csv with stimulus information
- Instruction screen (optional)
- Present a word
- Fixation cross-screen
- Present a visual stimulus
- Clock
- Keys to press
- Record the response & timing

If you feel like it, you can include auditory (spoken) stimuli as well, so you can try to see if
there is a difference in the reaction time effect between modalities.
Once you have completed the experiment, and have written the results to CSV files, you can
write a preprocessing and visualisation notebook. First, run a few “participants” (go through
the experiment yourself 2-3 times, or distract your office- or housemates with it!) Then, load
and merge the output files. Calculate some summary statistics, and verify that the results
look sensible. Then, use a plotting package of your choice to visualise results. Make (at
least) one diagnostic plot, with (relatively) raw data, as a check to see that the data actually
looks sensible, and (at least) one aggregate plot, aimed at effectively visualising the
outcome of the experiment with respect to its hypothesis. Finally, even though it may not
make much sense for the amount of data, try out some simple statistics

Research Question: Certain professions are associated with certain genders. For example, when asked to think of a doctor, people my often think first of a man rather than a woman. For a nurse, the opposite might be true. These kinds of biases can be studied through reaction time experiments. For example, a participant is shown the word "doctor" and then a picture, and they have to react as quickly as possible to indicate if the picture matches the word. If they have unconscious biases, their reaction time may be slower or faster depending on whether the picture meets their expectations. This experiment aims to explore the following research questions: 
1) Are biases apparent in L1?
2) Do biases exhibit in the same way in L2?

All participants are speakers of Dutch and English, their L1 will be one of these languages, and their proficiency level in the other will be a minimum of B1. There will be a practice round with animals. 
Steps:
1) Create a list of jobs that are gender neutral in Dutch