#define BOOST_TEST_MODULE main_test
#include <boost/lambda/lambda.hpp>
#include <boost/test/included/unit_test.hpp>
#include <boost/test/tools/output_test_stream.hpp>
#include "../src/main.cpp"

struct cout_redirect
{
    cout_redirect( std::streambuf * new_buffer )
        : old( std::cout.rdbuf( new_buffer ) )
    { }

    ~cout_redirect( )
    {
        std::cout.rdbuf( old );
    }

private:
    std::streambuf* old;
};

BOOST_AUTO_TEST_CASE(hello_world_test_case) {
    boost::test_tools::output_test_stream output;
    {
        cout_redirect guard(output.rdbuf());

        hello_world();
    }
    BOOST_CHECK(output.is_equal("Hello World!\n"));
}
