# Permutation with constraints
The program permRand.py creates a set of N arrays containing M indices. Each index can have the value 0 or 1. An additional constraint is that each array should only share a maximum of *one* additional index with all other arrays. For example, a setup like M=10, k =3, N= 10 results in the following arrays:

```python
[[0 1 0 0 1 1 0 0 0 0]
 [1 0 0 0 0 0 1 0 1 0]
 [0 0 1 1 0 0 0 1 0 0]
 [0 0 0 0 0 1 0 1 0 1]
 [0 1 1 0 0 0 0 0 0 1]
 [0 0 0 1 0 0 0 0 1 1]
 [0 0 1 0 0 1 1 0 0 0]
 [1 1 0 0 0 0 0 1 0 0]
 [1 0 1 0 1 0 0 0 0 0]
 [0 0 0 1 1 0 1 0 0 0]]
```

 In addition, the -t switch controls a target speads, leading to more evenly distributed array.


