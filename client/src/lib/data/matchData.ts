import type { Match } from '$client';
import { sum } from './utils';

export class MatchData {
    matches: number;
    minutes: number;

    constructor(matches: Match[]) {
        this.matches = matches.length;
        this.minutes = matches.map((match) => match.time).reduce(sum);
    }
}
