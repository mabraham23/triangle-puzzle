# Triangle Solver for CS4300

Contains Solution for Local Search ( Simulated Aneealing ) and Classic Search ( Depth First Search ) in their corresponding folders

In order to run all puzzles on **Local Search** issue the following bash command:

    for p in puzzles/*; do
        ./local-search/simulated-annealing.py $p
    done
    
In order to run all puzzles on **Classic Search** issue the following bash command:

      for p in puzzles/*; do
        ./classic-search/depth-first.py $p
      done
    
    
The output for a single test will look like this:

    aab
    aCc
    cBc
    Cbd
    eeA
    ECE
    ebb
    BDc
    CCC
    
Where each line will contain the piece, with sides ordered from left to right that should fit into each slot starting from the top of the triangle board to the bottom.

