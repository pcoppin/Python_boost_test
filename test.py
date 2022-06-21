import BOOST_test


print( BOOST_test.greet() )

# Compiles on Ubuntu with: g++ -shared -fPIC -I /usr/include/python3.8/ BOOST_test.cpp -o BOOST_test.so -lboost_system -lboost_python38 -lpython3.8
# Compiles on Ubuntu with: g++ -shared -fPIC -I /usr/include/python3.8/ BOOST_test.cpp -o BOOST_test.so -lboost_system -lboost_python38
