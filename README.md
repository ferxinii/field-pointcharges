# Electric field of static point charges ⚡️
This repository contains a simple Python code to visualize the electric field produced by a set of static point charges.

## Running the code
Simply click on the plot where you want to place the point charge. A random charge of (reduced) magnitude 1 or -1 will be placed there, and the corresponding electric field visualized.

## Physics
I have used Coulomb's law and the principle of superposition to compute the field in every point of a 2D grid. Note that the units are reduced.
``` math
\vec{E^*}(\vec{r}) = \sum_{i=1}^N q^*_i \frac{\vec{r}-\vec{r_i}}{(\vec{r}-\vec{r_i})^3}  \quad \quad q^*_i = 4\pi\epsilon _0q_i
```


## Examples
<p align="center">
<img src="./images/summary.png" alt="Example 1" width="400" height="auto" />
<img src="./images/m_evolution.jpg" alt="Example 2" width="400" height="auto">
</p>
