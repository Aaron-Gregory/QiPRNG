# QiPRNG *(pronounced "chee"-PRNG)*
A DT**Q**W-**i**nspired **PRNG**. The output sequence is a string of the least significant bits from the measurement probabilities corresponding to a DTQW determined by an arbitrary Hamiltonian. The construction of the DTQW follows Childs' 2010 paper [On the relationship between continuous-and discrete-time quantum walk](https://link.springer.com/article/10.1007/s00220-009-0930-1).

For reference on the statistical tests, see [NIST's page](https://www.nist.gov/publications/statistical-test-suite-random-and-pseudorandom-number-generators-cryptographic).

# Usage Instructions

If using the C implementations of SP800-22 test suite, navigate to the ```scr``` directory and compile the library with ```cc -fPIC -shared -o sp800.so ./sp800_22_tests_c/src/*```. Data generation can then be invoked with ```python DataProcessing.py```, or ```sbatch generate.sh``` if running on a cluster.
