#!/usr/bin/python3
import os
import sys
<<<<<<< HEAD:examples/ES-Hyper-NEAT_xor.py
import time
import random as rnd
import subprocess as comm
import cv2
import numpy as np
import pickle as pickle
=======
import commands as comm
>>>>>>> origin/master:examples/TESTESHyperNEAT_xor.py
import MultiNEAT as NEAT
import multiprocessing as mpc
import numpy as np
import cv2
import Utilities

params = NEAT.Parameters()
params.PopulationSize = 100
params.DynamicCompatibility = True
params.CompatTreshold = 1.0
params.YoungAgeTreshold = 15
params.SpeciesMaxStagnation = 30
params.OldAgeTreshold = 35
params.MinSpecies = 1
params.MaxSpecies = 15
params.RouletteWheelSelection = False
params.OverallMutationRate = 0.
params.MutateAddLinkProb = 0.03
params.MutateAddNeuronProb = 0.01
params.MutateWeightsProb = 0.90
params.MaxWeight = 5.0
params.WeightMutationMaxPower = 0.8
params.WeightReplacementMaxPower = 1.0
params.MutateNeuronActivationTypeProb = 0.03
params.CrossoverRate = 0.5
params.MutateWeightsSevereProb = 0.01

# Probabilities for a particular activation function appearance
params.ActivationFunction_SignedSigmoid_Prob = 0.25
params.ActivationFunction_UnsignedSigmoid_Prob = 0.0
params.ActivationFunction_Tanh_Prob = 0.0
params.ActivationFunction_TanhCubic_Prob = 0.0
params.ActivationFunction_SignedStep_Prob = 0.0
params.ActivationFunction_UnsignedStep_Prob = 0.0
params.ActivationFunction_SignedGauss_Prob = 0.25
params.ActivationFunction_UnsignedGauss_Prob = 0.0
params.ActivationFunction_Abs_Prob = 0.0
params.ActivationFunction_SignedSine_Prob = 0.25
params.ActivationFunction_UnsignedSine_Prob = 0.0
params.ActivationFunction_Linear_Prob = 0.25


params.DivisionThreshold = 0.5
params.VarianceThreshold = 0.03
params.BandThreshold = 0.3
params.InitialDepth = 3
params.MaxDepth = 4
params.IterationLevel = 1
params.Leo = True
params.GeometrySeed = True
params.LeoSeed = True
params.LeoThreshold = 0.3
params.CPPN_Bias = -3.0
params.Qtree_X = 0.0
params.Qtree_Y = 0.0
params.Width = 1.
params.Height = 1.
params.Elitism = 0.1

rng = NEAT.RNG()
rng.TimeSeed()

substrate = NEAT.Substrate([(-1., -1., 0.0), (1., -1., 0.0), (0., -1., 0.0)],
                           [],
                           [(0., 1., 0.0)])

substrate.m_allow_input_hidden_links = False
substrate.m_allow_input_output_links = False
substrate.m_allow_hidden_hidden_links = False
substrate.m_allow_hidden_output_links = False
substrate.m_allow_output_hidden_links = False
substrate.m_allow_output_output_links = False
substrate.m_allow_looped_hidden_links = False
substrate.m_allow_looped_output_links = False

# let's set the activation functions
substrate.m_hidden_nodes_activation = NEAT.ActivationFunction.SIGNED_SIGMOID
substrate.m_output_nodes_activation = NEAT.ActivationFunction.UNSIGNED_SIGMOID

# when to output a link and max weight
substrate.m_link_threshold = 0.2
substrate.m_max_weight_and_bias = 8.0

def evaluate_xor(genome):

    net = NEAT.NeuralNetwork()

    try:

        genome.Build_ES_Phenotype(net, substrate, params)
        error = 0
        depth = 3
        correct = 0.0

        net.Flush()

        net.Input([1,0,1])
        [net.Activate() for _ in range(depth)]
        o = net.Output()
        error += abs(o[0] - 1)
        if o[0] > 0.75:
            correct +=1.

        net.Flush()
        net.Input([0,1,1])
        [net.Activate() for _ in range(depth)]
        o = net.Output()
        error += abs(o[0] - 1)
        if o[0] > 0.75:
            correct +=1.

        net.Flush()
        net.Input([1,1,1])
        [net.Activate() for _ in range(depth)]
        o = net.Output()
        error += abs(o[0] - 0)
        if o[0] < 0.25:
            correct +=1.

        net.Flush()
        net.Input([0,0,1])
        [net.Activate() for _ in range(depth)]
        o = net.Output()
        error += abs(o[0] - 0)
        if o[0] < 0.25:
            correct +=1.

        return [(4 - error)**2, correct/4., net.GetTotalConnectionLength()]

    except Exception as ex:
<<<<<<< HEAD:examples/ES-Hyper-NEAT_xor.py

        print('Exception:', ex)

        return 1.0
=======
        return [1.0, 0.0, 0.0]
>>>>>>> origin/master:examples/TESTESHyperNEAT_xor.py



def getbest(run, filename):
    g = NEAT.Genome(0, 7, 1, True, NEAT.ActivationFunction.SIGNED_SIGMOID, NEAT.ActivationFunction.SIGNED_SIGMOID,
            params)

    pop = NEAT.Population(g, params, True, 1.0)
    for generation in range(1000):
        #Evaluate genomes
        genome_list = NEAT.GetGenomeList(pop)
<<<<<<< HEAD:examples/ES-Hyper-NEAT_xor.py
    #    fitnesses = NEAT.EvaluateGenomeList_Parallel(genome_list, evaluate)
        fitnesses = NEAT.EvaluateGenomeList_Serial(genome_list, evaluate_xor, display=False)
        [genome.SetFitness(fitness) for genome, fitness in zip(genome_list, fitnesses)]

        best = max([x.GetLeader().GetFitness() for x in pop.Species])

=======
        fitnesses = NEAT.EvaluateGenomeList_Serial(genome_list, evaluate_xor, display = False)
        [genome.SetFitness(fitness[0]) for genome, fitness in zip(genome_list, fitnesses)]
        # Visualize best network's Genome
>>>>>>> origin/master:examples/TESTESHyperNEAT_xor.py
        net = NEAT.NeuralNetwork()
        pop.Species[0].GetLeader().BuildPhenotype(net)
        img = np.zeros((500, 500, 3), dtype=np.uint8)
        img += 10
        NEAT.DrawPhenotype(img, (0, 0, 500, 500), net )
        cv2.imshow("CPPN", img)
        # Visualize best network's Pheotype
        net = NEAT.NeuralNetwork()
        pop.Species[0].GetLeader().Build_ES_Phenotype(net, substrate, params)
        img = np.zeros((500, 500, 3), dtype=np.uint8)
        img += 10

        Utilities.DrawPhenotype(img, (0, 0, 500, 500), net, substrate=True )
        cv2.imshow("NN", img)
        cv2.waitKey(1)
        # Print best fitness
        print "---------------------------"
        print "Generation: ", generation
        print "max ", max([x.GetLeader().GetFitness() for x in pop.Species])
        if max([x.GetLeader().GetFitness() for x in pop.Species]) > 15.5:
            break
        #Epoch
        generations = generation
        pop.Epoch()


    return generations


gens = []
<<<<<<< HEAD:examples/ES-Hyper-NEAT_xor.py
for run in range(100):
    gen = getbest()
    print('Run:', run, 'Generations to solve XOR:', gen)
=======
for run in range(2):
    gen = getbest(run, "test.csv")
    print 'Run:', run, 'Generations to solve XOR:', gen
>>>>>>> origin/master:examples/TESTESHyperNEAT_xor.py
    gens += [gen]

avg_gens = sum(gens) / len(gens)

<<<<<<< HEAD:examples/ES-Hyper-NEAT_xor.py
print('All:', gens)
print('Average:', avg_gens)

=======
print 'All:', gens
print 'Average:', avg_gens
>>>>>>> origin/master:examples/TESTESHyperNEAT_xor.py