import type { Fixture, SimpleShot, Team } from '$client';
import { SimpleShotData } from './shotData';

export class Opponents {
    teams: Team[];
    shotsConceded: SimpleShotData | null = null;
    teamShots: Map<string, SimpleShot[]> | null = null;

    constructor(fixtures: Fixture[], teams: Map<string, Team>) {
        this.teams = fixtures
            .map((d) => teams.get(Opponents.opponentName(d)))
            .filter((d) => d !== undefined) as Team[];
    }

    setShotsConceded(shotsConceded: Map<string, SimpleShot[]>) {
        this.shotsConceded = new SimpleShotData(
            this.teams
                .map((team) => shotsConceded.get(team.title) || [])
                .reduce((arr, shots) => arr.concat(shots), []),
        );
        this.teamShots = new Map(
            [...shotsConceded].filter(([title]) =>
                this.teams.map((team) => team.title).includes(title),
            ),
        );
    }

    private static sideSwitch(side: 'a' | 'h'): 'a' | 'h' {
        return side === 'h' ? 'a' : 'h';
    }

    private static opponentName(fixture: Fixture) {
        return fixture[Opponents.sideSwitch(fixture.side)].title;
    }
}
