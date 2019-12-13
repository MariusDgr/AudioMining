# AudioMining

A data mining project whose aim is to decompose a musical composition on the individual instrument tracks.

## High level end product structure and usage

![App Usage Diagram](./documentation/diagrams/app_objective.png)

A sound file is fed into the application, which separates the initial song into the individual instruments that we wish to extract as speciefied in the settings of the application.

### Prerequisites

Modules and auxiliary software that needs to be installed:

```
- ffmpeg: mp3 to wav conversion
```

## Tasks and deadlines
---
![Gantt Diagram](./documentation/diagrams/gantt_roadmap.png)

## Project developement workflow
---
A high level structure of the project modules comprising the prosect can be seen in the following diagram:

![Workflow](./documentation/diagrams/project_workflow.png)



The steps needed to complete the task will be described in a logical order:

<!--
    start project steps body
-->

### Mixed samples (Training dataset)
---
Mixed sound samples are needed as an input for the training of the model used in the app. 

#### Mixed samples generation strategies

1. Original sample and zero mean white noise
    - signal to noise ratio variable

2. Two original samples ovelapped (different instrument)
    - mixing matrix for amplitudes
    - sample offset

3. Concatenate original samples to produce longer tracks

4. Three different instruments overlapped

5. More different instruments overlapped

6. More original samples ovelapped (same instrument)


### Algorithm approaches
---
#### State of the art: PCA, ICA

#### PCA

#### ICA

#### Neural Network

NN architecture is composed by:
    - autoencoder

<!--
    end project steps body
-->

## Authors

* **Marius Dragomir** - [MariusDgm](https://github.com/MariusDgr)


## License

This project is licensed under the Apache license - see the [LICENSE](LICENSE) file for details

## Acknowledgments

Main dataset from: https://www.philharmonia.co.uk/explore/sound_samples

other datasets:
https://github.com/ejhumphrey/minst-dataset
https://sampleswap.org/


