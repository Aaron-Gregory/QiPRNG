#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 09:28:07 2021

@author: green
"""

from DataProcessing import *
import numpy as np
import time

# taken from
# x = np.where(np.less(data['test_000_tridiag'], 0.000001))[0]
# seeds = np.array(data['seed'], int)[x]
# for the current data from the cluster

seeds = [ 1008,  1323,   693,  1954,   694,  1199,   444,  1389,   508,
           950,   698,   636,   259,   135,  1521,  1837,  1523,  2407,
          1903,  1210,   770,  1465,  1023,  1591,  1843,  1844,  1340,
          1215,  2288,  2038,  1725,   151,  2421,  1224,   406,   469,
           156,  1921,  1732,  2488,  1291,   914,   790,  2492,   730,
           416,  1298,   543,   227,  1109,  1174,   545,  1048,   547,
           105,   863,   550,  2066,    49,  1183,  2191,  2004,  1626,
           177,   683,   998,  2008,  2196,   370,  2451,  1379,  2136,
           246,  2388,  1065,   877,   184,  2521,  2203,  3276,  4662,
          2712,  3154,  3785,  4414,  4352,  2905,  2591,  4165,  3662,
          4795,  4229,  3097,  4986,  4421,  4674,  4485,  4424,  2724,
          3291,  3355,  4803,  3356,  3419,  4241,  4621,  4055,  3236,
          2671,  2861,  3618,  2799,  3428,  3491,  3240,  3492,  3430,
          4878,  3494,  3873,  3684,  4629,  3057,  4126,  4630,  4378,
          4004,  4507,  4633,  3187,  2936,  3062,  4511,  4573,  4449,
          3128,  4515,  3195,  3131,  4013,  4015,  4332,  4772,  4521,
          4082,  3324,  4083,  3265,  4713,  3266,  3769,  3206,  4718,
          4025,  4975,  4658,  4596,  2645,  5859,  6301,  5169,  5549,
          5110,  5870,  6751,  7192,  5809,  7381,  7256,  6376,  6378,
          6001,  6819,  6193,  7200,  5502,  7075,  6447,  6071,  6700,
          5883,  5443,  7393,  6890,  6513,  6137,  6011,  6139,  6770,
          6711,  6270,  6521,  5516,  6273,  5835,  5207,  5712,  7410,
          6090,  5587,  5085,  5651,  5652,  7413,  6281,  5716,  5276,
          5466,  6413,  5406,  5469,  6538,  6667,  5849,  5724,  6104,
          6168,  5729,  5227,  5290,  5606,  7053,  6361,  5921,  5669,
          7750,  7556,  8003,  9513,  9136,  9263,  7942,  7754,  7817,
          8825,  7945,  8638,  9393,  8954,  8766,  7636,  8453,  7698,
          9021,  8457,  9778,  9152,  8711,  7832,  7645,  8650,  9720,
          9156,  7711,  9912,  7650,  9222,  9223,  8847,  8911,  8093,
          9287,  8597,  9730,  8536,  8474,  9858,  8413,  9797,  7850,
          9485,  9358,  9862,  8544,  9612,  8104,  8984,  8359,  9616,
          8675, 12388, 11317, 10185, 10690, 10754, 11132, 10440, 12142,
         11513, 12395, 11829, 12209, 10571, 12084, 12274, 12085, 10951,
         10952, 10890, 11583, 11773, 11837, 10324, 11082, 11902, 11274,
         10204, 11151, 11152, 11592, 11845, 11344, 12228, 10653, 11913,
         12103, 11410, 11223, 11539, 11605, 12362, 12172, 11102, 11796,
         11040, 11480, 12174, 12112, 12428, 10538, 10036, 10289, 11615,
         12373, 10041, 12247, 11870, 10799, 12249, 10235, 10929, 10552,
         12128, 11248, 10870, 11942, 10495, 13143, 14152, 14531, 13083,
         13461, 14910, 13777, 12833, 12770, 14092, 13715, 14722, 13150,
         12773, 13720, 13217, 13595, 12966, 14163, 14415, 13660, 12591,
         14668, 14857, 14858, 13915, 13289, 12659, 13226, 12850, 13542,
         13291, 14172, 14991, 13481, 14992, 14113, 14428, 13928, 13741,
         14810, 13425, 13114, 13177, 15003, 13493, 13935, 13118, 12615,
         14881, 14693, 14882, 14003, 14443, 13941, 12934, 14760, 13565,
         14257, 14132, 13628, 14574, 14763, 14451, 13131, 12756, 13007,
         14897, 14018, 13578, 13957, 14587, 13832, 14523, 15159, 14840,
         14150, 16293, 14968, 15981, 15605, 17366, 16236, 15985, 16804,
         17246, 15361, 15235, 16870, 16935, 16118, 16307, 16309, 15743,
         15682, 17004, 15370, 17256, 17446, 16819, 17259, 16821, 15690,
         15188, 17200, 15063, 16762, 16889, 16388, 17268, 15508, 17207,
         15823, 16517, 15955, 16331, 16268, 15956, 17399, 16708, 15515,
         15704, 16152, 17220, 15965, 16025, 16089, 17283, 16783, 17409,
         15901, 17348, 16660, 16032, 15278, 16348, 15596, 15849, 17296,
         17743, 17870, 17173, 18437, 19005, 19194, 19760, 18694, 19260,
         18757, 19386, 19827, 18004, 19829, 19452, 17882, 18512, 18827,
         18009, 18766, 19960, 18767, 19521, 19458, 18144, 19717, 19340,
         19905, 19279, 18653, 18087, 19659, 19724, 19218, 17901, 18467,
         17903, 18658, 19539, 18471, 17592, 19415, 19856, 18288, 18915,
         17596, 17916, 18859, 18921, 18104, 18922, 19866, 19616, 19869,
         18488, 20749, 22451, 20499, 20311, 20942, 20564]


def make_file_and_test(s):
    gen_exact, gen_diag, gen_tridiag, gen_dense = construct_PRNG_tuple(seeds[s], N_DIMS)
    generate_datafile("temp.bin", gen_tridiag, N_BYTES, verbosity=2)
    
    key = "temp"
    pvals_buffer = ctypes.pointer((ctypes.c_double * NUMOFPVALS)())
    filename_buffer = ctypes.create_string_buffer(len(key) + 1)
    filename_buffer.value = key.encode("utf-8")
    sp800.run_tests(pvals_buffer, filename_buffer)
    
    pvals = np.array(pvals_buffer.contents[:])
    
    shutil.rmtree(STATS_DATA_DIR + key)
    
    return pvals

def get_bits(s):
    gen_exact, gen_diag, gen_tridiag, gen_dense = construct_PRNG_tuple(seeds[s], N_DIMS)
    
    seq = np.zeros((8, N_BYTES), dtype = bool)
    t = time.time()
    print("starting gen")
    for i,b in enumerate(gen_tridiag):
        if i >= N_BYTES:
            break
        
        for p in range(8):
            seq[p][i] = (b // 2**p) % 2
    
    print("gen time: %.2f seconds" % (time.time() - t))
    
    print("counts: ", np.sum(seq, axis = 1))
    
    return seq

for i in range(10):
    get_bits(i)

