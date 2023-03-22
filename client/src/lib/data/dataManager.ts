import type { Player, Shot, Team, Match, Fixture } from '$client';
import { ShotData } from './shotData';

export class DataManager {
    player: Player;
    shots: Shot[];
    teams: Team[];
    matches: Match[];
    fixtures: Fixture[];

    shotData: ShotData;

    constructor(
        player: Player,
        shots: Shot[],
        teams: Team[],
        matches: Match[],
        fixtures: Fixture[],
    ) {
        this.player = player;
        this.shots = shots;
        this.teams = teams;
        this.matches = matches;
        this.fixtures = fixtures;

        this.shotData = new ShotData(shots);
    }
}
