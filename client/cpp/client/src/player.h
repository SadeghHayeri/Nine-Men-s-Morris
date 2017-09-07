//
// Created by Sadegh on 9/8/2017 AD.
//

#ifndef CLIENT_PLAYER_H
#define CLIENT_PLAYER_H

#include "game.h"

class Player {
public:
    Player(Game& _game) : game(_game) {}

    bool can_i_fly() {
        return game.can_fly();
    }

    virtual int place() = 0;
    virtual pair<int,int> move() = 0;
    virtual int select_enemy_piece() = 0;

protected:
    Game& game;
};


#endif //CLIENT_PLAYER_H
