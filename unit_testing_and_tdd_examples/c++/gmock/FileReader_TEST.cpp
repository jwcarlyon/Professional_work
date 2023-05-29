#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "FileReader.cpp"

// using ::testing::Return;
// using ::testing::Throw;
using namespace testing;

TEST(FileReaderTest, ReadFile)
{
    FileReader file_reader("testFile.txt");
    EXPECT_EQ(file_reader.getData(), "test data\n");
}
