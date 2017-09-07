//
// Created by Sadegh on 9/8/2017 AD.
//

#include <cstdlib>
#include "AIPlayer.h"
#include <iostream>

int AIPlayer::place() {
    vector<int> empty_positions = game.get_empty_positions();

    for(int e : empty_positions) {
        cout << e << ", ";
    }
    cout << endl;

    unsigned long randomIndex = rand() % empty_positions.size();
    return empty_positions[randomIndex];
}

pair<int, int> AIPlayer::move() {

//    int origin = 0; int destination = 10;
//    bool can_move = game.is_neighbor_position(origin, destination);

    vector< pair<int, int> > valid_movements = game.get_valid_movements();
    unsigned long randomIndex = rand() % valid_movements.size();
    return valid_movements[randomIndex];
}

int AIPlayer::select_enemy_piece() {

//    vector<int> board = game.get_board();
//    do something whit board!

    vector<int> enemy_positions = game.get_enemy_positions();
    unsigned long randomIndex = rand() % enemy_positions.size();
    return enemy_positions[randomIndex];
}
