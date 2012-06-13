#ifndef TAPAS_H
#define TAPAS_H

#include <boost/python.hpp>

class Tapas
{
public:
    Tapas(std::string name) { this->name = name; }
    std::string name;
};

class Restaurant
{
public:
    Restaurant(std::string name, boost::python::list menu) { this->name = name, this->menu = menu; }
    std::string name;
    boost::python::list menu;
};

#endif // TAPAS_H