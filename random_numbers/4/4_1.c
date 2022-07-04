#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begin
{

//Gaussian random numbers
uniform("uni1.dat",1000000);
uniform("uni2.dat",1000000);
two_time("uni1.dat","uni2.dat","4th.dat", 1000000);

//Mean of uniform
//printf("%lf",mean("uni.dat"));
return 0;
}


