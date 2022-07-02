#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
//Uniform random numbers
//uniform("uni.dat", 1000000);

//Gaussian random numbers
//gaussian("gau.dat", 1000000);

new_type_root("gau3.dat","gau4.dat",1000000);
//Mean of uniform
//printf("%lf",mean("uni.dat"));
return 0;
}


