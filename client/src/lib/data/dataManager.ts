import type { Player, Shot, Team, Match, Fixture } from '$client';
import { Opponents } from './opponents';
import { ShotData } from './shotData';

export const key = Symbol();

export class DataManager {
    player: Player;
    shots: Shot[];
    teams: Map<string, Team>;
    matches: Match[];
    fixtures: Fixture[];

    shotData: ShotData;
    opponents: Opponents;

    constructor(
        player: Player,
        shots: Shot[],
        teams: Map<string, Team>,
        matches: Match[],
        fixtures: Fixture[],
        nFixtures: number = 5,
    ) {
        this.player = player;
        this.shots = shots;
        this.teams = teams;
        this.matches = matches;
        this.fixtures = fixtures;

        this.shotData = new ShotData(shots);
        this.opponents = new Opponents(fixtures.slice(0, nFixtures), teams);
    }
}
