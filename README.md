# deepTimeSeriesPrediction for Industrial plants

Modern industrial plant is a complex of thousands of machineries. Understanding dynamic of the complex with physics laws and differential equations is almost impossible. For the purpose of understanding physical dynamics of industrial complex, instead of classical model based aprrocach, I have conducted data-driven modeling approach.

## Problem solving directions

### General work-flow

The plant has physical connections (e.g. in the format of pipelining). Therefore, we can decompose the large comeplex into small subset of machines. Hence, we firstly model the single or small set of machines with small model. After we will combine the small models for recognize dynamic of the complex.

### Class of problem

I interprete industrial machine modeling as a multiple time-series regression problem. Multiple time seireis regression is a class of regression where input and output are time-series; input and output could be multiple time-series. Imagine a machine in the factory.
An operator(or computer system) will give **control inputs** for the machine. As a result, the machine produce **reactive behaviors**.
Here, the control input may cause some effect on the reactive bahaviors over some time span. In other words, a time window of **input controls** will cause an effect to the **reative behaviors**

In functional format, the relationship among the inputs and behaviors will be represented as follows

time seires of reactive behaviors = f_time_series_model(time series of control inputs)


