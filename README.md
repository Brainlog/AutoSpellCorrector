# AutoCorrector
It is an Ai agent that uses local search variations for correctly finding a better version of given sentence that makes more sense with given context. We have made changes to only to the file solvers.py where we implmented Local Search, Beam Search. Rest interface is provided by the course coordinator.

# Run
```
conda activate aia1
python run.py -src data/input.txt -tar data/pred.txt -tm 2
```


