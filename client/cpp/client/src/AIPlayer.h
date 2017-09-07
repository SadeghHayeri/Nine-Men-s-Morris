//
// Created by Sadegh on 9/8/2017 AD.
//

#ifndef CLIENT_AIPLAYER_H
#define CLIENT_AIPLAYER_H

#include "player.h"
#include "game.h"
#include <utility>

class AIPlayer : Player {
public:
    AIPlayer(Game& _game) : Player(_game) {}

    int place() override;
    pair<int,int> move() override;
    int select_enemy_piece() override;

private:
};


#endif //CLIENT_AIPLAYER_H
