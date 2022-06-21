char const* greet()
{
   return "hello, world";
}

#include <boost/python.hpp>

BOOST_PYTHON_MODULE(BOOST_test)
{
    using namespace boost::python;
    def("greet", greet);
}

//int main(){}
