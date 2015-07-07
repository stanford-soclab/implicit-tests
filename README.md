## Overview

This is a collection of interactive reaction time based studies implemented in Javascript, geared towards studies deployed on Qualtrics. The majority were written for the Stanford Laboratory for Social Research, and are ports of the corresponding tests in Millisecond; exceptions are noted in the corresponding info.txt files. They are written with easy modification in mind (mostly). 

## Usage

Most of the tests consist of an .html source which can be pasted into the Qualtrics source, along with a python script to parse the output (for instructions, see the Usage console output). The more recent tests can all be modified as follows:

* To run on or off Qualtrics, set the in_qualtrics flag to true or false respectively;
* Timings etc can be modified by changing the respective variables;
* Prime and target words/images can be added into arrays of primes/targets.

#### For Qualtrics:

* change the in_qualtrics flag to true;
* create a question of format "text input";
* paste the .html source into the rich content editor -> source for that question.

Parsers are run on the .csv output that Qualtrics exports.

(The older tests will probably eventually be upgraded as they are reused...)

## Under the hood

Successive study participant responses are appended to an html element with ID equal to the ID of the corresponding Qualtrics question (Qualtrics tells you this...somewhere).

(more to come, maybe)

## Contact

[Stanford Lab for Social Research](http://lsr.stanford.edu)

Authors: 
Justine Zhang (github: tisjune)


