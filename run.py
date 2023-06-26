from code.algorithms.baseline import Baseline_search
from code.algorithms.Hillclimber import Hillclimber
from code.algorithms.SimulatedAnnealing import SimulatedAnnealing
from code.algorithms.Hillclimber_prime import Hillclimber_prime
from code.algorithms.SimulatedAnnealing_prime import SimulatedAnnealing_prime
from code.algorithms.import_data import stations
from code.algorithms.opdrachtsolver import visualize

iteration_count = 1000
route_duration = 180
route_count = 20

## For further variation: 
    ## In code/algorithms/import_data.py, set data to data/StationsHolland.csv and data/ConnectiesHolland.csv 
    ## or data/StationsNationaal.csv and data/ConnectiesNationaal.csv

## Now simulate!
## Comments are prefixed by double-hashtags '##' and code-lines are prefixed by single-hashtags '#'
## Delete or add a hashtag '#' in front of the below code-lines in order to run or disable them!


######## EXERCISE 1 SOLVER ########

## Visualize lijnvoering found as a solution to opdracht 1. Enforce route_duration = 120 and route_count = 7.
#visualize(iteration_count, 180, 20)



######## BASELINE SEARCH ########

## Construct a map of the stations with their interconnections, and enforces a route on the map:
#Baseline_search(stations).visualise(route_duration, route_count)

## Construct a density plot of K-scores found after running Baseline-search:
#Baseline_search(stations).density_plot(iteration_count, route_duration, route_count)



######## HILLCLIMBER SEARCH ########

## Visualise the Hillclimber-algorithm by plotting both the K-score for the Hillclimber and each K-score upon searching for the optimal K-score.
#Hillclimber(stations).plot(iteration_count, route_duration, route_count)

## Calculate and plots the lijnvoering found upon applying Hillclimber optimization with a chosen amount of iterations. 
## Text output can be found in code/results/output_hillclimber.csv.
#Hillclimber(stations).optimal_lijnvoering_finder(iteration_count, route_duration, route_count)



######## SIMULATED ANNEALING ########

## Perform experiment for simulated annealing: choose Linear Temperature-function, vary alpha over 0, 0.1, 0.2, 0.3, ..., 1.
#SimulatedAnnealing(stations, route_duration, route_count).plot_linear(iteration_count, route_duration, route_count)

## Perform experiment for simulated annealing: choose Exponential Temperature-function, vary alpha over 0, 0.1, 0.2, 0.3, ..., 1.
#SimulatedAnnealing(stations, route_duration, route_count).plot_expo(iteration_count, route_duration, route_count)

## Give an impression of the inner-workings of Simulated Annealing whilst maximizing K.
#SimulatedAnnealing(stations, route_duration, route_count).search_vs_score(iteration_count, route_duration, route_count)

## Conduct an experiment under: vary the Temperature function over Linear and Exponential, vary alpha over 0, 0.1, 0.2, 0.3, ..., 1.
## function chooses the lijnvoering with highest K under variable alpha and temperature function, andchosen amount of iterations.
## Text output can be found in code/results/output_annealing.csv.
#SimulatedAnnealing(stations, route_duration, route_count).Optimal_lijnvoering_finder(iteration_count, route_duration, route_count)



################################################ PRIME ALGORITHMS ################################################
## These algorithms are extremely improved versions of the above algorithms, though the degree of improvement does indicate a buggy implementation



######## HILLCLIMBER SEARCH PRIME ########

## Visualise the Hillclimber-algorithm by plotting both the K-score for the Hillclimber and each K-score upon searching for the optimal K-score.
#Hillclimber_prime(stations).plot(iteration_count, route_duration, route_count)

## Calculate, output and plots the lijnvoering found upon applying Hillclimber optimization with a chosen amount of iterations.
## Text output can be found in code/results/out_hillclimber_prime.csv.
#Hillclimber_prime(stations).optimal_lijnvoering_finder(iteration_count, route_duration, route_count)



######## SIMULATED ANNEALING PRIME ########

## Perform experiment for simulated annealing: choose Linear Temperature-function, vary alpha over 0, 0.1, 0.2, 0.3, ..., 1.
#SimulatedAnnealing_prime(stations, route_duration, route_count).plot_linear(iteration_count, route_duration, route_count)

## Perform experiment for simulated annealing: choose Exponential Temperature-function, vary alpha over 0, 0.1, 0.2, 0.3, ..., 1.
#SimulatedAnnealing_prime(stations, route_duration, route_count).plot_expo(iteration_count, route_duration, route_count)

## Give an impression of the inner-workings of Simulated Annealing whilst maximizing K.
#SimulatedAnnealing_prime(stations, route_duration, route_count).search_vs_score(iteration_count, route_duration, route_count)

## Conduct an experiment under: vary the Temperature function over Linear and Exponential, vary alpha over 0, 0.1, 0.2, 0.3, ..., 1.
## function chooses the lijnvoering with highest K under variable alpha and temperature function, andchosen amount of iterations.
## Text output can be found in code/results/output_annealing_prime.csv.
#SimulatedAnnealing_prime(stations, route_duration, route_count).Optimal_lijnvoering_finder(iteration_count, route_duration, route_count)