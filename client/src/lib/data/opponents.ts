import type { Fixture, Team } from '$client';

export class Opponents {
    teams: Team[];

    constructor(fixtures: Fixture[], teams: Map<string, Team>) {
        this.teams = fixtures
            .map((d) => teams.get(Opponents.opponentName(d)))
            .filter((d) => d !== undefined) as Team[];
    }

    private static sideSwitch(side: 'a' | 'h'): 'a' | 'h' {
        return side === 'h' ? 'a' : 'h';
    }

    private static opponentName(fixture: Fixture) {
        return fixture[Opponents.sideSwitch(fixture.side)].title;
    }
}
