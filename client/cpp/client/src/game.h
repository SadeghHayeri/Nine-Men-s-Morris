//
// Created by Sadegh on 9/7/2017 AD.
//

//--------------- GRAPH SCHEMA ------------
//     0------------1------------2
//     |            |            |
//     |   8--------9------10    |
//     |   |        |       |    |
//     |   |   16--17--18   |    |
//     |   |   |        |   |    |
//     7---15--23      19--11----3
//     |   |   |        |   |    |
//     |   |   22--21--20   |    |
//     |   |        |       |    |
//     |   14------13------12    |
//     |            |            |
//     6------------5------------4

#ifndef CLIENT_GAME_H
#define CLIENT_GAME_H

#include <vector>
#include <string>
#include <utility>

using namespace std;

class Game {
public:
    Game();
    void set_game(vector<int> new_board, int new_phase);
    bool can_fly();
    bool is_neighbor_position(int a, int b);

    vector<int> get_board();
    vector<int> get_empty_positions();
    vector<int> get_insider_positions();
    vector<int> get_enemy_positions();
    vector< pair<int, int> > get_valid_movements();

private:
    int phase;
    vector<int> board;
    vector< pair<int,int> > graph;

    vector<int> empty_positions;
    vector<int> insider_positions;
    vector<int> enemy_positions;
    vector< pair<int, int> > valid_movements;
};


#endif //CLIENT_GAME_H
