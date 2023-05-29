#include <stdio.h>
#include <gtest/gtest.h>

GTEST_API_ int main(int argc, char **argv)
{
    printf("Running main() from gtest_main.cc, which must be linked in by the compiler...\n");
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
