# Boost Unit Testing with C++
## ./src/main and ./test/main_test files
The main example currently has one function which makes a call to standard cout,  
this hello_world function has a a single test case with some mockup for capturing cout output.  
To run the test enter the following from a terminal:
`$g++ -I /path/to/header-only-library/boost_1_81_0/ main_test.cpp -o test`  
Then enter: `$./test`, the output should be:
`Running 1 test case...  

*** No errors detected`
The int main() function in main.cpp is commented out to avoid a compiler error:  
`error: conflicting declaration of C function ‘int main()’`
