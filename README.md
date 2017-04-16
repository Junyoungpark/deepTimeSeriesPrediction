# deepTimeSeriesPrediction for Industrial plants

Modern industrial plant is a complex of thousands of machineries. Understanding dynamic of the complex with physics laws and differential equations is almost impossible. For the purpose of understanding physical dynamics of industrial complex, instead of classical model based aprrocach, I have conducted data-driven modeling approach.

## Problem solving directions

### General work-flow

The plant has physical connections (e.g. in the format of pipelining). Therefore, we can decompose the large comeplex into small subset of machines. Hence, we firstly model the single or small set of machines with small model. After we will combine the small models for recognize dynamic of the complex.

### Class of problem

I interprete industrial machine modeling as a multiple time-series regression problem.


