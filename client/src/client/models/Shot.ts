/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type Shot = {
    id: number;
    match_id: number;
    minute: number;
    xG: number;
    player: string;
    player_assisted?: string;
    season: number;
    situation: string;
    shotType: string;
    result: string;
    'X': number;
    'Y': number;
    h_team: string;
    a_team: string;
    h_goals: number;
    a_goals: number;
    h_a: ('h' | 'a');
    date: string;
};

