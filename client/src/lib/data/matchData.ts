import type { Match } from '$client';
import { sum } from './utils';

export class MatchData {
    minutes: number;

    constructor(matches: Match[]) {
        this.minutes = matches.map((match) => match.time).reduce(sum);
    }
}
