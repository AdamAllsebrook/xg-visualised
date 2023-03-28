import type { Player, Shot, Team, Match, Fixture } from '$client';
import { MatchData } from './matchData';
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
    matchData: MatchData
    opponents: Opponents;

    constructor(
        player: Player,
        shots: Shot[],
        teams: Team[], 
        matches: Match[],
        fixtures: Fixture[],
        nFixtures: number = 5,
    ) {
        this.player = player;
        this.shots = shots;
        this.teams = new Map(teams.map(t => [t.title, t]));
        this.matches = matches;
        this.fixtures = fixtures;

        this.shotData = new ShotData(shots);
        this.matchData = new MatchData(matches);
        this.opponents = new Opponents(fixtures.slice(0, nFixtures), this.teams);
    }
}
