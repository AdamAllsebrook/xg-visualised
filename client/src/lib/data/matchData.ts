import type { Match } from '$client';
import { sum } from './utils';

export class MatchData {
    matches: number;
    minutes: number;
    homeMinutes: number;
    awayMinutes: number;

    constructor(matches: Match[]) {
        this.matches = matches.length;
        this.minutes = matches.map((match) => match.time).reduce(sum);

        this.homeMinutes = matches.filter((match) => match.h_a === 'h').map((match) => match.time).reduce(sum, 0);
        this.awayMinutes = this.minutes - this.homeMinutes;
    }
}
