#ifndef CLIENT_H
#define CLIENT_H

#include <ngrest/common/Service.h>
#include <vector>
#include <utility>

class client: public ngrest::Service {
public:

    // *method: POST
    int placing(int phase, std::vector<int> board);

    // *method: POST
    std::vector<int> moving(int phase, std::vector<int> board);

    // *method: POST
    int destroyPiece(int phase, std::vector<int> board);

};


#endif // CLIENT_H
