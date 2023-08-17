#include <string>
#include <fstream>
#include <sstream>
#include <iostream>


class FileReader
{
public:
    FileReader(const char* filename) : filename_(filename)
    {
        std::ifstream stream_source;
        std::stringstream file_stream;
        stream_source.exceptions(std::ifstream::failbit | std::ifstream::badbit);
        try {
            stream_source.open(filename_);
            file_stream << stream_source.rdbuf();
            stream_source.close();
        } catch (std::ifstream::failure exception) {
            std::cout << "ERROR::READFILE_NOT_FOUND::" << exception.what() << std::endl;
            stream_source.close();
            throw exception;
        }
        file_data = file_stream.str();
        std::cout << "DEBUG::READFILE::" << file_data << std::endl;
    }
    std::string getData()
    {
        return file_data;
    }
private:
    const char* filename_;
    std::string file_data;
};


// class AIGEN_FileReader {
// public:
//     AIGEN_FileReader(const char* filename) : filename_(filename) {}
//     bool openFile() {
//         stream_.open(filename_);
//         return stream_.is_open();
//     }
// private:
//     const char* filename_;
//     std::ifstream stream_;
// };
// int main()
// {return 0;}

// class MockFileReader : public FileReader {
//  public:
//   MOCK_METHOD(std::string, ReadLine, (), (override));
//   MOCK_METHOD(void, Close, (), (override));
// };
//
// TEST(FileReaderTest, ReadLine) {
//   MockFileReader mock_file_reader;
//   EXPECT_CALL(mock_file_reader, ReadLine())
//       .WillOnce(Return("Hello"))
//       .WillOnce(Return("World"))
//       .WillOnce(Throw(std::runtime_error("End of file")));
//   EXPECT_EQ(mock_file_reader.ReadLine(), "Hello");
//   EXPECT_EQ(mock_file_reader.ReadLine(), "World");
//   EXPECT_THROW(mock_file_reader.ReadLine(), std::runtime_error);
// }
//
// TEST(FileReaderTest, Close) {
//   MockFileReader mock_file_reader("test");
//   EXPECT_CALL(mock_file_reader, Close())
//       .Times(1);
//   mock_file_reader.Close();
// }
