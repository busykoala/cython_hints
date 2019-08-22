#include "cfib.h"

int cfib(int n)
{
   if (n <= 1)
      return n;
   return cfib(n-1) + cfib(n-2);
}
