#include "cppfib.h"

int cppfib(int n) {
   if (n <= 1)
      return n;
   return cppfib(n-1) + cppfib(n-2);
}
