# Learning to Label and Segment Human Demonstrations

A project for weakly supervised segmentation of sensor data from human demonstrations. A Hidden Markov Model (HMM) with a particle filter is used to model the system and determine the action being performed by the human at each point in time.

<br />
<p align="center">
  <img src="https://github.com/egalbally/HumanDataLabellingAndSegmentation/blob/master/readme_imgs/method.png" width="550"/>
</p>
<br />

As shown above, our algorithm takes as inputs: (a) sensor data recorded during a human demonstration of a complete task, and (b) a set of "primitive" actions that can be combined to perform the complete task. Given **_a single manually labelled demonstration_** of the task, the algorithm is able to automatically label and segment other demonstrations and output the primitive sequence that was executed by the human. Below is an example of what the **data and results** look like for two tasks: putting a cap on a bottle and screwing a threaded pipe. **Note** that the algorithm generalizes to different objects. As long as the task involves the same set of primitive actions, we are able to label and segment the sensor data.

<br />
<p align="center">
  <img src="https://github.com/egalbally/HumanDataLabellingAndSegmentation/blob/master/readme_imgs/sampleResults.png" width="750"/>
</p>
<br />

## Data: 
  - Human demonstrations of complete manipulation tasks
  - Manipulated object pose and contact forces and moments (recorded using optitrack and a 6DOF optoforce sensor)
  - Objects: small, medium, large bottle, lightbulb, pipe

<br />
<p align="center">
  <img src="https://github.com/egalbally/HumanDataLabellingAndSegmentation/blob/master/readme_imgs/data.PNG" width="750"/>
</p>
<br />

## Analysis: 

**_Note_** - this code requires Python 3

   - Directories: 
      - /figures
      - /figures2label
      - /references
      - /results
      - /transitions
      - /past_results
   - Key files
      - gmm.py and gmm_objects.py
         - used to identify and segment human demonstration data into primitives
         - gmm_objects simplifies the use on data from different objects
         - method: Hidden Markov Model with particle filter
         - uses: read_data.py and plot_data.py
         - requires: having created 3 directories called: transitions, results, figures, references.
      - initialProcessing_rawdata.py 
         - script for use right after collecting sensor measurements
         - uses: read_data.py and plot_data.py
         - see file for how to use and functions
      - finalProcessing_results.py
         -  plots segmented data both manual and automatic by using functions in plot_data 
         -  computes success rate as the similarity between demonstrated and labelled primitive sequences
      - read_data.py - reads in raw sensor data and processes it (change of frame, offsets, quaternions...)
      - plot_data.py (pending refactoring)
          - plot_file() - plots the segmented sensor data with labels
          - getlabels()
          - compute_success_rate() - really it's computing accuracy as defined in the paper
          - write_Pr_file()
      - testmultiple.sh - bash script to run gmm.py on many runs at once
   - Ploting 
        - plotconfusion.py - plots a confusion matrix to visualize labelling errors
        - plotbar.py - plots a bar diagram that respresents the same concept as the confusion matrix
        - plotbox.py - makes a box plot with the mean and standard deviation of all runs
        - plotTmatrixdata.py - 3x1 plot containing data about Tmatrix updates
   - Old or test files
       - analyse.py
       - classifier.py
       - jupyter notebooks - used for plot debugging
       - test.py - uses classifier.py 
    
## Training: 
  - network.py 
  - Learns a transition model for the task based on the data labelled by the gmm
