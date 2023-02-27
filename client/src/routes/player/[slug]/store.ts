import { writable, type Writable } from 'svelte/store';
import type { Match, Season, Shot, Team } from '$client';

export const matches: Writable<Match[]> = writable();
export const seasons: Writable<Season[]> = writable();
export const shots: Writable<Shot[]> = writable();
export const team: Writable<Team> = writable();
