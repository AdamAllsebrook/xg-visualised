import { writable, type Writable } from 'svelte/store';
import type { SimpleShot } from '$client';

export const allShotsAgainst: Writable<Record<string, SimpleShot[]> | null> = writable(null);

