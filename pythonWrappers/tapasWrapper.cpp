#include <boost/python.hpp>
#include "../sources/tapas.h"

using namespace std;
using namespace boost::python;

BOOST_PYTHON_MODULE(tapas)
{
    class_<Tapas>("Tapas", init<std::string>())
        .def_readwrite("name", &Tapas::name)
    ;

    class_<Restaurant>("Restaurant", init<string, list>())
    	.def_readwrite("name", &Restaurant::name)
    	.def_readwrite("menu", &Restaurant::menu)
    ;
}