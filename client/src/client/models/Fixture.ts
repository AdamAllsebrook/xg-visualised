/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { FixtureTeam } from './FixtureTeam';

export type Fixture = {
    id: number;
    side: ('h' | 'a');
    'h': FixtureTeam;
    'a': FixtureTeam;
    datetime: string;
};

