#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
gaussian("gau1.dat", 1000000);

//Gaussian random numbers
gaussian("gau2.dat", 1000000);

new_type("gau1.dat","gau2.dat","gau3.dat",1000000);

//Mean of uniform
//printf("%lf",mean("uni.dat"));
return 0;
}


