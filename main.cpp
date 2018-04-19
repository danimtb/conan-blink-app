#include <iostream>

#ifdef WIRINGPI
    #include <wiringPi.h>
#endif


int main (void)
{
    #ifdef WIRINGPI
        wiringPiSetup();
        pinMode(0, OUTPUT);
    #endif

    while(1)
    {
        std::cout << "HIGH" << std::endl;
        #ifdef WIRINGPI
            digitalWrite(0, HIGH);
            delay(500);
        #endif

        std::cout << "LOW" << std::endl;
        #ifdef WIRINGPI
            digitalWrite(0, LOW);
            delay(500);
        #endif
    }

    return 0;
}
