import { writable, type Writable } from 'svelte/store';
import type { LeagueShotsConceded } from '$lib/data/leagueShotsConceded';

export const leagueShotsConceded: Writable<LeagueShotsConceded | null> = writable(null);

