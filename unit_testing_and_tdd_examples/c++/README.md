# Unit Testing with C++
## ./src/main and ./test/main_test files
### BOOST
The main example currently has one function which makes a call to standard cout,  
this hello_world function has a a single test case with some mockup for capturing cout output.  
To run the test enter the following from a terminal in the boost directory:
`$g++ -I /path/to/header-only-library/boost_1_81_0/ main_test.cpp -o test`  
Then enter: `$./test`, the output should be:
`Running 1 test case...  

*** No errors detected`
The int main() function in main.cpp is commented out to avoid a compiler error:  
`error: conflicting declaration of C function ‘int main()’`
### GMOCK/GTEST
This is a TDD example of a file reading class with testing
There are no mocks... yet.
To run the test enter the following from a terminal in the gmock directory:
`$g++ GTestMain.cpp FileReader_TEST.cpp FileReader.cpp -lgtest -lgmock -pthread -o test_case`  
