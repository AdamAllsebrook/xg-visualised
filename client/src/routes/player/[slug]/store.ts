import { writable, type Writable } from 'svelte/store';
import type { Match, Season, Team } from '$client';

export const matches: Writable<Match[]> = writable([]);
export const seasons: Writable<Season[]> = writable([]);
export const team: Writable<Team> = writable({
    id: 0,
    name: ''
});