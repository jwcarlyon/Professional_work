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

TEST(FileReaderTest, InvalidFileThrowsException)
{
    // Arrange
    const char* invalid_filename = "nonexistent.txt";

    // Act and Assert
    EXPECT_THROW(FileReader reader(invalid_filename), std::ifstream::failure);
}
