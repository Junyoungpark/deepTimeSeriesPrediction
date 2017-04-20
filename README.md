# deepTimeSeriesPrediction for Industrial plants

Modern industrial plants are composed of a large of number of sub-components. Usually, it is almost impossible to model such complex systems using physics laws or mathematical equations. For the purpose of understanding physical dynamics of industrial plants, I employed data-driven modeling approach, in this case deep learning.

## Problem solving directions

### General work-flow: From complex to sub-components

The plant has physical connections (e.g. in the format of pipelining). Therefore, we can decompose the large complex into small sub-components. Hence, we firstly model the sub-components with small model. After, we will combine the small models for recognize dynamic of the complex.

### Class of problem

I interpret industrial machine modeling as a **multiple time-series regression** problem. Multiple time-series regression is a class of regression where input and output are time-series; input and output could be multiple time-series. Imagine a machine in the factory. An operator(or computer system) will give **control inputs** for the machine. As a result, the machine produce **reactive behaviors**. Here, the control input may cause some effect on the reactive behaviors over some time span. In other words, a time window of **input controls** will cause an effect to the **relative behaviors**

In a functional format, the relationship among the inputs and behaviors will be represented as follows.

  time seires of reactive behaviors = f_{time_series_model} (time series of control inputs, contextual inputs)
  
  where contextual inputs are observable but not controllable variables, which can possibly represent the environmental conditions.

### Multiple-time series modeling through deep learning

Various class of neural network are empirically shown nice performance for prediction task. However, the most plausible choice of network structure will be RNN family. In this research, time-series are modelled with recurrent neural network and stacked fully connected layers.

## Examples of Multiple-time series modeling

1. Displacement prediction under stochastically varying input controls in petroleum plant
[link to jupyter notebook](https://github.com/Junyoungpark/deepTimeSeriesPrediction/blob/master/displacement.ipynb)
2. Viscosity predcioton under stochastically varying input controls in chemical plnat
[link to jupyter notebook](https://github.com/Junyoungpark/deepTimeSeriesPrediction/blob/master/viscosity_prediction.ipynb)
